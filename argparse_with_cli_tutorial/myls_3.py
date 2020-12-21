import os # operating system manipulation library 
import sys # gets information like command line arguments
import argparse # makes using the info from os.argv easier through parsing



my_parser = argparse.ArgumentParser(description='List the contents of a folder')

my_parser.add_argument('Path', 
                    metavar='path',
                    type=str,
                    help='the path to list')

''' this arg below is added to old code'''
my_parser.add_argument('-l', 
                       '--long',
                        action='store_true',
                        help='enable the long listing format')
# the docs: https://docs.python.org/3/library/argparse.html


args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('the path specified does not exist')
    sys.exit()

''' this is added to old code '''
for line in os.listdir(input_path):
    if args.long: # Simplified long listing
        size = os.stat(os.path.join(input_path, line)).st_size
        line = '%10d %s' % (size, line)
    print(line)
