# Caesar-Cipher--Encryption-Decryption

To use this code, you would call the encrypt() and decrypt() functions like this:

Copy code
plaintext = "hello world"
shift = 3
ciphertext = encrypt(plaintext, shift)
print(ciphertext)  # Output: khoor zruog

decrypted_text = decrypt(ciphertext, shift)
print(decrypted_text)  # Output: hello world
In this implementation, the shift parameter specifies the number of characters to shift the plaintext by. For example, with a shift of 3, the letter "a" becomes "d", "b" becomes "e", and so on. The Caesar cipher is a very simple and easy to understand substitution cipher, but it is also very easy to break, especially if the shift value is known. There are much more secure ways to encrypt and decrypt messages, such as the AES algorithm.
