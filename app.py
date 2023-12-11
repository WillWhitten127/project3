from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from services.encryption_service import encrypt_message
from services.password_service import generate_password_hash
import os
import uuid

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Importing models after initializing db to avoid circular imports
from models.user import User
from models.auth_log import AuthLog

# Route for user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data['username']
    email = data['email']
    password = str(uuid.uuid4())  # Generating a UUIDv4 password

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create and store the new user
    new_user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"password": password}), 201

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
