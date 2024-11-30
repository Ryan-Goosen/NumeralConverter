'''MODULE CONVERTS DIFFERENT NUMERALS BETWEEN EACH OTHER'''

from .roman_convertion import roman_convert_from, roman_convert_to
from .utils import is_valid_decimal

def convert(value, from_format, to_format):
    """
    Convert a numeral from one format to another.

    Args:
        value: The numeral to convert.
        from_format: The current format of the numeral (e.g., "roman", "binary").
        to_format: The target format (e.g., "morse", "binary").

    Returns:
        The converted numeral.
    """
    converters = {
        "roman": (roman_convert_from, roman_convert_to),
        "decimal": (),
    }

    if from_format.lower() not in converters or to_format.lower() not in converters:
        raise ValueError(f"Unsupported format: {from_format} or {to_format}")

    base10_value = is_valid_decimal(value)
    if to_format.lower() == 'decimal':
        return base10_value

    converted_value = converters[to_format][1](base10_value)
    return converted_value
