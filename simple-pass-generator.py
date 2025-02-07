#!/usr/bin/python3

"""
MIT License

Copyright (c) 2025 Alexey Gumirov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import string

from itertools import permutations
from pathlib import Path
from random import choice


def get_random_string(length: int, delimiter: str = "-", split_step: int = 4) -> str:
    """
    Generates a random string of a specified length.

    Args:
        length (int): The length of the random string.
        delimiter (str): The delimiter to separate the string.
        split_step (int): The number of characters in each split.

    Returns:
        str: The random string.
    """
    if length == 0:
        return ""
    letters = string.ascii_lowercase
    result_str = "".join(choice(letters) for _ in range(length))
    if split_step == 0:
        return result_str
    result_str = delimiter.join(
        [result_str[i : i + split_step] for i in range(0, len(result_str), split_step)]
    )
    return result_str


def capitalize_first_letter(word: str) -> str:
    """
    Capitalizes the first letter of a given word.

    Args:
        word (str): The word to capitalize the first letter.

    Returns:
        str: The word with the first letter capitalized.
    """
    return word[0].upper() + word[1:]


def append_special_symbol(word: str) -> str:
    """
    Appends a random special symbol to the given word.

    Args:
        word (str): The word to append a special symbol.

    Returns:
        str: The word with a random special symbol appended to it.
    """
    special_symbols = "!@#$%^&*"
    return word + choice(list(special_symbols))


def make_pass_phrase(
    number_of_words: int,
    number_of_words_to_capitalize: int,
    number_of_words_to_special_symbols: int,
) -> str:
    """
    Generate a passphrase using a dictionary of words.

    Reads a dictionary of words from a file, selects a specified number of words, capitalizes a specified number of words,
    and adds special symbols to a specified number of words. Finally, it prints a passphrase by joining the selected words
    in a random order with dashes.

    Args:
        number_of_words (int): The number of words to generate the passphrase.
        number_of_words_to_capitalize (int): The number of words to capitalize.
        number_of_words_to_special_symbols (int): The number of words to add special symbols.

    Returns:
        str: The generated passphrase.
    """
    with open(
        Path(__file__).parent.joinpath("dict.txt"), "r", encoding="utf-8"
    ) as file:
        words_massive = file.readlines()

    select_words = []
    i = 0
    while i < number_of_words:
        selected_word = choice(words_massive).strip().lower()
        if selected_word not in select_words:
            select_words.append(selected_word)
            i += 1

    capitalized_words = []
    i = 0
    while i < number_of_words_to_capitalize:
        word = choice(select_words)
        if capitalize_first_letter(word) not in capitalized_words:
            select_words.remove(word)
            select_words.append(capitalize_first_letter(word))
            capitalized_words.append(capitalize_first_letter(word))
            i += 1

    words_with_special_symbols = []
    i = 0
    while i < number_of_words_to_special_symbols:
        word = choice(select_words)
        if append_special_symbol(word) not in words_with_special_symbols:
            select_words.remove(word)
            select_words.append(append_special_symbol(word))
            words_with_special_symbols.append(append_special_symbol(word))
            i += 1

    return "-".join(choice(list(permutations(select_words))))


def main():
    """
    The main function of the script.
    """
    parser = argparse.ArgumentParser(
        description="Generate a passphrase using a dictionary of words."
    )
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")
    parser_phrase = subparsers.add_parser("phrase", help="Generate a passphrase")
    parser_phrase.add_argument(
        "-w",
        "--words",
        type=int,
        default=5,
        help="The number of words to generate the passphrase. (default: 5)",
    )
    parser_phrase.add_argument(
        "-c",
        "--capitalize",
        type=int,
        default=4,
        help="The number of words to capitalize. (default: 4)",
    )
    parser_phrase.add_argument(
        "-s",
        "--special",
        type=int,
        default=3,
        help="The number of words to add special symbols. (default: 3)",
    )

    parser_string = subparsers.add_parser("string", help="Generate a random string")
    parser_string.add_argument(
        "-b",
        "--blocks",
        type=int,
        default=5,
        help="Nuimber of string blocks. (default: 5)",
    )
    parser_string.add_argument(
        "-l",
        "--length",
        type=int,
        default=5,
        help="Length of the single string block. (default: 5)",
    )
    parser_string.add_argument(
        "-d",
        "--delimiter",
        type=str,
        default="-",
        help="String block delimiter. (default: '-')",
    )

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    if args.command == "phrase":
        print(
            make_pass_phrase(
                number_of_words=args.words,
                number_of_words_to_capitalize=min(args.capitalize, args.words),
                number_of_words_to_special_symbols=min(args.special, args.words),
            )
        )
    if args.command == "string":
        print(
            get_random_string(
                args.blocks * args.length,
                split_step=args.length,
                delimiter=args.delimiter,
            )
        )


if __name__ == "__main__":
    main()
