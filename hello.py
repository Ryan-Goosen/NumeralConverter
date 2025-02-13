# MAIN FUNCTION
from numeralconverter import convert

# SUB FUNCTIONS USED INSIDE OF THE MAIN FUNCTION BUT CAN ALSO be CALLED BY THE USEr
# FOR ROMAN CONVERTIONS
from numeralconverter import from_roman, to_roman

# FOR NUMERAL BASE CONVERTION
from numeralconverter import from_base, to_base

def main():
    print(convert(value='XXX', from_format="roman", to_format="number_base", base=9))

if __name__ == "__main__":
    main()