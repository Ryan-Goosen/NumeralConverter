'''CONVERTS A VALUE FROM AND TO BINARY OR DECIMAL'''

from .utils import is_valid_numeral, is_valid_size, is_valid_decimal

BINARIES = {
    '1' : 1, '0' : 0
}
def from_binary(numeral:str) -> int:
    """
    Convert a numeral from binary to decimal.

    Args:
        numeral: The numeral to convert.
    Returns:
        The converted numeral as an integer.
    """
    is_valid_numeral(numeral, BINARIES)
    num = 0
    for pos, value in enumerate(numeral[::-1]):
        num += int(value) * (2 ** pos)

    return num


def to_binary(number:int) -> str:
    """
    Convert a number from binary to deciaml.

    Args:
        number: The decimal number you want to convert.
    Returns:
        The converted number as a numeral.
    """
    number = is_valid_decimal(number)
    is_valid_size(number, minimum=0, maximum=2**1000)
    if number == 0:
        return '0'
    divisor = -1
    num = 0
    binary_sequence = ''
    while num < number:
        divisor += 1
        num = 2 ** divisor
    
    while divisor >= 0:
        num_a = 2 ** divisor
        if num_a <= number:
            number -= num_a
            binary_sequence += '1'
        else:
            if binary_sequence != '':
                binary_sequence += '0'

        divisor -= 1

    return binary_sequence
