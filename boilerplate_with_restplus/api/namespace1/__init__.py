from flask_restplus import Namespace, Resource

api = Namespace('ns1', description='Namespace1 operations')


@api.route('/')
class Test(Resource):

    def get(self):
        return "from Namespace1"
