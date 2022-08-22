""""
    Euclidean Algorithm written and outlined in python code
    Date:  22nd August, 2022
    Arthur:
"""
def greatest_common_divisor(firstValue, secondValue):
    firstValue = max(firstValue, secondValue)
    secondValue = min(firstValue, secondValue)
    remainder = 0
    while True:
        try:
            remainder = firstValue % secondValue
        except ZeroDivisionError:
            return f'The values of both {firstValue} and {secondValue} ' \
                   f'should not be a non-negative and non-zero integers '
        if remainder == 0:
            result = secondValue
            return result
        firstValue = secondValue
        secondValue = remainder

print(greatest_common_divisor(60, 0))
