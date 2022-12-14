def encrypt(plaintext, shift):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            shift_ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shift_ch
        else:
            ciphertext += ch
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            shift_ch = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            plaintext += shift_ch
        else:
            plaintext += ch
    return plaintext
