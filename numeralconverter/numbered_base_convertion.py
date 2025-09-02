'''CONVERTS A VALUE FROM AND TO BINARY OR DECIMAL'''

from .utils import is_valid_numeral, is_valid_size, is_valid_decimal, largest_exponent, correct_binaries

def from_base(numeral:str, base:int) -> int:
    """
    Convert a numeral from binary to decimal.

    Args:
        numeral: The numeral to convert.
        base: The base of the numeral.
    Returns:
        The converted numeral as an integer.
    """
    is_valid_decimal(base)
    is_valid_size(base, minimum=2, maximum=94)
    BINARIES = {value: index for index, value in enumerate(correct_binaries(base))}
    is_valid_numeral(numeral, BINARIES)
    
    numeral_value = 0
    exponent = len(numeral) - 1
    for value in numeral:
        numeral_value += BINARIES[value] * base ** exponent
        exponent -= 1

    return numeral_value


def to_base(number:int, base:int) -> str:
    """
    Convert a number from binary to deciaml.

    Args:
        number: The decimal number you want to convert.
        base: The base you want to use to convert the number,
    Returns:
        The converted number as a numeral.
    """
    is_valid_decimal(base)
    number = is_valid_decimal(number)
    is_valid_size(base, minimum=2, maximum=94)
    is_valid_size(number, minimum=0, maximum=2**64)
    
    numeral_sequence = ''
    variables = correct_binaries(base)

    if (17 <= base <= 26) and (number == 0):
        return 'A'
    
    if number == 0:
        return '0'

    while number > 0:
        number, remainder = divmod(number, base)
        numeral_sequence += str(variables[remainder])

    return numeral_sequence[::-1]
