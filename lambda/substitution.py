

KEY_STRING_TOP = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
KEY_STRING_BOTTOM = "WXYZABCDEFGHIJKLMNOPQRSTUVwxyzabcdefghijklmnopqrstuv "
KEY = [[], []]


class Substitution(object):
    """
    """

    def __init__(self):
        """
        """
        i = KEY_STRING_TOP.index('I')
        # print("INIT: " + str(i))
        # print("INIT: " + KEY_STRING_BOTTOM[i])

    def substitute(self, character):
        """
        """
        try:
            return KEY_STRING_BOTTOM[KEY_STRING_TOP.index(character)]

        except Exception as e:
            return 'E'

    def unsubstitute(self, character):
        """
        """
        try:
            c = KEY_STRING_TOP[KEY_STRING_BOTTOM.index(character)]
            return c

        except Exception as e:
            return 'E'

    def encode(self, s):
        """
        """
        encoded = ""
        for character in s:
            encoded = encoded + self.substitute(character)

        return encoded

    def decode(self, s):
        """
        """
        decoded = ""
        for character in s:
            decoded = decoded + self.unsubstitute(character)

        return decoded
