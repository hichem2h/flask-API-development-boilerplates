from flask import Blueprint
from flask_restplus import Api


bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(bp, 
    title='My Title',
    version='1.0',
    description='A description',
)

from .namespace1 import api as ns1

api.add_namespace(ns1)
