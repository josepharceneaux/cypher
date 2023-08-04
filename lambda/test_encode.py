import pytest


from . import substitution as Substitution


CLEAR_TEXT = "I love you"

def test_reverse():
    """
    Test the cypher object by encoding a string and then validating the decode of that string.
    """

    print("In TEST_REVERSE")
    
    coder = Substitution.Substitution()
    encoded = coder.encode(CLEAR_TEXT)
    decoded = coder.decode(encoded)
    assert decoded == CLEAR_TEXT

