from flask import Blueprint
from .views import TestView

bp = Blueprint('api', __name__, url_prefix='/api/v1/ns1')


bp.add_url_rule('/', view_func=TestView.as_view('test_view'))
