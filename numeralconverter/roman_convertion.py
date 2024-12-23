'''CONVERTS A VALUE FROM AND TO ROMAN NUMERALS OR DECIMAL '''
<<<<<<< HEAD
from .utils import is_valid_size, is_valid_decimal, is_valid_numeral, roman_order_correct

NUMERALS = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',}
=======
from .utils import is_valid_roman, is_valid_decimal, value_is_valid_size

NUMERALS = {
    1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
}
>>>>>>> 5604d5f167d995b0a355d62bf3a863447f40a0a9
REVERSE_NUMERALS = {v: k for k, v in NUMERALS.items()}
SORTED_NUMERALS = sorted(NUMERALS, reverse=True)

def __partion_number__(number):
    partitioned_number = []
    number = str(number)
    for pos , val in enumerate(number):
        if val != '0':
            partitioned_number.append(int(f'{val}{'0'*(len(number) - pos -1)}'))
    return partitioned_number

def from_roman(numeral:str) -> int:
    """
    Convert a numeral from roman to decimal.

    Args:
        numeral: The numeral to convert.
    Returns:
        The converted numeral as an integer.
    """
<<<<<<< HEAD

    is_valid_numeral(numeral, NUMERALS.values())
    roman_order_correct(numeral, REVERSE_NUMERALS)
=======
    
    is_valid_roman(numeral)
>>>>>>> 5604d5f167d995b0a355d62bf3a863447f40a0a9
    number = 0
    previous = 0
    for num in numeral:
        new_num = REVERSE_NUMERALS[num]
        if new_num > previous and previous != 0:
            number += (new_num-previous) - previous
        else:
            number += new_num
        previous = new_num

    return number

<<<<<<< HEAD


=======
>>>>>>> 5604d5f167d995b0a355d62bf3a863447f40a0a9
def to_roman(number:int) -> str:
    """
    Convert a number from decimal to roman numeral.

    Args:
        number: The decimal number you want to convert.
    Returns:
<<<<<<< HEAD
        The converted number as a numeral.
    """
    number = is_valid_decimal(number)
    is_valid_size(number, maximum=3999, minimum=1)
=======
        The converted numeral.
    """
    number = is_valid_decimal(number)
    value_is_valid_size(number)
>>>>>>> 5604d5f167d995b0a355d62bf3a863447f40a0a9

    partioned_number = __partion_number__(number)
    converted = []

    for num in partioned_number:
        viable_nums = [x for x in SORTED_NUMERALS if x <= num]
        times, remainder = divmod(num, viable_nums[0])
        if remainder == 0 and times <= 3:
            converted.append(NUMERALS[viable_nums[0]] * times)
            continue

        non_viable_nums = [x for x in SORTED_NUMERALS if x >= num]
        new_viable_nums = [x for x in SORTED_NUMERALS if x <= num and x * 10 >= non_viable_nums[-1] and x * 2 != non_viable_nums[-1]]
        if non_viable_nums[-1] - new_viable_nums[0] == num:
            converted.append(f'{NUMERALS[new_viable_nums[0]]}{NUMERALS[non_viable_nums[-1]]}')
            continue

        new_times, new_remainder = divmod(remainder, viable_nums[1])
        if new_remainder == 0:
            converted.append(f'{NUMERALS[viable_nums[0]]*times}{NUMERALS[viable_nums[1]]*new_times}')
            continue

    return ''.join(converted)
