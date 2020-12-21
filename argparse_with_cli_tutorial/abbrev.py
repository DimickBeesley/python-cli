import argparse

'''
the program prints an int input after the --input option from the command line
'''

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', type=int, required=True) # the reason this is here is because - and -- signify 'optionals' and you can make them not optional
# if an argument does not have a - or -- in front of it, it is not non-optional (positional)
my_parser.add_argument('--id', action='store', type=int)

# i did this to see if abbrev conflics happen when we say, input --in 32. THEY DO 
my_parser.add_argument('--inc', action='store', type=float,)

""" This field shuts down abbrev altogether """
# my_parser.allow_abbrev = False

args = my_parser.parse_args()

print(args.input)

'''
Summation:
argparse.ArgumentParser(abbrev) controls whether you can abbreviate your 
optional arguments when running programs from the command line.

if you have another optional arg with same starting chars (like --input and --inc)
they conflict until you are specific enough to rule one outs
'''