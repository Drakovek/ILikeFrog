#!/usr/bin/env python3

from argparse import ArgumentParser

def pad_num(num:str=None, length:int=0) -> str:
    """
    Pads out a number string with zeros until the desired length.

    :param num: Number string to pad out, defaults to None
    :type num: str, optional
    :param length: Length of the returned string, defaults to 0
    :type length: int, optional
    :return: Number string with the desired length, padded if necessary
    :rtype: str
    """
    # Return string of length if given string is invalid
    if num is None:
        return pad_num("", length)
    # Pad out number
    padded = num
    while len(padded) < length:
        padded = "0" + padded
    return padded

def decimal_to_ternary(decimal:int=0) -> str:
    """
    Converts from a positive decimal integer to a ternary string.

    :param decimal: Decimal integer, defaults to 0
    :type decimal: int, optional
    :return: String of ternary conversion of decimal
    :rtype: str
    """
    # Returns "0" if decimal is negative or already 0
    if decimal < 1:
        return "0"
    # Convert to ternary
    main = decimal // 3
    remainder = decimal % 3
    if main == 0:
        return str(remainder)
    else:
        return decimal_to_ternary(main) + str(remainder)

def ternary_to_decimal(ternary:str=None) -> int:
    """
    Converts from a ternary string to a decimal integer.

    :param ternary: String of a ternary number, defaults to None
    :type ternary: str, optional
    :return: Decimal conversion of the given ternary number
    :rtype: int
    """
    try:
        # Attempt converting ternary to decimal
        final = 0
        multiplier = 1
        for index in range(0, len(ternary)):
            final += int(ternary[len(ternary) - (index + 1)]) * multiplier
            multiplier = multiplier * 3
        return final
    except (ValueError, TypeError):
        # Returns 0 if given value wasn't a valid ternary number
        return 0

def english_to_frog(text:str=None) -> str:
    """
    Converts given text to "Frog-Talk"

    :param text: Given English text to convert, defaults to None
    :type text: str, optional
    :return: Given text converted to "Frog-Talk"
    :rtype: str
    """
    # Return empty string if given text is invalid
    if text is None:
        return ""
    # Run through every character in the given text
    frog = ""
    for cnum in range(0, len(text)):
        # Get the decimal UTF-8 value of the current charcter.
        char = ord(text[cnum])
        # Check if character is in the ASCII range
        if(char < 128):
            # Add padded ternary value of the character to frog text
            frog = frog + pad_num(decimal_to_ternary(char), 5)
    # Convert ternary decimals to frog-speak terms
    frog = frog.replace("0", "I")
    frog = frog.replace("1", "Like")
    frog = frog.replace("2", "Frog")
    return frog

def frog_to_english(text:str=None) -> str:
    """
    Converts from "Frog-Talk" back to standard text.

    :param text: Given Frog-Talk text to convert, defaults to None
    :type text: str, optional
    :return: Given text converted from "Frog-Talk" to English
    :rtype: str
    """
    # Return None if given text is invalid
    if text is None:
        return None
    # Convert "Frog-Talk" to string of ternary digits
    dec_string = ""
    frog = text.lower()
    while len(frog) > 0:
        if frog.startswith("i"):
            dec_string = dec_string + "0"
            frog = frog[1:]
        elif frog.startswith("like"):
            dec_string = dec_string + "1"
            frog = frog[4:]
        elif frog.startswith("frog"):
            dec_string = dec_string + "2"
            frog = frog[4:]
        else:
            return None
    # Convert decimal string to English
    try:
        english = ""
        while len(dec_string) > 0:
            # Get block of five ternary digits
            char = dec_string[:5]
            # Return None if 5 digit block doesn't exist
            if not len(char) == 5:
                return None
            # Convert ternary to decimal, then to ASCII character
            english = english + str(chr(ternary_to_decimal(char)))
            dec_string = dec_string[5:]
        return english
    except:
        return None

def main():
    """
    Parses user arguments for converting to/from Frog-Talk.
    """
    parser = ArgumentParser()
    parser.add_argument(
        "text",
        help="Text to convert to/from frog-talk.",
        type=str)
    parser.add_argument(
        "-e",
        "--english",
        help="Flag for converting frog-talk back to english.",
        action="store_true")
    args = parser.parse_args()
    text = None
    print()
    # Convert text
    if args.english:
        # Convert frog-talk to English
        text = frog_to_english(args.text)
        print("ENGLISH:")
    else:
        # Convert English to frog-talk
        text = english_to_frog(args.text)
        print("FROG TALK:")
    # Print converted text
    if text is None:
        print("[INVALID INPUT]")
    else:
        print(text)

if __name__ == "__main__":
    main()
