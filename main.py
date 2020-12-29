from xml.dom import minidom


def write_code(classes, type):
    for k in range(len(classes.childNodes[j].childNodes)):
        if classes.childNodes[j].childNodes[k].nodeName == type:
            if type == "Attribute":
                f.write(classes.childNodes[j].childNodes[k].attributes["Name"].value + ", ")
            if type == "Operation":
                f.write("\n\tdef " + classes.childNodes[j].childNodes[k].attributes["Name"].value + "():\n")


def clean_classes(temp):
    temp_classes = []
    for i in range(len(temp)):
        if temp[i].parentNode.nodeName == "ModelChildren":
            temp_classes.append(temp[i])
    return temp_classes


f = open("interface.py", "a")
class_diagram = minidom.parse('case_use/class_diagram.xml')
classes = class_diagram.getElementsByTagName('Class')
classes = clean_classes(classes)

for i in range(len(classes)):
    f.write("\n\nclass " + classes[i].attributes['Name'].value + ":\n\tdef __init__(self, ")
    for j in range(len(classes[i].childNodes)):
        write_code(classes[i], "Attribute")
        # for k in range(len(classes[i].childNodes[j].childNodes)):
        #     if classes[i].childNodes[j].childNodes[k].nodeName == "Attribute":
        #         # attributes.append(classes[i].childNodes[j].childNodes[k].attributes["Name"].value)
        #         f.write(classes[i].childNodes[j].childNodes[k].attributes["Name"].value + ", ")
    f.write("):\n\t\t")
    for j in range(len(classes[i].childNodes)):
        write_code(classes[i], "Operation")
    # if classes[i].childNodes[j].childNodes[k].nodeName == "Operation":
    #     operations.append(classes[i].childNodes[j].childNodes[k].attributes["Name"].value)
    #     if len(classes[i].childNodes[j].childNodes[k].childNodes) == 0:
    #         returning.append(False)
    #     for w in range(len(classes[i].childNodes[j].childNodes[k].childNodes)):
    #         if classes[i].childNodes[j].childNodes[k].childNodes[w].nodeName != "ReturnType":
    #             returning.append((False, k))
    #         else:
    #             returning.append((True, k))

    # for j in range(len(attributes)):
    #     f.write(attributes[j] + ", ")
    # f.write("):\n\t\t")
    #
    # for j in range(len(attributes)):
    #     f.write("self." + attributes[j] + " = " + attributes[j] + "\n\t\t")
    #
    # for j in range(len(operations)):
    #     f.write("\n\tdef " + operations[j] + "():\n")
    #     if returning[k]:
    #         f.write("\t\treturn NotImplemented\n")

f.close()
