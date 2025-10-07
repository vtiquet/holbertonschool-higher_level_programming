#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT Authentication
Implements role-based access control (Task 5)
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = 'your-secret-key-for-task-5'
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth"""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


@jwt.unauthorized_loader
@jwt.invalid_token_loader
@jwt.expired_token_loader
@jwt.revoked_token_loader
@jwt.needs_fresh_token_loader
def handle_auth_error(err):
    """Ensures all JWT authentication failures return a 401 status code."""
    return jsonify({"error": "Missing or invalid token"}), 401



@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to obtain JWT token"""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    additional_claims = {"role": users[username]['role']}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )

    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route using JWT Authentication"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Protected route accessible only to admin users (RBAC)"""
    claims = get_jwt()
    role = claims.get('role', None)

    if role != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)