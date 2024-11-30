# Project Name

## Features

## Installation

## Usage

## Supported Systems

## How It Works
Each numeral has its own class in its own .py file, the class contains all the logic neccesary to convert the base to decimal and from decimal to the base. 

Each class consists of two public classes example BinaryConvert has `convert_to_decimal` & `convert_to_binary`. Each convert has its own validation function that checks the input its about to receive is a valid input. 

When the user imports numeralconverter it include these files which allows you to use each convert individualy. For example lets say we only want to convert between binary and decimal. All we need to do is import the binary convert class from numeral converter and we can use it by itself.

Example:
```python
from numeralconverter import BinaryConvert

number = BinaryConvert.convert_to_decimal('1001010')
print(number)
<-------------->
OUTPUT: 84 
```


## Future Plans
- General Base converter (be able to convert between any numbered base)

## C`ontributers
- Ryan Goosen (Creator)
 
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.


<!-- ## Acknowledgments -->
