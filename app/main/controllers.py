# app/main/controllers.py
# pylint: disable=missing-docstring

from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/hello')
def home():
    return "Hello from a Blueprint!"
