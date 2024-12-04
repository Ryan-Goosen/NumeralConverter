'''Contains all the little utility functions that can also be used else where'''

import sys
sys.tracebacklimit = 0

def is_valid_roman(roman:str) -> None:
    '''CHECKS IF THE INPUTED VALUE IS A VALID ROMA NUMERAL'''
    
    if not isinstance(roman, str):
        raise TypeError(f'{type(roman)} is not a valid format.')

    roman = roman.upper()
    roman_chars = ['I','V','X','L','C','D','M']
    valid_chars = all(char in roman_chars for char in roman)

    if not valid_chars:
        raise ValueError(f'Invalid char in string({roman})')

def value_is_valid_size(number, maximum=3999, minimum=0) -> None:
    '''Checks if the value is not too large'''
    if not minimum < number < maximum:
        raise ValueError('Max allowed value is 3999')

def is_valid_decimal(number) -> int:
    '''Checks if the inputed value is an interger'''
    try:
        number = int(number)
        return number
    except TypeError as e:
        raise TypeError from e
