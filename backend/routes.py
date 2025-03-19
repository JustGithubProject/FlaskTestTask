""" File with user routes """
from flask import Blueprint, jsonify, request

from core.services import user_service


user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()

    # If name and email are missing
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email required'}), 400
    
    # Does user exist?
    user = user_service.get_user_by_email(data['email'])
    if user:
        return jsonify({'error': 'User already exists'}), 400
    
    # Creating new user
    user_service.create_user(data['name'], data['email'])
    return jsonify({'message': 'User created'}), 201


@user_routes.route('/users', methods=['GET'])
def get_all_users_route():
    # Fetching all users
    users = user_service.fetch_all_users()
    return jsonify([user.to_dict() for user in users]), 200


@user_routes.route('/users/<int:id>', methods=['GET'])
def get_user_by_id_route(id: int):
    # Fetching user by id
    user = user_service.get_user_by_id(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200


@user_routes.route('/users/<int:id>', methods=['PUT'])
def update_user_by_id_route(id: int):
    data = request.get_json()
    
    # If name and email are missing
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email required'}), 400
    
    # Does user exist?
    user = user_service.get_user_by_id(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Updating user by id
    user_service.update_user_by_id(id, data['name'], data['email'])
    
    return jsonify({"message": f"User {id} updated"}), 200


@user_routes.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id_route(id: int):
    # Does user exist?
    user = user_service.get_user_by_id(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Deleting user by id
    user_service.delete_user_by_id(id)
    return jsonify({"message": f"User {id} deleted"}), 200






