# Numeral Converter

---

## Project Identity

| Field | Value |
| ----- | ----- |
| **Name** | Numeral Converter |
| **Project ID** | NC-2024-015 |
| **Owner** | Ryan Goosen |
| **Date Created** | 2024-01-01 |
| **Last Updated** | 2026-05-02 |

---

## Vision & Purpose

**Elevator Pitch:**
A Python library for converting numbers between any format - binary, Roman numerals, Morse code, and more.

**Long-Term Vision:**
A comprehensive numeral conversion library that can handle any base system. Showcase project demonstrating understanding of numeral systems.

**Success Metrics:**
- [x] Binary conversion working
- [x] Roman numeral conversion working
- [x] General base converter (any base to any base)
- [ ] Comprehensive test coverage

---

## Tech Stack

| Category | Tools / Languages |
| -------- | ----------------- |
| **Core Language** | Python |
| **Framework** | None (Library) |
| **Libraries** | None (stdlib only) |
| **Tools** | VS Codium |
| **Version Control** | [Codeberg](https://codeberg.org/Ryan-Goosen/numeralConverter) |

---

## Current State

**Phase:** Needs Testing
**Progress:** 85%

**Recent Wins:**
- [x] Binary conversion class implemented
- [x] Roman numeral conversion class implemented
- [x] Validation functions for inputs
- [x] Package structure for pip installation

**Blockers:**
- [ ] Need comprehensive test suite
- [ ] General base converter not yet implemented

---

## Roadmap

### Main Objectives

1. **Core Conversions** *(Complete)*
   - [x] Binary to decimal and back
   - [x] Roman numerals to decimal and back
   - [x] Input validation

2. **Testing Phase** *(Current)*
   - [ ] Unit tests for all converters
   - [ ] Edge case testing
   - [ ] Integration tests

3. **Future Enhancements** *(Backlog)*
   - [ ] General base converter (any base to any base)
   - [ ] Morse code support
   - [ ] Hexadecimal support
   - [ ] Publish as a library

### Immediate Next Steps
1. Write unit tests for BinaryConvert
2. Write unit tests for RomanConvert
3. Test edge cases and validation

---

## Project Structure

```
/numeralConverter
├── numeralconverter/    # Main package
│   ├── __init__.py
│   ├── binary_convertion.py
│   └── roman_convertion.py
├── setup.py             # Package setup
└── LICENSE.txt
```

---

## Notes & Decisions

**Key Choices:**
- Each numeral type has its own class for modularity
- All conversions go through decimal as intermediate step
- Validation functions built into each converter class

**Backlog / Ideas:**
- Add Morse code converter
- Support for hexadecimal
- Command-line interface
- Web API version

**Debug Log:**

---

## Visuals

[Attach or link to mockups, screenshots, or diagrams]
