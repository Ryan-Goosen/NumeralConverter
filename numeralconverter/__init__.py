'''MODULE CONVERTS DIFFERENT NUMERALS BETWEEN EACH OTHER'''

from .numbered_base_convertion import from_base, to_base
from .roman_convertion import from_roman, to_roman
from .utils import is_valid_decimal

def convert(value:str, from_format:str, to_format:str) -> str:
    """
    Convert a numeral from one format to another.

    Parameters
    ----------
    value : str
        The numeral to convert.
    from_format : str
        The current format of the numeral (e.g., "roman", "binary").
    to_format : str
        The target format (e.g., "morse", "binary").

    Returns
    -------
    str
        The converted numeral.

    Notes
    -----
    Currently Functional:
        - 'roman' -> ROMAN NUMERALS
        - 'binary' -> BINARY
    """


    converters = {
        "roman": (from_roman, to_roman),
        "decimal": (),
        "binary":(from_base, to_base),
    }

    if from_format.lower() not in converters or to_format.lower() not in converters:
        raise ValueError(f"Unsupported format: {from_format} or {to_format}")

    base10_value = is_valid_decimal(value)
    if to_format.lower() == 'decimal':
        return base10_value

    converted_value = converters[to_format][1](base10_value)
    return converted_value
