import sys
import os
import json
import urllib3


from substitution import Substitution


def lambda_handler(event, context):
    """
    """

    print("Python 3.10 Cypher Function")

    s = Substitution()

    action = event['queryStringParameters']['request']
    if action and action == "encrypt":
        print("Encrypting")
        plain_text = event['queryStringParameters']['plaintext']
        encoded_text = s.encode(plain_text)
    elif action and action == "decrypt":
        encoded_text = event['queryStringParameters']['encodedtext']
        print("Decrypting")
        plain_text = s.decode(encoded_text)
    else:
        action = "unknown action"
        plaintext = ""
        encoded_text = ""
        print("Unknown request")

    return {
        'request': action,
        'plaintext': plain_text,
        'encodedtext': encoded_text
        }
