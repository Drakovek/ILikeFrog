#!/usr/bin/env python3

from argparse import ArgumentParser

def pad_num(num:str) -> str:
    padded = num
    while len(padded) < 5:
        padded = "0" + padded
    return padded

def decimal_to_ternary(decimal:int) -> str:
    if decimal == 0:
        return "0"
    main = decimal//3
    remainder = decimal%3
    if main == 0:
        return str(remainder)
    else:
        return decimal_to_ternary(main) + str(remainder)

def ternary_to_decimal(ternary:str) -> int:
    final = 0
    multiplier = 1
    for index in range(0, len(ternary)):
        final += int(ternary[len(ternary) - (index + 1)]) * multiplier
        multiplier = multiplier * 3
    return final

def english_to_frog(text:str):
    frog = ""
    for cnum in range(0, len(text)):
        char = ord(text[cnum])
        if(char < 128):
            frog = frog + pad_num(decimal_to_ternary(char))
    # Convert ternary values to frog-speak
    frog = frog.replace("0", "I")
    frog = frog.replace("1", "Like")
    frog = frog.replace("2", "Frog")
    return frog

def frog_to_english(text:str):
    frog = text.lower()
    dec_string = ""
    # Convert to string of decimals
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
            return "Not valid frog-talk!"
    # Convert decimal string to English
    try:
        english = ""
        while len(dec_string) > 0:
            english = english + str(chr(ternary_to_decimal(dec_string[:5])))
            dec_string = dec_string[5:]
        return english
    except:
        return "Not valid frog-talk!"
    

if __name__ == "__main__":
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
    if args.english:
        # Convert frog-talk to English
        print("ENGLISH: " + frog_to_english(args.text))
    else:
        # Convert English to frog-talk
        print("FROG TALK: " + english_to_frog(args.text))
    
