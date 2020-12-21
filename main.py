from xml.dom import minidom

f = open("interface.py", "x")
class_diagram = minidom.parse('case_use/class_diagram_1.xml')
classes = class_diagram.getElementsByTagName('Class')
attributes = []
operations = []

for i in range(len(classes)):
    attributes.clear()
    operations.clear()
    if classes[i].parentNode.nodeName == "ModelChildren":
        f.write("\n\nclass " + classes[i].attributes['Name'].value + ":\n\tdef __init__(self, ")
        for j in range(len(classes[i].childNodes)):
            for k in range(len(classes[i].childNodes[j].childNodes)):
                if classes[i].childNodes[j].childNodes[k].nodeName == "Attribute":
                    print(classes[i].childNodes[j].childNodes[k].attributes["Name"].value + " is an attribute of " +
                          classes[i].attributes['Name'].value)
                    attributes.append(classes[i].childNodes[j].childNodes[k].attributes["Name"].value)
                if classes[i].childNodes[j].childNodes[k].nodeName == "Operation":
                    print(classes[i].childNodes[j].childNodes[k].attributes["Name"].value + " is an operation of " +
                          classes[i].attributes['Name'].value)
                    operations.append(classes[i].childNodes[j].childNodes[k].attributes["Name"].value)

        for j in range(len(attributes)):
            f.write(attributes[j] + ", ")
        f.write("):\n\t\t")

        for j in range(len(attributes)):
            f.write("self." + attributes[j] + " = " + attributes[j] + "\n\t\t")

        for j in range(len(operations)):
            f.write("\n\t\tdef " + operations[j] + "():\n")

f.close()
