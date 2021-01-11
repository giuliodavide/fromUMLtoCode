def write_code(list, tag, output_file):
    attributes = []
    for j in range(len(list.childNodes)):
        for k in range(len(list.childNodes[j].childNodes)):
            if list.childNodes[j].childNodes[k].nodeName == tag:
                if tag == "Attribute":
                    output_file.write(list.childNodes[j].childNodes[k].attributes["Name"].value + ", ")
                    attributes.append(list.childNodes[j].childNodes[k].attributes["Name"].value)
                if tag == "Operation":
                    output_file.write("\n\tdef " + list.childNodes[j].childNodes[k].attributes["Name"].value + "(self, ")
                    for w in range(len(list.childNodes[j].childNodes[k].childNodes)):
                        for z in range(len(list.childNodes[j].childNodes[k].childNodes[w].childNodes)):
                            if list.childNodes[j].childNodes[k].childNodes[w].childNodes[z].nodeName == "Parameter":
                                output_file.write(list.childNodes[j].childNodes[k].childNodes[w].childNodes[z].attributes["Name"].value + ", ")
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
            if tag == 'Class':
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
