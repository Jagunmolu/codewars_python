# This is my third codewars challenge, and this was a bit challenging as it is a 7 kata challenge.
# Right now, I am glad I took this path.
# Date: ca January 2022
# Refined Solution Date: April 25, 2022
# Solution ID: 3
"""
The function below takes in an argument: a string which is in number format,
and it is meant to return an integer.

DESCRIPTION
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.
Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    lists = list()
    num = str(num)
    for i in num:
        i = int(i)
        a = i ** 2
        a = str(a)
        lists.append(a)
    strings = ""
    for b in lists:
        strings += b
        strings.replace(" ", "")
        integer = int(strings)
    return (integer)


# Trust me, I would do this differently right now:

def square_digits_updated(num):
    result = ''
    for i in str(num):
        result += str(int(i) ** 2)
    return int(result)
