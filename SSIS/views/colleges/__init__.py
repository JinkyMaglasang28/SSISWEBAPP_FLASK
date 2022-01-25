from flask import Blueprint

colleges = Blueprint('college', __name__)

from . import routes