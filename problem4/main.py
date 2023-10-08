def ubah_huruf(sentence):
    cipher_key = 10
    pattern = ""

    for char in sentence:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - shift + cipher_key) % 26 + shift)
            pattern += encoded_char
        else:
            pattern += char

    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB