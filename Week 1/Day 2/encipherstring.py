def caesar_cipher(plaintext, shift):
    cipher = ''

    for char in plaintext:
        val = ord(char) + shift
        cipher += chr(val)

    return cipher


text = "abcwxy"

print(caesar_cipher(text, 1))
