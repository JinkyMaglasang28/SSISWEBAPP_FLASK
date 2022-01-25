from flask import Blueprint

courses = Blueprint('course', __name__)

from . import routes