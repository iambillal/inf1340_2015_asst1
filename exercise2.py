def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name
    Inputs: user input 3-10
    Expected Outputs: triangle, quadrilateral, pentagon, hexagon, heptagon, octagon, nonagon, decagon.
    Errors: 0,1,2, any number greater than 10 and any other string
    """




    name_that_shape = raw_input("How many sides? ")



    if (name_that_shape == "3"):
        print("triangle")
    elif (name_that_shape == "4"):
        print("quadrilateral")
    elif (name_that_shape == "5"):
        print("pentagon")
    elif (name_that_shape == "6"):
        print("hexagon")
    elif (name_that_shape == "7"):
        print("heptagon")
    elif (name_that_shape == "8"):
        print("octagon")
    elif (name_that_shape == "9"):
        print("nonagon")
    elif (name_that_shape == "10"):
        print("decagon")
    else:
        print("Error")

#name_that_shape()

"""
Test cases:

How many sides? 3
triangle

How many sides? 4
quadrilateral

How many sides? 5
pentagon

How many sides? 6
hexagon

How many sides? 7
heptagon

How many sides? 8
octagon

How many sides? 9
nonagon

How many sides? 10
decagon

How many sides? 2
Error

How many sides? 11
Error
"""
