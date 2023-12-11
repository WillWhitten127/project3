from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize the Flask application
app = Flask(__name__)

# Load the configuration from the Config class in config.py
app.config.from_object(Config)

# Initialize the database with SQLAlchemy
db = SQLAlchemy(app)

# Import routes
from your_project import routes
