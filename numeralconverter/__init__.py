'''MODULE CONVERTS DIFFERENT NUMERALS BETWEEN EACH OTHER'''

from .numbered_base_convertion import from_base, to_base
from .roman_convertion import from_roman, to_roman
from .utils import is_valid_decimal

"""
The way this function is suppose to work is that a user adds a from and to base and we convert the number from to to. These bases can be almost anything so we should account for that.
TODO: 
- Fix the convertion process
    - Allow the convertion process to be less static and work with more options.
"""

def convert(value:str, from_format:str, to_format:str) -> str:
    """
    Convert a numeral from one format to another.

    Parameters
    ----------
    value : str
        The numeral to convert.
    from_format : str
        The current format of the numeral (e.g., "roman", "number_base").
    to_format : str
        The target format (e.g., "morse", "number_base").

    Returns
    -------
    str
        The converted numeral.

    Notes
    -----
    Currently Functional:
        - 'roman' -> ROMAN NUMERALS
        - 'number_base' -> CONVERTS NUMBER TO SELECTED BASE
    """


    converters = {
        "roman": (from_roman, to_roman),
        "decimal": (),
        "number_base":(from_base, to_base),
    }

    if from_format.lower() not in converters or to_format.lower() not in converters:
        raise ValueError(f"Unsupported format: {from_format} or {to_format}")

    base10_value = is_valid_decimal(value)
    if to_format.lower() == 'decimal':
        return base10_value

    converted_value = converters[to_format][1](base10_value)
    return converted_value
