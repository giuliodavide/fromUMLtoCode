def write_code(list, tag, output_file):
    attributes = []
    for j in range(len(list.childNodes)):
        for k in range(len(list.childNodes[j].childNodes)):
            if list.childNodes[j].childNodes[k].nodeName == tag:
                if tag == "Attribute":
                    output_file.write(list.childNodes[j].childNodes[k].attributes["Name"].value + ", ")
                    attributes.append(list.childNodes[j].childNodes[k].attributes["Name"].value)
                if tag == "Operation":
                    output_file.write(
                        "\n\tdef " + list.childNodes[j].childNodes[k].attributes["Name"].value + "(self, ")
                    for w in range(len(list.childNodes[j].childNodes[k].childNodes)):
                        for z in range(len(list.childNodes[j].childNodes[k].childNodes[w].childNodes)):
                            if list.childNodes[j].childNodes[k].childNodes[w].childNodes[z].nodeName == "Parameter":
                                output_file.write(
                                    list.childNodes[j].childNodes[k].childNodes[w].childNodes[z].attributes[
                                        "Name"].value + ", ")
                    output_file.write("):\n\t\t# insert body here\n")
                    try:
                        list.childNodes[j].childNodes[k].attributes["ReturnType"]
                        output_file.write("\t\treturn NotImplemented\n")
                    except KeyError:
                        NotImplemented
                    if len(list.childNodes[j].childNodes[k].childNodes) != 0:
                        for w in range(len(list.childNodes[j].childNodes[k].childNodes)):
                            if list.childNodes[j].childNodes[k].childNodes[w].nodeName == "ReturnType":
                                output_file.write("\t\treturn NotImplemented\n")
    return attributes


def extract(temp_var, tag):
    temp = []
    for index in range(len(temp_var)):
        if temp_var[index].parentNode.nodeName == 'ModelChildren':
            if tag == 'Class' or tag == 'InstanceSpecification':
                temp.append(temp_var[index])
            if tag == 'Generalization':
                temp.append((temp_var[index].attributes['From'].value, temp_var[index].attributes['To'].value))
    return temp


def verify(index, fromTo, classes):
    for i in range(len(fromTo)):
        if classes[index].attributes["Id"].value == fromTo[i][1]:
            return association(fromTo[i][0], classes)
    return ""


def association(id, classes):
    for i in range(len(classes)):
        if id == classes[i].attributes["Id"].value:
            return classes[i].attributes["Name"].value
    return "NotDefined"


def classof(instance):
    for i in range(len(instance.childNodes)):
        if instance.childNodes[i].nodeName == "Classifiers":
            for j in range(len(instance.childNodes[i].childNodes)):
                if instance.childNodes[i].childNodes[j].nodeName == 'Class':
                    return instance.childNodes[i].childNodes[j].attributes['Name'].value


def valueof(instance):
    var = []
    for i in range(len(instance.childNodes)):
        element = False
        if instance.childNodes[i].nodeName == 'Slots':
            element = True
    if element:
        return ""
    for i in range(len(instance.childNodes)):
        if instance.childNodes[i].nodeName == 'Slots':
            for j in range(len(instance.childNodes[i].childNodes)):
                if instance.childNodes[i].childNodes[j].nodeName == 'Slot':
                    for k in range(len(instance.childNodes[i].childNodes[j].childNodes)):
                        if instance.childNodes[i].childNodes[j].childNodes[k].nodeName == "Values":
                            for m in range(len(instance.childNodes[i].childNodes[j].childNodes[k].childNodes)):
                                found = False
                                if instance.childNodes[i].childNodes[j].childNodes[k].childNodes[m].nodeName == "CompositeValueSpecification":
                                    for n in range(len(instance.childNodes[i].childNodes[j].childNodes[k].childNodes[m].childNodes)):
                                        if instance.childNodes[i].childNodes[j].childNodes[k].childNodes[m].childNodes[n].nodeName == "Value":
                                            found = True
                                            for p in range(len(instance.childNodes[i].childNodes[j].childNodes[k].childNodes[m].childNodes[n].childNodes)):
                                                if instance.childNodes[i].childNodes[j].childNodes[k].childNodes[m].childNodes[n].childNodes[p].nodeName == "InstanceSpecification":
                                                    var.append(instance.childNodes[i].childNodes[j].childNodes[k].childNodes[m].childNodes[n].childNodes[p].attributes["Name"].value)
                                    if not found:
                                        var.append(instance.childNodes[i].childNodes[j].childNodes[k].childNodes[m].attributes["Value"].value)
    return tuple(var)
