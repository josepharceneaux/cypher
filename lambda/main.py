#!/usr/bin/env python3


import argparse

from subsitution import Substitution


CLEAR_TEXT = "This is a test"

substitution_obj = Substitution()

if __name__ == "__main__":

    s = "I love you"
    print("String: " + s)
    encoded = substitution_obj.encode(s)
    print("Encoded: " + encoded)
    decoded = substitution_obj.decode(encoded)
    print("Decoded: " + decoded)
