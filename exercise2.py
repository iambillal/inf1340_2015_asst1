#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """

    print("Error")


name_that_shape = raw_input("How many sides? ")
name_that_shape = int(name_that_shape)

if (name_that_shape == 3):
    print("triangle")
elif (name_that_shape == 4):
    print("quadrilateral")
elif (name_that_shape == 5):
    print("pentagon")
elif (name_that_shape == 6):
    print("hexagon")
elif (name_that_shape == 7):
    print("heptagon")
elif (name_that_shape == 8):
    print("octagon")
elif (name_that_shape == 9):
    print("nonagon")
elif (name_that_shape == 10):
    print("decagon")
else:
    print("Error")







