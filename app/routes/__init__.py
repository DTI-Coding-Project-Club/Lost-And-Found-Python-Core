# This is initialization class for all the route files
from flask import Blueprint

bp = Blueprint("routes", __name__)

# Developers need to add the new route files below for it to come into effect
from . import health_route
