import sys
import os
import json


from subsitution import Substitution


def lambda_handler(event, context):
    """
    """
    s = Substitution()
    if event['request'] == "encrypt":
        plain_text = event['plaintext']
        encoded_text = s.encode(plain_text)
    else:
        encoded_text = event['encodedtext']
        plain_text = s.decode(encoded_text)

    return {
        'request': event['request'],
        'plaintext': plain_text,
        'encodedtext': encoded_text
        }
