# This isn't really a bad solution. I might just make it simpler now, though.
# Right now, I am glad I took this path.
# Date: ca February 2022
# Refined Solution Date: April 25, 2022.
# Solution ID: 5
"""
DESCRIPTION
Your task is to create a function that does four basic mathematical operations.
The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
"""


def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    else:
        return value1 / value2


# Anything good can be better:

def basic_op_updated(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))
