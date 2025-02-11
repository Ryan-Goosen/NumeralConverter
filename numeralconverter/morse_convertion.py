class MorseCode:
    '''DOC STRING'''

    def __init__(self, number):
        self.symbols = {
            0: '-----',
            1: '.----',
            2: '..---',
            3: '...--',
            4: '....-',
            5: '.....',
            6: '-....',
            7: '--...',
            8: '---..',
            9: '----.',
        }

        self.number = number


    def class_convert_from(self):
        print(self.symbols[self.number])


def morse_convert_from():
    pass

def morse_convert_to():
    pass