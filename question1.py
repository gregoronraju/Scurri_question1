"""
# File          : question1.py
# Created       : 07/09/22 6:37 pm
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""


def print_multiples():
    """prints the numbers from 1 to 100. But for multiples of three print “Three”
    instead of the number and for the multiples of five print “Five”. F
    or numbers which are multiples of both three and five print “ThreeFive” """
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0 and i % 5 != 0:
            print("Three")
        elif i % 3 != 0 and i % 5 == 0:
            print("Five")
        else:
            print(i)
