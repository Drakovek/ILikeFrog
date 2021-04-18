# ILikeFrog

A utility for converting between English and Frog-Talk

# Instalation
ILikeFrog can be installed from its [PyPI package](https://pypi.org/project/ILikeFrog/) using pip:

    pip install ilikefrog

# How to use
Requires python v3 or higher.

Install the ilikefrog package and run using the following command.

    ilikefrog [text] [-e] [-s]

**-e/--english:** Converts your text from Frog-Talk to English. Otherwise the program will convert from English to Frog-Talk.

**-s/--simplified:** Uses a simplified version of Frog-Talk that takes less space, but only supports A-Z

# Examples

**English to Frog-Talk:**

    $ ilikefrog "Yay frog!"

    FROG TALK:
    LikeIIFrogFrogLikeILikeFrogLikeLikeLikeLikeLikeLikeILikeILikeFrogLikeIFrogLikeILikeLikeIFrogILikeLikeILikeILikeIFrogLikeLikeILikeIFrogI

**Frog-Talk to English:**

    $ ilikefrog -e "IFrogLikeFrogLikeLikeLikeIFrogILikeLikeILikeILikeIFrogLikeLikeLikeIFrogLikeLikeLikeLikeLikeLikeLike"

    ENGLISH:
    Froggy

**English to simplified Frog-Talk:**

    $ ilikefrog -s "RIBBIT RIBBIT"

    FROG TALK:
    ILikeFrogFrogIILikeLikeFrogLikeLikeFrogFrogIIIIFrogIIIILikeFrogFrogIILikeLikeFrogLikeLikeFrogFrogIIIIFrog

**Simplified Frog-Talk to English:**

    $ ilikefrog -s -e "LikeLikeIILikeFrogIFrogIILikeILikeFrogFrog"

    ENGLISH:
    CROAK
