'''CONVERTS A VALUE FROM AND TO BINARY OR DECIMAL'''

from .utils import is_valid_numeral, is_valid_size, is_valid_decimal, largest_exponent



def from_base(numeral:str, base:int) -> int:
    """
    Convert a numeral from binary to decimal.

    Args:
        numeral: The numeral to convert.
        base: The base of the numeral (Can't be larger than 9)
    Returns:
        The converted numeral as an integer.
    """
    is_valid_decimal(base)
    BINARIES = {
        str(i):i for i in range(abs(base)) 
    }
    is_valid_numeral(numeral, BINARIES)
    
    numeral_value = 0
    exponent = len(numeral) - 1
    for value in numeral:
        numeral_value += int(value) * base ** exponent
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
    is_valid_size(number, minimum=0, maximum=2**1000)
    if number == 0:
        return '0'
    
    numeral_sequence = ''\

    while number != 0:
        numeral, number = divmod(number, base)
        numeral_sequence += str(numeral)

    return numeral_sequence
