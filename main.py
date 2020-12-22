from xml.dom import minidom

f = open("interface.py", "a")
class_diagram = minidom.parse('case_use/class_diagram_3.xml')
temp = class_diagram.getElementsByTagName('Class')
classes = []
attributes = []
operations = []
returning = []

for i in range(len(temp)):
    if temp[i].parentNode.nodeName == "ModelChildren":
        classes.append(temp[i])

temp.clear()

for i in range(len(classes)):
    attributes.clear()
    operations.clear()
    f.write("\n\nclass " + classes[i].attributes['Name'].value + ":\n\tdef __init__(self, ")
    for j in range(len(classes[i].childNodes)):
        for k in range(len(classes[i].childNodes[j].childNodes)):
            if classes[i].childNodes[j].childNodes[k].nodeName == "Attribute":
                attributes.append(classes[i].childNodes[j].childNodes[k].attributes["Name"].value)
            if classes[i].childNodes[j].childNodes[k].nodeName == "Operation":
                operations.append(classes[i].childNodes[j].childNodes[k].attributes["Name"].value)
                if len(classes[i].childNodes[j].childNodes[k].childNodes) == 0:
                    returning.append(False)
                for w in range(len(classes[i].childNodes[j].childNodes[k].childNodes)):
                    if classes[i].childNodes[j].childNodes[k].childNodes[w].nodeName != "ReturnType":
                        returning.append(False)
                    else:
                        returning.append(True)

    for j in range(len(attributes)):
        f.write(attributes[j] + ", ")
    f.write("):\n\t\t")

    for j in range(len(attributes)):
        f.write("self." + attributes[j] + " = " + attributes[j] + "\n\t\t")

    for j in range(len(operations)):
        f.write("\n\tdef " + operations[j] + "():\n")
        if returning[j]:
            f.write("\t\treturn NotImplemented\n")

f.close()
