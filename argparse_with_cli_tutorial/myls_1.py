# myls.py

import os # operating system manipulation library 
import sys # gets information like command line arguments
import argparse # makes using the info from os.argv easier through parsing

"""

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

print('\n'.join(os.listdir(input_path)))

# .git
# README.md
# leaen_cli.py
# .gitignore

