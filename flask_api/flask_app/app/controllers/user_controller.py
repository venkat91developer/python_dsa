from flask import Blueprint, request, jsonify
from app.models.user_model import User, db
from app.forms import RegistrationForm, LoginForm

user_controller = Blueprint('user', __name__)

@user_controller.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    return jsonify({'error': 'Invalid input'}), 400

@user_controller.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:  # Replace with hashed password check
            return jsonify({'message': 'Login successful', 'user': user.to_dict()}), 200
        return jsonify({'error': 'Invalid username or password'}), 401
    return jsonify({'error': 'Invalid input'}), 400
