import os

class Config:
    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AES Encryption Key
    AES_ENCRYPTION_KEY = os.environ.get('NOT_MY_KEY')

    # Argon2 Configuration for Password Hashing (Adjust these as needed)
    ARGON2_TIME_COST = 2
    ARGON2_MEMORY_COST = 102400
    ARGON2_PARALLELISM = 8
    ARGON2_HASH_LENGTH = 16
    ARGON2_SALT_LENGTH = 16
