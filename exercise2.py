#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import math

#upc = 03600029145x where x = 2

def upc (0, 3, 6, 0, 0, 0, 2, 9, 1, 4, 5, 2):

#prints 12th digit: print(10 - (((sum(upc[::2])*3) + sum(upc[1::2])) % 10))
#not sure if I need the for loop, but definitely need the (sum(upc[::2]))
#for num in upc:
#     #num = (sum(upc[::2]))

def checksum(upc):
    #use a string to represent the object

    upc = str(0:11)

    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string
if upc != str():
    raise TypeError("Invalid Input")

    # check length of string
    # raise ValueError if not 12
if len(upc) != 12:
    raise ValueError("Incorrect Length")

    # convert string to array
    # hint: use the list function
upc = '0, 3, 6, 0, 0, 0, 2, 9, 1, 4, 5, 2'
upc = upc.split(',')
upc
[0, 3, 6, 0, 0, 0, 2, 9, 1, 4, 5, 2]

    # generate checksum using the first 11 digits provided
    # check against the the twelfth digit
        #1 Add odd number digits then multiplying by 3
        #2 Add step 1 result + total of even number digits
        #3 calculate step 2 result modulo 10
        #4 Subtract step 3 result from 10
(10 - (((sum(upc[::2])*3) + sum(upc[1::2])) % 10))


    # return True if they are equal, False otherwise
#checks if upc 12th number equals the checksum result
if checksum = upc[11]
    return True





    return False

