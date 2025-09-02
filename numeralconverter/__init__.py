'''MODULE CONVERTS DIFFERENT NUMERALS BETWEEN EACH OTHER'''

from .numbered_base_convertion import from_base, to_base
from .roman_convertion import from_roman, to_roman
from .utils import is_valid_decimal


def convert(value:str, from_format:str, to_format:str, *base) -> str:
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
    base:
        This is for when you want to convert a value to a certian base. (DEFAULT = 2)

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
        "number_base":(from_base, to_base),
    }

    if from_format.lower() not in converters or to_format.lower() not in converters:
        raise ValueError(f"Unsupported format: {from_format} or {to_format}")


    needs_base = "number_base" in (from_format, to_format) and (from_format in converters and to_format in converters)

    if (needs_base and base is None):
        raise ValueError(f"Base must be provided for converting between {from_format} and {to_format}")

    from_needs_base = from_format == "number_base"
    to_needs_base = to_format == "number_base"
    

    if to_format.lower() == 'decimal':
        converted_value = converters[from_format][0](value, base) if needs_base and base else converters[from_format][0](value)
    else:
        new_value = (
            converters[from_format][0](value, base) 
            if from_needs_base and base else 
            converters[from_format][0](value)
        )

        converted_value = (
            converters[to_format][1](new_value, base) 
            if to_needs_base and base else 
            converters[to_format][1](new_value)
        )

    return converted_value
