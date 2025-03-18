""" File with user routes """
from flask import Blueprint, jsonify


user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users', methods=['POST'])
def create_user_route():
    return jsonify({'message': 'User created'}), 201


@user_routes.route('/users', methods=['GET'])
def get_all_users_route():
    return jsonify({'users': []}), 200


@user_routes.route('/users/<int:id>', methods=['GET'])
def get_user_by_id_route(id):
    return jsonify({'user_id': id}), 200


@user_routes.route('/users/<int:id>', methods=['PUT'])
def update_user_by_id_route(id):
    return jsonify({"message": f"User {id} updated"}), 200


@user_routes.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id_route(id):
    return jsonify({"message": f"User {id} deleted"}), 200






