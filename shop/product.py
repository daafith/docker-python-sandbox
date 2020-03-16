from flask_restful import Resource, reqparse
from .db import Collection, get_db

class Product(Resource):
    def get(self, identifier):
        products = get_db(Collection.products)
        if not (identifier in products):
            return {'message': 'Product not found'}, 404

        return {'message': 'Product found', 'product': products[identifier]}, 200
    
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('price', type=int, required=True)

        args = parser.parse_args()
        products = get_db(Collection.products)

        if (args['identifier'] in products):
            return {'message': 'Product already exists'}, 409
        
        if int(args['price']) <= 0:
            return {'message': 'Price must be higher than 0'}, 400
 
        products[args['identifier']] = args
        return {'message': 'Product registered', 'product': args}, 201
    
    def put(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('price', type=int, required=True)

        args = parser.parse_args()
        products = get_db(Collection.products)

        if not (args['identifier'] in products):
            return {'message': 'Product not found'}, 404

        if int(args['price']) <= 0:
            return {'message': 'Price must be higher than 0'}, 400
 
        products[args['identifier']] = args
        return {'message': 'Product updated', 'product': args}, 200

    def delete(self, identifier):
        products = get_db(Collection.products)
        if not (identifier in products):
            return {'message': 'Product does not exist (anymore)'}, 410

        del products[identifier]
        return {'message': 'Product removed'}, 200

class ProductList(Resource):
    def get(self):
        products = get_db(Collection.products)
        keys = list(products.keys())

        ps = []

        for key in keys:
            ps.append(products[key])

        return {'message': str(len(ps)) + ' Product(s) found', 'products': ps}, 200
