from your_project.services.encryption_service import encrypt, decrypt

def test_encryption_decryption():
    """
    GIVEN a string
    WHEN it is encrypted and then decrypted
    THEN check that the initial and final strings are the same
    """
    original_string = "TestString"
    encrypted_string = encrypt(original_string)
    decrypted_string = decrypt(encrypted_string)
    assert original_string == decrypted_string
