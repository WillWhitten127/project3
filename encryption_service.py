from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import environ
import base64

# Load the encryption key from an environment variable
AES_ENCRYPTION_KEY = environ.get('AES_ENCRYPTION_KEY').encode()

def encrypt(data):
    """
    Encrypts the given data using AES encryption.

    :param data: The data to encrypt.
    :return: Encrypted data in base64 format.
    """
    # Ensure data is bytes
    if not isinstance(data, bytes):
        data = data.encode()

    # Create a cipher object using the first 32 bytes of the AES key
    cipher = Cipher(algorithms.AES(AES_ENCRYPTION_KEY[:32]), modes.CBC(b'16_byte_iv___'), backend=default_backend())
    encryptor = cipher.encryptor()

    # Padding for the input data
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Perform encryption and return the base64 encoded result
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(encrypted_data).decode()

def decrypt(encrypted_data):
    """
    Decrypts the given encrypted data using AES.

    :param encrypted_data: The data to decrypt, in base64 format.
    :return: Decrypted data as a string.
    """
    # Decode the base64 data
    encrypted_data_bytes = base64.b64decode(encrypted_data)

    # Create a cipher object
    cipher = Cipher(algorithms.AES(AES_ENCRYPTION_KEY[:32]), modes.CBC(b'16_byte_iv___'), backend=default_backend())
    decryptor = cipher.decryptor()

    # Perform decryption
    decrypted_padded = decryptor.update(encrypted_data_bytes) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

    return decrypted_data.decode()

# Example Usage
# encrypted = encrypt('Secret Data')
# print(encrypted)
# decrypted = decrypt(encrypted)
# print(decrypted)
