def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name
    Inputs:
    Expected Outputs:
    Errors:
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