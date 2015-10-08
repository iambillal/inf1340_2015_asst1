#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """


    car = raw_input("Is the car silent when you turn the key?")
    if car == "Y":
        car = raw_input("Are the battery terminals corroded?")
        if car == "Y":
            print "Clean terminals and try starting again."
        elif car == "N":
            print("Replace cables and try again.")
    elif car == "N":
        car = raw_input("Does the car make a clicking noise?")
        if car == "Y":
            print "Replace the battery."
        elif car == "N":
            car = raw_input("Does the car crank up but fail to start?")
            if car == "Y":
                print "Check spark plug connections."
            elif car == "N":
                car = raw_input("Does the engine start then die?")
                if car == "Y":
                    car = raw_input("Does you care have fuel injection?")
                    if car == "N":
                        print "Check to make sure the choke is opening and closing."
                    elif car == "Y":
                        print "Get it in for service."


#diagnose_car()








