#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT Authentication
Implements role-based access control (Task 5)
"""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
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
    """Callback for HTTPBasicAuth to verify credentials."""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token"""
    return jsonify({"error": "Token has been revoked"}), 401

def handle_auth_error(err):
    """Returns 401 Unauthorized for all JWT authentication failures."""
    return jsonify({"error": "Missing or invalid token"}), 401

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to obtain JWT token."""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password']
    user = users.get(username)

    if user is None or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    additional_claims = {"role": user['role']}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )

    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route using JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Protected route accessible only to admin users (RBAC)."""
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

@app.route('/data')
def data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    """Returns the details for a specific user (password hash excluded)."""
    user_info = users.get(username)
    if user_info:
        safe_info = user_info.copy()
        safe_info.pop('password', None)
        return jsonify(safe_info)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Handles POST request to add a new user (basic Task 4 functionality)."""
    new_user_data = request.get_json()
    username = new_user_data.get('username')
    password = new_user_data.get('password')
    role = new_user_data.get('role', 'user')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    users[username] = {
        "username": username,
        "password": generate_password_hash(password),
        "role": role
    }

    return jsonify({
        "message": "User added and secured",
        "username": username
    }), 201


if __name__ == '__main__':
    app.run(debug=True)
