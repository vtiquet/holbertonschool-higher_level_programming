#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """Returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """Returns the API status."""
    return "OK"


@app.route('/data')
def data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    """Returns the details for a specific user."""
    user_info = users.get(username)
    if user_info:
        return jsonify(user_info)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Handles POST request to add a new user."""
    new_user = request.get_json()

    if not new_user or 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user['username']

    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == '__main__':
    app.run()