from i_like_frog.main.ilikefrog import decimal_to_ternary
from i_like_frog.main.ilikefrog import english_to_frog
from i_like_frog.main.ilikefrog import english_to_simple_frog
from i_like_frog.main.ilikefrog import frog_to_english
from i_like_frog.main.ilikefrog import pad_num
from i_like_frog.main.ilikefrog import simple_frog_to_english
from i_like_frog.main.ilikefrog import ternary_to_decimal

def test_pad_num():
    """
    Tests the pad_num function.
    """
    # Test padding number
    assert pad_num("123", 5) == "00123"
    assert pad_num("63", 2) == "63"
    assert pad_num("702", 2) == "702"
    # Test padding invalid string
    assert pad_num(None, 5) == "00000"
    assert pad_num("", 3) == "000"

def test_decimal_to_ternary():
    """
    Tests the decimal_to_ternary function.
    """
    # Test converting decimal to ternary
    assert decimal_to_ternary(0) == "0"
    assert decimal_to_ternary(2) == "2"
    assert decimal_to_ternary(3) == "10"
    assert decimal_to_ternary(25) == "221"
    assert decimal_to_ternary(128) == "11202"
    # Test converting invalid integers
    assert decimal_to_ternary(-1) == "0"
    assert decimal_to_ternary() == "0"

def test_ternary_to_decimal():
    """
    Tests the ternary_to_decimal function.
    """
    # Test converting ternary to decimal
    assert ternary_to_decimal("0") == 0
    assert ternary_to_decimal("2") == 2
    assert ternary_to_decimal("10") == 3
    assert ternary_to_decimal("221") == 25
    assert ternary_to_decimal("11202") == 128
    # Test converting invalid ternary numbers
    assert ternary_to_decimal("-1") == 0
    assert ternary_to_decimal("NotANumber") == 0
    assert ternary_to_decimal(None) == 0
    assert ternary_to_decimal() == 0

def test_english_to_frog():
    """
    Tests the english_to_frog function.
    """
    # Test converting text to "Frog-Talk"
    frog = "IFrogLikeFrogLikeLikeLikeIFrogILikeLikeILikeILikeIFrog"\
           +"LikeLikeLikeIFrogLikeLikeLikeLikeLikeLikeLike"
    assert english_to_frog("Froggy") == frog
    frog = "LikeIIFrogFrogLikeILikeFrogLikeLikeLikeLikeLikeLikeILike"\
           +"ILikeFrogLikeIFrogLikeILikeLikeIFrogILikeLikeILikeILikeI"\
           +"FrogLikeLikeILikeIFrogI"
    assert english_to_frog("Yay frog!") == frog
    # Test converting invalid strings
    assert english_to_frog("") == ""
    assert english_to_frog("ÄëÎöú") == ""
    assert english_to_frog(None) == ""
    assert english_to_frog() == ""

def test_frog_to_english():
    """
    Tests the frog_to_english function.
    """
    # Test converting "Frog-Talk" to normal text
    frog = "IFrogLikeFrogLikeLikeLikeIFrogILikeLikeILikeILikeIFrog"\
           +"LikeLikeLikeIFrogLikeLikeLikeLikeLikeLikeLike"
    assert frog_to_english(frog) == "Froggy"
    frog = "likeIIFrogFrogLikeILikeFrogLikeLikeLikeLikeLikeLikeILike"\
           +"ILikeFrogLikeIFrogLikeILikeLikeIfrogIlikeLikeILikeILikeI"\
           +"FrogLikeLikeILikeIFrogI"
    assert frog_to_english(frog) == "Yay frog!"
    # Test converting invalid strings
    assert frog_to_english("") == ""
    assert frog_to_english(None) == None
    assert frog_to_english("Its Not Frog-Talk!") == None
    assert frog_to_english("FrogFrog") == None

def test_english_to_simple_frog():
    """
    Tests the english_to_simple_frog function.
    """
    # Test converting text to simplified Frog-Talk
    frog = "IIFrogIILikeILikeLikeIIFrogIIILikeFrogIIILikeILikeLikeI"\
           +"LikeLikeILikeIFrogFrogIIILike"
    assert english_to_simple_frog("Test message....") == frog
    frog = "FrogILikeILikeFrogIFrogIFrogFrogIFrogFrogIFrogIFrog"
    assert english_to_simple_frog("Froggy") == frog
    # Test converting invalid strings
    assert english_to_simple_frog("") == ""
    assert english_to_simple_frog("ÄëÎöú") == ""
    assert english_to_simple_frog(None) == ""
    assert english_to_simple_frog() == ""

def test_simple_frog_to_english():
    """
    Tests the simple_frog_to_english function.
    """
    # Test converting simplified Frog-Talk back to standard text
    frog = "IIFrogIILikeILikeLikeIIFrogIIILikeFrogIIILikeILikeLikeI"\
           +"LikeLikeILikeIFrogFrogIIILike"
    assert simple_frog_to_english(frog) == "TEST MESSAGE"
    frog = "FrogILikeILikeFrogIFrogIFrogFrogIFrogFrogIFrogIFrog"
    assert simple_frog_to_english(frog) == "FROGGY"
    # Test converting invalid strings
    assert simple_frog_to_english("") == ""
    assert simple_frog_to_english(None) == None
    assert simple_frog_to_english("Its Not Frog-Talk!") == None
    assert simple_frog_to_english("FrogFrog") == None
