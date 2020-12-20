from xml.dom import minidom

class_diagram = minidom.parse('case_use/class_diagram.xml')

classes = class_diagram.getElementsByTagName('Class')

for i in range(len(classes)):
    if classes[i].parentNode.nodeName == "Models":
        for j in range(len(classes[i].childNodes)):
            for k in range(len(classes[i].childNodes[j].childNodes)):
                if classes[i].childNodes[j].childNodes[k].nodeName == "Attribute":
                    print(classes[i].childNodes[j].childNodes[k].attributes["Name"].value + " is an attribute of " +
                          classes[i].attributes['Name'].value)
                if classes[i].childNodes[j].childNodes[k].nodeName == "Operation":
                    print(classes[i].childNodes[j].childNodes[k].attributes["Name"].value + " is an operation of " +
                          classes[i].attributes['Name'].value)
