# Numeral Converter

> A Python library for converting numbers between any format.

---

## About

### What it does
A quick way to convert numbers between any format, for example binary to Morse code, Roman numerals to decimal, and more.

### Why I built it
I made this as a showcase project to demonstrate my programming skills and understanding of different numeral systems.

### Who it's for
Developers and learners who need quick numeral system conversions, or anyone reviewing my portfolio of work.

---

## Built With

| Category | Tool |
| -------- | ---- |
| **Language** | Python |
| **Framework** | None (Library) |
| **Libraries** | None (stdlib only) |

---

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

1. Clone the repo:
```bash
git clone https://codeberg.org/Ryan-Goosen/numeralConverter.git
```

2. Navigate into the project:
```bash
cd numeralConverter
```

3. Install locally:
```bash
pip install .
```

---

## Usage

Import individual converter classes:

```python
from numeralconverter import BinaryConvert

# Convert binary to decimal
number = BinaryConvert.convert_to_decimal('1001010')
print(number)  # Output: 74
```

---

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

---

## Acknowledgments

- Ryan Goosen (Creator)
