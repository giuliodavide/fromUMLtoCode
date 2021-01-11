from xml.dom import minidom
import argparse
import os
from utility import *


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--class", required=True,
                help="class diagram we want to traduce")
ap.add_argument("-o", "--output", required=False,
                help="output path in which we want to save the code, you need to write the name.py", default="output/interface.py")
args = vars(ap.parse_args())

try:
    f = open(args["output"], "w")
except FileNotFoundError:
    _ = str(args["output"]).split("/")
    _ = [_[index] for index in range(0, len(_) - 1)]
    path = ""
    for i in range(len(_)):
        path += _[i] + "/"
    os.makedirs(path)
finally:
    f = open(args["output"], "w")

class_diagram = minidom.parse(args["class"])
classes = class_diagram.getElementsByTagName('Class')
classes = extract(classes, 'Class')
attributes = []
fromTo = class_diagram.getElementsByTagName('Generalization')
fromTo = extract(fromTo, "Generalization")

for i in range(len(classes)):
    f.write("\n\nclass " + classes[i].attributes['Name'].value + "(" + verify(i, fromTo, classes) + ")" + ":\n"
                                                                                                          "\tdef __init__(self, ")
    write_code(classes[i], "Attribute", f, attributes)
    f.write("):\n")
    if len(verify(i, fromTo, classes)) > 0:
        f.write("\t\tsuper().__init__()\n")
    for j in range(len(attributes)):
        f.write("\t\tself." + attributes[j] + " = " + attributes[j] + "\n")
    attributes.clear()
    write_code(classes[i], "Operation", f)

f.close()
