# Numeral Converter

## Description

Numeral Converter is a Python library designed to simplify conversions between various numeral systems. It also allows users to target a specific numeral system for a precise conversion.

## Installation

### From PyPI (NOT OPERATIONAL YET)

```bash
pip install numeral-converter
```

### From Source

```bash
git clone https://github.com/Ryan-Goosen/NumeralConverter.git
cd NumeralConverter
pip install .
```

## Usage

### Here are examples of how to use Numeral Converter:

### 1. Convert from One Numeral to Another
```python 
from numeralconverter import convert

result = convert(value='XIV', from_format='roman', to_format='morse')
print(result) 
<----------->
OUTPUT: .---- ....-
```

### Direct Conversions

If you only need to convert to or from a specific numeral system, you can use the specialized functions

#### Convert to Roman Numerals
```python
from numeralconverter import to_roman

result = to_roman(14)
print(result) # OUTPUT: XIV
```

#### Convert from Roman Numerals
```python
from numeralconverter import from_roman

result = from_roman('XIV')
print(result) # 
<------------>
OUTPUT: 14
```

## Features

- **Ease of Use**: Easily convert between various numerals and number bases using a single function `convert`.
- **Specialized Conversion Functions**: Use dedicated functions like `to_roman` to convert a decimal number to Roman numerals, or `from_base` to convert from a specific base to decimal. All conversions go through decimal for consistent results.
- **Supports Multiple Numeral Systems**: Includes support for Roman numerals, Morse code, and common number bases like binary, decimal, and hexadecimal.
- **Flexible Conversions**: Convert between any two supported numeral systems with ease, using either general or specific conversion methods.
- **Extensible Design**: Easily add new numeral systems or base conversions to the library.

## Supported Numerals and Number Systems

- Roman Numerals (e.g., 'XIV', 'IX')
- Number Bases (accepted bases are '2' to '94')

## How It Works
Each convertion has its own file with two main function, one to convert to that numeral and one to convert from that numeral to decimal. In the init file we created the conversion function which takes 3 inputs: value, from_format, to_format. Also to note is that we saved each functions for each language in a dictionary that can be called by using the from and to format. So what happens is that the from_format gets converted to decimal and then from decimal is gets converted to the to_format. It was decided to do this instead of other option because it would be easier to 

Each convertion module has two functions that can be called one to convert from that numeral to decimal and one to convert from decimal to that numeral. This functionality was chosen because each and every numeral can be converted with ease to decimal making future expansion of the library easy. The init file contains the main convertion function which calls the convertion function from every other module to make an easy convertion process. 

Example (converting a number from to decimal to base 64): 
```python
from numeralconverter import to_base

number = to_base(number:1000, base=64)
print(number)
<-------------->
OUTPUT: fE 
```

Example (converting a number from roman to base 9): 
```python
from numeralconverter import convert

number = convert(value='XXX', from_format="roman", to_format="number_base", base=9)
print(number)
<-------------->
OUTPUT: 33
```

## Contributing
As this is a personal portfolio project, contributions are not currently being accepted. However, feel free to explore the code and suggest improvements via GitHub issues or create your own fork!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Contributers
- Ryan Goosen (Creator)
