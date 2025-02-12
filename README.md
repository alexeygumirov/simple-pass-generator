# Simple Passphrase and Pass String Generator

[Github repository](https://github.com/alexeygumirov/simple-pass-generator/)

## Overview

A Python-based command-line tool for generating secure and customizable passwords or passphrases.

## Features

- Two password generation modes:
  1. Passphrase Mode: `simple-pass-generator.py phrase`
     - Generate passphrases using a dictionary of words
        - `dict.txt` file required in the same directory with the script.
     - Customize number of words
     - Optional capitalization of words
     - Optional addition of special symbols

  2. Random String Mode: `simple-pass-generator.py string`
     - Generate random strings with configurable block length and number of blocks
     - String consits only of lowercase letters and delimiters

## Requirements

- Python 3.x
- `dict.txt` file in the same directory (word dictionary for passphrase generation)

## Installation

1. Clone the repository
2. Ensure you have the required `dict.txt` file in the same directory as the script.
3. Make `simple-pass-generator.py` executable or just run `python3 simple-pass-generator.py` in the terminal.

## Usage

### Passphrase Generation

```bash
usage: simple-pass-generator.py phrase [-h] [-w WORDS] [-c CAPITALIZE]
                                       [-s SPECIAL]

options:
  -h, --help            show this help message and exit
  -w, --words WORDS     The number of words to generate the passphrase.
                        (default: 5)
  -c, --capitalize CAPITALIZE
                        The number of words to capitalize.
                        (default: 0)
  -s, --special SPECIAL
                        The number of words to add special symbols.
                        (default: 0)
```

With default parameters:

```bash
$ python simple-pass-generator.py phrase
sickliness-telos-jasey-macrotone-lolly
```

Pass phrase from 3 words, non-capitalized and 2 special symbols:

```bash
$ python simple-pass-generator.py phrase -w 3 -c 0 -s 2
answerer!-enneahedrons$-murumuru
```

Pass phrase from 5 words, 3 capitalized and 4 special symbols:
```bash
$ python simple-pass-generator.py phrase -w 5 -c 3 -s 4
sparklingly-Campaigner#-Nonperverse*-Abhorrers@-artisanship@
```

### Random String Generation

```bash
usage: simple-pass-generator.py string [-h] [-b BLOCKS] [-l LENGTH]
                                       [-d DELIMITER]

options:
  -h, --help            show this help message and exit
  -b, --blocks BLOCKS   Nuimber of string blocks.
                        (default: 5)
  -l, --length LENGTH   Length of the single string block.
                        (default: 5)
  -d, --delimiter DELIMITER
                        String block delimiter.
                        (default: '-')
```

With default parameters:

```bash
$ python3 simple-pass-generator.py string
mfnye-rsbmq-ixzdg-zewcs-ipyfy
```

String with 3 blocks, 4 characters each and `#` delimiter:

```bash
$ python3 simple-pass-generator.py string -b 3 -l 4 -d "#"
pjwb#wopa#ydpd
```

## License

MIT License

Copyright (c) 2025 Alexey Gumirov
