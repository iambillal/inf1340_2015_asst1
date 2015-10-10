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

    Inputs: string from user as either Y or N

    Expected outputs: A string providing advice on how to proceed or an additional question requiring another Y/N input
    from the user in order to further diagnosis the car problem.

    Errors: none, user will only input Y or N.

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
                if car == "N":
                    print"Engine is not getting enough fuel. Clean fuel pump."
                elif car == "Y":
                    car = raw_input("Does you care have fuel injection?")
                    if car == "N":
                        print "Check to ensure the choke is opening and closing."
                    elif car == "Y":
                        print "Get it in for service."


#diagnose_car()

"""

Test cases:

Is the car silent when you turn the key?Y
Are the battery terminals corroded?Y
Clean terminals and try starting again.

Is the car silent when you turn the key?Y
Are the battery terminals corroded?N
Replace cables and try again.

Is the car silent when you turn the key?N
Does the car make a clicking noise?Y
Replace the battery.

Is the car silent when you turn the key?N
Does the car make a clicking noise?N
Does the car crank up but fail to start?Y
Check spark plug connections.

Is the car silent when you turn the key?N
Does the car make a clicking noise?N
Does the car crank up but fail to start?N
Does the engine start then die?Y
Does you care have fuel injection?Y
Get it in for service.

Is the car silent when you turn the key?N
Does the car make a clicking noise?N
Does the car crank up but fail to start?N
Does the engine start then die?Y
Does you care have fuel injection?N
Check to ensure the choke is opening and closing.

Is the car silent when you turn the key?N
Does the car make a clicking noise?N
Does the car crank up but fail to start?N
Does the engine start then die?N
Engine is not getting enough fuel. Clean fuel pump.

"""





