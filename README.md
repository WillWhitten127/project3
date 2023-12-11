Main Application Directory

    app.py - The main Flask application file where routes and app initialization are defined.
    config.py - Configuration file for setting up database connections, environment variables, and other configurations.

Database Models

    models/
        __init__.py - Initializes the models package.
        user.py - Defines the User model for the database.
        auth_log.py - Defines the AuthLog model for logging authentication requests.

Services and Utilities

    services/
        __init__.py - Initializes the services package.
        encryption_service.py - Contains functions for AES encryption and decryption.
        password_service.py - Functions for password hashing and verification.
    utils/
        __init__.py - Initializes the utilities package.
        rate_limiter.py - Configures the rate limiting functionality.
Tests

    tests/
        __init__.py - Initializes the tests package.
        test_user_model.py - Tests for the User model.
        test_auth_log_model.py - Tests for the AuthLog model.
        test_encryption_service.py - Tests for encryption and decryption functionality.
        test_password_service.py - Tests for password hashing and verification.
