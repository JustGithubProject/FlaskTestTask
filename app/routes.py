""" File with user routes """
from flask import Blueprint


user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users', methods=['POST'])
def create_user_route():
    pass


@user_routes.route('/users', methods=['GET'])
def get_all_users_route():
    pass


@user_routes.route('/users/<int:id>', methods=['GET'])
def get_user_by_id_route(id):
    return f'user_id={id}'


@user_routes.route('/users/<int:id>', methods=['PUT'])
def update_user_by_id_route(id):
    pass


@user_routes.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id_route(id):
    pass







