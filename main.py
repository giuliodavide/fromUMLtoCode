from xml.dom import minidom
import argparse
import os
from utility import *


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--class", required=True,
                help="class diagram we want to traduce")
ap.add_argument("-obj", "--object", required=False,
                help="required if you want also a main.py related to the class diagram", default=None)
args = vars(ap.parse_args())

try:
    output_class = open("output/class.py", "w")
except FileNotFoundError:
    os.mkdir("output")
finally:
    output_class = open("output/class.py", "w")

if args["object"] is not None:
    try:
        output_main = open("output/main.py", "w")
    except FileNotFoundError:
        os.mkdir("output")
    finally:
        output_main = open("output/main.py", "w")

class_diagram = minidom.parse(args["class"])
obj_diagram = minidom.parse(args["object"])
classes = class_diagram.getElementsByTagName('Class')
classes = extract(classes, 'Class')
if args["object"] is not None:
    instances = obj_diagram.getElementsByTagName('InstanceSpecification')
    instances = extract(instances, 'InstanceSpecification')
attributes = []
fromTo = class_diagram.getElementsByTagName('Generalization')
fromTo = extract(fromTo, "Generalization")

for i in range(len(classes)):
    output_class.write("\n\nclass " + classes[i].attributes['Name'].value + "(" + verify(i, fromTo, classes) + ")" + ":\n\tdef __init__("
                                                                                                  "self, ")
    attributes = write_code(classes[i], "Attribute", output_class)
    output_class.write("):\n")
    if len(verify(i, fromTo, classes)) > 0:
        output_class.write("\t\tsuper().__init__()\n")
    for j in range(len(attributes)):
        output_class.write("\t\tself." + attributes[j] + " = " + attributes[j] + "\n")
    attributes.clear()
    temp = write_code(classes[i], "Operation", output_class)

output_class.close()

if instances is not None:
    for i in range(len(instances)):
        output_main.write(instances[i].attributes['Name'].value + " = " + classof(instances[i]))

output_main.close()
