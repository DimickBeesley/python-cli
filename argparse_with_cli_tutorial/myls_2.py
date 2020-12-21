# myls.py

import os # operating system manipulation library 
import sys # gets information like command line arguments
import argparse # makes using the info from os.argv easier through parsing


"""

Second example at How to Build Command Line Interfaces in Python With argparse:
    https://realpython.com/command-line-interfaces-python-argparse/#:~:text=The%20command%20line%20interface%20(also,currently%20the%20Python%20argparse%20library.

"""


# create parser
my_parser = argparse.ArgumentParser(description='List the contents of a folder') # more descriptive

# add args (not in the docs below TODO func renamed since tutorial or overloaded?)
my_parser.add_argument('Path', # <-- TODO what is this? (maybe affects line 71 .Path?)
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

"""
from the tutorial:

The code has changed a lot with the introduction of the Python argparse library.

The first big difference compared to the previous version is that the if statements
to check the arguments provided by the user are gone because the library will check
the presence of the arguments for us.

We’ve imported the Python argparse library, created a simple parser with a brief 
description of the program’s goal, and defined the positional argument we want to get
from the user. Lastly, we have executed .parse_args() to parse the input arguments and
get a Namespace object that contains the user input.

Now, if you run this code, you’ll see that with just four lines of code. You have a very
different output:
"""

# so now the program recognizes that it needs at least one positional argument and takes 
# an -h tag.
