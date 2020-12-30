from xml.dom import minidom


def write_code(list, tag):
    for j in range(len(list.childNodes)):
        for k in range(len(list.childNodes[j].childNodes)):
            if list.childNodes[j].childNodes[k].nodeName == tag:
                if tag == "Attribute":
                    f.write(list.childNodes[j].childNodes[k].attributes["Name"].value + ", ")
                    attributes.append(list.childNodes[j].childNodes[k].attributes["Name"].value)
                if tag == "Operation":
                    f.write("\n\tdef " + list.childNodes[j].childNodes[k].attributes["Name"].value + "(self, ")
                    for w in range(len(list.childNodes[j].childNodes[k].childNodes)):
                        for z in range(len(list.childNodes[j].childNodes[k].childNodes[w].childNodes)):
                            if list.childNodes[j].childNodes[k].childNodes[w].childNodes[z].nodeName == "Parameter":
                                f.write(list.childNodes[j].childNodes[k].childNodes[w].childNodes[z].attributes["Name"].value + ", ")
                    f.write("):\n\t\t# insert body here\n")
                    try:
                        list.childNodes[j].childNodes[k].attributes["ReturnType"]
                        f.write("\t\treturn NotImplemented\n")
                    except KeyError:
                        NotImplemented
                    if len(list.childNodes[j].childNodes[k].childNodes) == 0:
                        break
                    for w in range(len(list.childNodes[j].childNodes[k].childNodes)):
                        if list.childNodes[j].childNodes[k].childNodes[w].nodeName == "ReturnType":
                            f.write("\t\treturn NotImplemented\n")


def extract(temp_var, tag):
    temp = []
    for index in range(len(temp_var)):
        if temp_var[index].parentNode.nodeName == 'ModelChildren':
            if tag == 'Class':
                temp.append(temp_var[index])
            if tag == 'Generalization':
                temp.append((temp_var[index].attributes['From'].value, temp_var[index].attributes['To'].value))
    return temp


def verify(list):
    for i in range(len(fromTo)):
        if list.attributes["Id"].value == fromTo[i][1]:
            return association(fromTo[i][0])
    return ""


def association(id):
    for i in range(len(classes)):
        if id == classes[i].attributes["Id"].value:
            return classes[i].attributes["Name"].value
    return "NotDefined"


f = open("interface.py", "w")
class_diagram = minidom.parse('case_use/class_diagram_3.xml')
classes = class_diagram.getElementsByTagName('Class')
classes = extract(classes, 'Class')
attributes = []
fromTo = class_diagram.getElementsByTagName('Generalization')
fromTo = extract(fromTo, "Generalization")

for i in range(len(classes)):
    f.write("\n\nclass " + classes[i].attributes['Name'].value + "(" + verify(classes[i]) + ")" + ":\n\tdef __init__("
                                                                                                  "self, ")
    write_code(classes[i], "Attribute")
    f.write("):\n")
    if len(verify(classes[i])) > 0:
        f.write("\t\tsuper().__init__()\n")
    for j in range(len(attributes)):
        f.write("\t\tself." + attributes[j] + " = " + attributes[j] + "\n")
    attributes.clear()
    write_code(classes[i], "Operation")

f.close()
