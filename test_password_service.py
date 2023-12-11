from your_project.services.password_service import generate_password_hash, verify_password_hash

def test_password_hashing():
    """
    GIVEN a plain password
    WHEN a password is hashed and then verified
    THEN check that the verify function confirms it matches the original
    """
    password = "secure_password"
    hashed_password = generate_password_hash(password)
    assert verify_password_hash(hashed_password, password)
