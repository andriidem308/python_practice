"""
Написать функцию XOR_cipher, принимающая 2 аргумента:
строку, которую нужно зашифровать, и ключ шифрования.

Функция возвращает строку, зашифрованную путем применения
функции XOR (^) над символами строки с ключом.
Написать также функцию XOR_uncipher, которая по зашифрованной
строке и ключу восстанавливает исходную строку.
"""


def XOR_cipher(msg, k):
    longkey = ''
    for i in range(len(msg) // len(k) + 1):
        longkey += k

    res = ''
    for i in range(len(msg)):
        res += chr(ord(msg[i]) ^ ord(longkey[i]))

    return res


def XOR_cipher_1(msg, k):
    def _str_cycle(_sample):
        while True:
            for char in _sample:
                yield char

    def _cipher(_message, _key):
        encrypt = ''.join(
            chr(ord(mg_char) ^ ord(k_char))
            for mg_char, k_char in zip(_message, _str_cycle(_key))
        )

        return encrypt

    return _cipher(msg, k)



XOR_uncipher = XOR_cipher


message = input("Message for encryption: ")
key = input("Key of encryption: ")

e_message = XOR_cipher(message, key)
print('Encrypted message:', e_message)
print("Key:", XOR_cipher(message, e_message))
