from flask import Blueprint, request

main_routes_bp = Blueprint('main_routes', __name__)

@main_routes_bp.route('/', methods=['GET'])
def root():
    return "Welcome to the Brain Dump API, work is being done here"