# ILikeFrog

A utility for converting between English and Frog-Talk

# Instalation
ILikeFrog can be installed from its PyPI package using pip:

    pip install ilikefrog

# How to use
Requires python v3 or higher.

Install the ilikefrog package and run using the following command.

    ilikefrog *text* [-e]

Use the -e/--english tag to convert your text from Frog-Talk to English.
Otherwise the program will convert from English to Frog-Talk.

# Examples

    ilikefrog "Yay frog!"

    > FROG TALK:
    LikeIIFrogFrogLikeILikeFrogLikeLikeLikeLikeLikeLikeILikeILikeFrogLikeIFrogLikeILikeLikeIFrogILikeLikeILikeILikeIFrogLikeLikeILikeIFrogI

    ilikefrog -e "IFrogLikeFrogLikeLikeLikeIFrogILikeLikeILikeILikeIFrogLikeLikeLikeIFrogLikeLikeLikeLikeLikeLikeLike"

    > ENGLISH:
    Froggy
