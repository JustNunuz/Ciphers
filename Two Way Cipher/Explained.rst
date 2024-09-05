Title: Two-Way Encryption with Mouse Position and Timestamp-Based Key Generation
=======================================================================================================

This reStructuredText (RST) file provides an explanation and documentation for a Python script that demonstrates a two-way encryption system using a mouse position and timestamp-based key generation method. The script uses the `cryptography` library to encrypt and decrypt the input text.

Code Overview
-------------

The script consists of several functions:

1. `get_mouse_position()`: This function retrieves the current mouse position on the screen and returns it as a string in the format "x_y".
2. `generate_key(mouse_position, timestamp)`: This function generates a random encryption key based on the mouse position and timestamp. The function uses the mouse position and timestamp as a seed for the random number generator.
3. `encrypt(key, plain_text)`: This function encrypts the input plain text using the provided encryption key and returns the cipher text.
4. `decrypt(key, cipher_text)`: This function decrypts the input cipher text using the provided encryption key and returns the plain text.
5. `two_way_encryption()`: This function is the main function that performs the two-way encryption. The function prompts the user to enter the text to encrypt, retrieves the current mouse position and timestamp, generates an encryption key, encrypts the input text, decrypts the cipher text, and prints the encrypted and decrypted text.

Two-Way Encryption
------------------

The script demonstrates a two-way encryption system that uses a mouse position and timestamp-based key generation method. The key generation method ensures that the encryption key is unique for each encryption operation, making it more secure. The script uses the `Fernet` class from the `cryptography` library to encrypt and decrypt the input text.

Usage
-----

To use this script, follow these steps:

1. Install the required library: `cryptography`.
2. Run the script.
3. The script will prompt the user to enter the text to encrypt.
4. The script will retrieve the current mouse position and timestamp, generate an encryption key, encrypt the input text, decrypt the cipher text, and print the encrypted and decrypted text.

Disclaimer
----------

This script is intended for educational purposes only. The authors and contributors of this script do not condone or promote any illegal or unethical activities. The script should not be used to encrypt sensitive information without proper authorization.
