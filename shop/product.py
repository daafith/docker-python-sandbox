from flask_restful import Resource, reqparse
from .db import Collection, get_db

class Product(Resource):
    def get(self, identifier):
        products = get_db(Collection.products)

        if not (identifier in products):
            return {'message': 'Product not found'}, 404

        return {'message': 'Product found', 'product': products[identifier]}, 200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('price', required=True)

        args = parser.parse_args()
        products = get_db(Collection.products)

        if (args['identifier'] in products):
            return {'message': 'Product already exists'}, 409
 
        products[args['identifier']] = args
        return {'message': 'Product registered', 'product': args}, 201
    
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('price', required=True)

        args = parser.parse_args()
        products = get_db(Collection.products)

        if not (args['identifier'] in products):
            return {'message': 'Product not found'}, 404
 
        products[args['identifier']] = args
        return {'message': 'Product updated', 'product': args}, 200

class ProductList(Resource):
    def get(self):
        products = get_db(Collection.products)
        keys = list(products.keys())

        ps = []

        for key in keys:
            ps.append(products[key])

        return {'message': 'Products found', 'products': ps}, 200
