from flask_restful import Resource, reqparse
from .productRepository import ProductRepository

class Product(Resource):
    def __init__(self):
        self.repo = ProductRepository()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('price', type=int, required=True)

    def get(self, name=None):
        if name is None:
            ps = self.repo.all()
            return {'message': str(len(ps)) + ' Product(s) found', 'products': ps}, 200

        if not self.repo.hasItem(name):
            return {'message': 'Product not found'}, 404
        
        return {'message': 'Product found', 'product': self.repo.get(name)}, 200
    
    def post(self):
        args = self.parser.parse_args()

        if self.repo.hasItem(args['name']):
            return {'message': 'Product already exists'}, 409
        
        if int(args['price']) <= 0:
            return {'message': 'Price must be higher than 0'}, 400
 
        self.repo.save(args)
        return {'message': 'Product registered', 'product': args}, 201
    
    def put(self):
        args = self.parser.parse_args()

        if not self.repo.hasItem(args['name']):
            return {'message': 'Product not found'}, 404

        if int(args['price']) <= 0:
            return {'message': 'Price must be higher than 0'}, 400
         
        self.repo.update(args)
        return {'message': 'Product updated', 'product': args}, 200

    def delete(self, name):
        if not self.repo.hasItem(name):
            return {'message': 'Product does not exist (anymore)'}, 410

        self.repo.remove(name)
        return {'message': 'Product removed'}, 200

