import argparse

'''
All of these pertain to different options of preset action that you can set to
an optional argument that 


STORE: 
stores the input value to the Namespace object. (This is the default action.)
STORE_CONST:
stores a constant value when the corresponding optional arguments are specified.
STORE_TRUE:
stores the Boolean value True when the corresponding optional argument is specified and stores a False elsewhere.
STORE_FALSE:
stores the Boolean value False when the corresponding optional argument is specified and stores True elsewhere.
APPEND:
stores a list, appending a value to the list each time the option is provided.
APPEND_CONST:
stores a list appending a constant value to the list each time the option is provided.
COUNT:
stores an int that is equal to the times the option has been provided.
HELP:
shows a help text and exits.
VERSION:
shows the version of the program and exits.
'''

my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'
my_parser.add_argument('-a', action='store')
my_parser.add_argument('-b', action='store_const', const=42)
my_parser.add_argument('-c', action='store_true')
my_parser.add_argument('-d', action='store_false')
my_parser.add_argument('-e', action='append')
my_parser.add_argument('-f', action='append_const', const=42)
my_parser.add_argument('-g', action='count')
my_parser.add_argument('-i', action='help')
my_parser.add_argument('-j', action='version')


args = my_parser.parse_args()
print(vars(args))