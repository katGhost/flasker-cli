from flask import Blueprint, jsonify

app_bp = Blueprint(__name__)

@app_bp.route('/')
def index():
    return jsonify({'message': 'Welcome to Flasker!'})