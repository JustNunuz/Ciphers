import random
import win32api
import win32con
import time
from cryptography.fernet import Fernet

def get_mouse_position():
    x, y = win32api.GetCursorPos()
    return str(x) + "_" + str(y)

def generate_key(mouse_position, timestamp):
    seed = int(mouse_position + str(timestamp))
    random.seed(seed)
    return Fernet.generate_key()

def encrypt(key, plain_text):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plain_text.encode())
    return cipher_text

def decrypt(key, cipher_text):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text.decode()

def two_way_encryption():
    plain_text = input("Enter the text to encrypt: ")
    mouse_position = get_mouse_position()
    timestamp = int(time.time() * 1000)
    key = generate_key(mouse_position, timestamp)
    cipher_text = encrypt(key, plain_text)
    print("Encrypted text:", cipher_text)
    decrypted_text = decrypt(key, cipher_text)
    print("Decrypted text:", decrypted_text)

two_way_encryption()