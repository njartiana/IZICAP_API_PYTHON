import random


class Data:
    def generate_string_value(self, _lengthNumber):
        str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
              + "abcdefghijklmnopqrstuvxyz"
        return ''.join(random.choice(str) for caracter in range(_lengthNumber))

    def generate_number_value(self, _lengthNumber):
        number = "0123456789"
        return ''.join(random.choice(number) for numbre in range(_lengthNumber))

    def generate_alphanumeric_value(self, _lengthNumber):
        str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
              + "abcdefghijklmnopqrstuvxyz" \
              + "0123456789"
        return ''.join(random.choice(str) for caracter in range(_lengthNumber))
