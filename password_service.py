from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Initialize the PasswordHasher with Argon2 parameters
ph = PasswordHasher(
    time_cost=2,  # Time cost
    memory_cost=102400,  # Memory cost
    parallelism=8,  # Parallelism factor
    hash_len=16,  # Hash length
    salt_len=16  # Salt length
)

def generate_password_hash(password):
    """
    Generates a hash for the given password.

    :param password: The password to hash.
    :return: A hashed password.
    """
    return ph.hash(password)

def verify_password_hash(hashed_password, password):
    """
    Verifies a password against a given hash.

    :param hashed_password: The hash to verify against.
    :param password: The password to verify.
    :return: True if the password matches the hash, otherwise False.
    """
    try:
        ph.verify(hashed_password, password)
        return True
    except VerifyMismatchError:
        return False
