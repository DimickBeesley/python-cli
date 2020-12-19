# myls.py

import os # operating system manipulation library 
import sys # gets information like command line arguments
import argparse # makes using the info from os.argv easier through parsing

"""
Sooooo, lets figure this out. (CLIs and Jupyter)


Links I'm learning from:

Jupyter notebook Tips and Tricks:
    https://www.geeksforgeeks.org/jupyter-notebook-tips-and-tricks/#:~:text=Jupyter%20notebook%20provides%20a%20very%20efficient%20way%20to%20achieve%20the%20same.&text=First%2C%20we%20need%20to%20select,highlighted%20portion%20of%20the%20code.

How to Build Command Line Interfaces in Python With argparse:
    https://realpython.com/command-line-interfaces-python-argparse/#:~:text=The%20command%20line%20interface%20(also,currently%20the%20Python%20argparse%20library.

argpars Docs:
    https://docs.python.org/3/library/argparse.html

"""



""" WHAT ARGPARSE IS WHY ITS USEFUL """

''' without argparse '''

# breaks CL input (after the first command) up into an array
if len(sys.argv) < 2:
    print('You need to specify the path to be listed')
    sys.exit() # it exit()s as soon as we're done using it.

# say we input 'python3 learn_cli.py .', then:
#   argv == ['learn_cli.py', '.']
#   argv[1] == '.'
input_path = sys.argv[1]

# checks if input_path is directory
if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

# uses os to go look at the path, prints it's contents
#
# print('\n'.join(os.listdir(input_path))) >>
#
# .git
# README.md
# leaen_cli.py
# .gitignore


''' with arg parse '''

# create parser
my_parser = argparse.ArgumentParser(description='List the contents of a folder') # more descriptive

# add args (not in the docs below TODO func renamed since tutorial or overloaded?)
my_parser.add_args('Path', # <-- TODO what is this? (maybe affects line 71 .Path?)
                    metavar='path', # probably decides procedure base on what kind or param we're looking for?
                    type=str, # has to be data type of param we're taking
                    help='the path to list')
# the docs: https://docs.python.org/3/library/argparse.html


# execute parse_args()
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('the path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path))) # prints the same as the example above
