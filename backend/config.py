import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:12345678@localhost/flask_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
