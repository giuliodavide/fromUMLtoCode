# fromUMLtoCode

This script returns an incomplete code of a diagram/object class _.xml_ exported with Visual Paradigm. It has been tested with some working examples available on the Community Edition of the program itself. The output of the entire script will be a output/ folder which will have a main.py and an interface.py, based on the choices made by the user.


## Usage

To run the script, open a terminal in the directory of the project and type the following command:

''' python main.py [-c/--class "path/to/class.xml"] [-obj/--object "path/to/object.xml"] '''

In output you will have up to two files: main.py for the object diagram, interface.py for the class diagram. It won't work if you don't specify at least one argument.

## Features

The script can detect:
- Classes
- Attributes
- Operation
 - Parameters
 - Return
- Relation of Generalization
- Instantiation of a class

In the case you will specify all the arguments on the terminal, the main.py file in output will automatically import all the class in the interface.py file.

## Known Issues

Path with whitespace will cause problems. We suggest to copy the file in a path without whitespace.
