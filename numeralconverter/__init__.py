'''MODULE CONVERTS DIFFERENT NUMERALS BETWEEN EACH OTHER'''

<<<<<<< HEAD
from .binary_convertion import from_binary, to_binary
=======
>>>>>>> 5604d5f167d995b0a355d62bf3a863447f40a0a9
from .roman_convertion import from_roman, to_roman
from .utils import is_valid_decimal

def convert(value:str, from_format:str, to_format:str) -> str:
    """
    Convert a numeral from one format to another.

<<<<<<< HEAD
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
        "binary":(from_binary, to_binary),
=======
    Args:
        value: The numeral to convert.
        from_format: The current format of the numeral (e.g., "roman", "binary").
        to_format: The target format (e.g., "morse", "binary").

    Returns:
        The converted numeral.
    """
    converters = {
        "roman": (from_roman,   ),
        "decimal": (),
>>>>>>> 5604d5f167d995b0a355d62bf3a863447f40a0a9
    }

    if from_format.lower() not in converters or to_format.lower() not in converters:
        raise ValueError(f"Unsupported format: {from_format} or {to_format}")

    base10_value = is_valid_decimal(value)
    if to_format.lower() == 'decimal':
        return base10_value

    converted_value = converters[to_format][1](base10_value)
    return converted_value
