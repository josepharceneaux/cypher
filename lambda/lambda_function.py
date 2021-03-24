import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__)))
# from subsitution import Substitution
import substitution

# def lambda_handler(event, context):
#     """
#     """
#     s = substitution.Substitution()
#     if event['request'] == "encrypt":
#         plain_text = event['plainText']
#         encoded_text = s.encode(plain_text)
#     else:
#         encoded_text = event['encodedText']
#         plain_text = s.decode(encoded_text)

#     return {
#         'encodedText': encoded_text,
#         'plainText': plain_text,
#         }


def lambda_handler(event, context):
    """
    """
    return json.dumps(event)
