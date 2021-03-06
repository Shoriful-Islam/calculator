#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import calculator

# parse arguments

parser = argparse.ArgumentParser(description='Simple calculator.')

parser.add_argument('-s', required=True, action='store', dest='s', 
                    help='an input string of numbers and operands separated by spaces')

args = parser.parse_args()

c = calculator.simple.SimpleCalculator()

if __name__ == "__main__":
    c.run(args.s)
    print "TAPE:"
    for i in c.log:
        print str(i)

    print "LCD:\n%s" % c.lcd
