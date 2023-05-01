import sys
import os
import json


from substitution import Substitution


def lambda_handler(event, context):
    """
    """

    print("New Cypher Function Starting")
    # print("Event plist:")
    # for key in event.keys():
    #     print("  Key: " + key)
    #     print("  Value: " + event[key])
    #     if key == "rawQueryString":
    #        print("  " + key + "Query String Values")
    #    else:
    #        print("  " + key + " : " + event[key])

    s = Substitution()
    
    action = event['request']
    if action and action == "encrypt":
        print("Encrypting")
        plain_text = event['plaintext']
        encoded_text = s.encode(plain_text)
    elif action and action == "decrypt":
        print("Decrypting")
        encoded_text = event['plaintext']
        plain_text = s.decode(encoded_text)
    else:
        action = "unknown action"
        print("Unknown request")

    return {
        'request': action,
        'plaintext': plain_text,
        'encodedtext': encoded_text
        }
