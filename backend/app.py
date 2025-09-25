import os
from flask import Flask, request, jsonify, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from config import Config
from models import db, User, File

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend')
app.config.from_object(Config)

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Frontend Routes
@app.route('/signup')
def signup_page():
    return send_from_directory(app.template_folder, 'signup.html')

@app.route('/login')
def login_page():
    return send_from_directory(app.template_folder, 'login.html')

@app.route('/dashboard')
@login_required
def dashboard_page():
    return send_from_directory(app.template_folder, 'dashboard.html')

# API Routes
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        name=data['name'],
        age=data['age'],
        address=data['address'],
        email=data['email'],
        mobile=data['mobile'],
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        session['name'] = user.name
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/logout')
@login_required
def logout():
    logout_user()
    session.pop('name', None)
    return jsonify({'message': 'Logout successful'})

@app.route('/api/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(f"{current_user.name}_{file.filename}")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        new_file = File(
            filename=filename,
            filetype=filename.rsplit('.', 1)[1].lower(),
            user_id=current_user.id
        )
        db.session.add(new_file)
        db.session.commit()
        
        return jsonify({'message': 'File uploaded successfully'}), 201
    return jsonify({'message': 'File type not allowed'}), 400

@app.route('/api/download/<filename>')
@login_required
def download_file(filename):
    if "sample.pdf" in filename:
        return send_from_directory(app.static_folder, 'sample.pdf', as_attachment=True)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/api/files')
@login_required
def get_files():
    user_files = File.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'filename': f.filename} for f in user_files])

@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'login.html')

if __name__ == '__main__':
    app.run(debug=True)
