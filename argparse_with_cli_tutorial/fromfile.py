# myls.py

import os 
import sys 
import argparse 

"""
Now we'll be playing with some of the more complex argparse funcionality:
"""



# we can set the name of the program as we want it to run from the command line
# read this:

my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                    prog='adv1',
                                    description='learning about arguments')



# now if we want to run this program from the command line we'll need to input:
# python3 myls, not python3 myls.py, or python3 {prog}

my_parser.add_argument('a',
                        help='a first argument')

my_parser.add_argument('b',
                        help='a second argument')

my_parser.add_argument('c',
                        help='a third argument')

my_parser.add_argument('d',
                        help='a fourth argument')

my_parser.add_argument('e',
                        help='a fifth argument')

my_parser.add_argument('-v',
                        action='store_true',
                        help='an optional argument')



args = my_parser.parse_args()

print('if you read this line it means that you provided '
      'all the parameters')