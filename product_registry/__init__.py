from flask import Flask, g
import markdown
import os
import shelve
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("stubCollection.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as md_file:
        content = md_file.read()
        return markdown.markdown(content)

class ProductList(Resource):
    def get(self):
        collection = get_db()
        keys = list(collection.keys())

        products = []

        for key in keys:
            products.append(collection[key])

        return {'message': 'My products', 'data': products}, 200

class Product(Resource):
    def get(self, identifier):
        collection = get_db()

        if not (identifier in collection):
            return {'message': 'Product not found', 'data': {}}, 404

        return {'message': 'Product found', 'data': collection[identifier]}, 200
    
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('price', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        collection = get_db()
        collection[args['identifier']] = args

        return {'message': 'Product registered', 'data': args}, 201

product_routes = [
    '/product',
    '/product/<string:identifier>'
]

api.add_resource(ProductList, '/products')
api.add_resource(Product, *product_routes)
