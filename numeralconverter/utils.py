import sys
sys.tracebacklimit = 0

def is_valid_roman(roman:str) -> None:
    '''CHECKS IF THE INPUTED VALUE IS A VALID ROMA NUMERAL'''
    if not isinstance(roman, str):
        raise TypeError(f'{type(roman)} is not a valid format.')

    roman_chars = ['I','V','X','L','C','D','M']
    valid_chars = all(char in roman_chars for char in roman)

    if not valid_chars:
        raise ValueError(f'Invalid char in string({roman})')


def is_valid_decimal(number) -> None:
    try:
        number = int(number)
        return number
    except:
        pass
