'''Contains all the little utility functions that can also be used else where'''

import sys, math, string
sys.tracebacklimit = 0



# ==========================
# GENERALLY USEFUL FUNCTIONS
# ==========================
def is_valid_size(number, minimum, maximum) -> None:
    """
    Checks if the value is not too large
    If a number doesn't fit the size criteria an error is raised

    Args:
        number: The number that is being tested.
        maximum: The largest value the number can be.
        minimum: The smallest value the number can be.
    Returns:
        None.
    """
    if int(number) > int(maximum):
        raise ValueError(f'Max allowed value is {maximum}')

    if int(number) < int(minimum):
        raise ValueError(f'Minimum allowed value is {minimum}')

def is_valid_decimal(number:str) -> int:
    """
    Checks if the inputed value is an interger
    If a number is not an integer an error is raised

    Args:
        number: The number that is being tested.
    Returns:
        number converted into an integer
    """
    if len(str(number)) < 1:
        raise ValueError("Empty string can't be converted.")

    if isinstance(number, bool):
        raise Exception('Unexpected error') from e 


    try:
        if "." in str(number):
            raise ValueError(f"Only whole numbers are accepted: {number}")
        if "-" in str(number):
            raise ValueError(f"Only whole numbers are accepted: {number}")
        number = int(number)
        return number
    except ValueError as e:
        raise ValueError(f"Only whole numbers are accepted: {number}") from e

    except Exception as e:
        raise Exception('Unexpected error') from e 

def is_valid_numeral(numeral:str, numeral_chars:list) -> None:
    """
    Checks if the inputed value is only contain valid numeral characters
    If a number is not an integer an error is raised

    Args:
        numeral: The numeral being tested.
        numeral_chars: A list of all the valid numerals.
    Returns:
        None.
    """
    if not isinstance(numeral, str):
        raise TypeError(f'{type(numeral)} is not a valid format.')

    if len(numeral) < 1:
        raise ValueError("Empty string can't be converted.")

    # numeral_chars = list(numeral_chars)
    valid_chars = all(char in numeral_chars for char in numeral)

    if not valid_chars:
        raise ValueError(f'Invalid char/s in string({numeral})')

# ==========================
# ROMAN CONVERSIONS
# ==========================
def roman_order_correct(roman:str, roman_numerals) -> bool:
    '''Checks the order of the given roman numeral'''
    previous_value = 0
    continues_counter = 0
    num = 0
    for char in roman:
        if previous_value == 0:
            previous_value = char
            num += roman_numerals[char]
            continue

        if previous_value == char:
            continues_counter += 1
            if continues_counter > 2:
                raise ValueError(f"Invalid formatting for Roman numeral: {roman}")
        else:
            continues_counter = 0

        if char.upper() in ['V','L','D'] and previous_value in ['V','L','D']:
            raise ValueError(f"Invalid formatting for Roman numeral: {roman}")

        if roman_numerals[char] > roman_numerals[previous_value]:
            num = roman_numerals[char] - num
            if previous_value in ['V','L','D'] :
                raise ValueError(f"Invalid formatting for Roman numeral: {roman}")
            if roman_numerals[char] // roman_numerals[previous_value] > 10:
                raise ValueError(f"Invalid formatting for Roman numeral: {roman}")
        else:
            num += roman_numerals[char] 

        previous_value = char
    if num in roman_numerals.values() and len(roman) > 1:
        raise ValueError(f"Invalid formatting for Roman numeral: {roman}")

    return True

# ==========================
# BASE CONVERSIONS
# ==========================
def largest_exponent(number, root):
    if number <= 1 and -1 < abs(root) < 1:
        raise ValueError("Base (x) must be > 1 and target (y) must be >= 1")
    return math.floor(math.log(number, abs(root)))

def correct_binaries(base):
    if 2 <= base <= 10:
        return string.digits[:base]
    elif 11 <= base <= 16:
        return (string.digits + string.ascii_uppercase)[:base]
    elif 17 <= base <= 26:
        return string.ascii_uppercase[:base]
    elif 27 <= base <= 36:
        return (string.digits + string.ascii_uppercase)[:base]
    elif 37 <= base <= 62:
        return (string.digits + string.ascii_letters)[:base]
    elif 63 <= base <= 94:
        return (string.digits + string.ascii_letters + string.punctuation)[:base]
    