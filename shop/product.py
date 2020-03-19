from flask_restful import Resource, reqparse
from .productRepository import ProductRepository

class Product(Resource):
    notFoundMessage = {'message': 'Product not found'}
    invalidPriceMessage = {'message': 'Price must be 5 or higher'}
    invalidAmountMessage = {'message': 'Size must be 1 or higher'}

    def __init__(self):
        self.repo = ProductRepository()
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('unitPrice', type=int, required=True)
        self.parser.add_argument('unitSize', type=int, required=True)
        self.parser.add_argument('unitType', choices=('ITEM', 'GRAM', 'MILLILITER'), required=True)

    def get(self, name=None):
        if name is None:
            ps = self.repo.all()
            return {'message': str(len(ps)) + ' Product(s) found', 'products': ps}, 200

        if not self.repo.hasItem(name):
            return Product.notFoundMessage, 404
        
        return {'message': 'Product found', 'product': self.repo.find(name)}, 200
    
    def post(self):
        args = self.parser.parse_args()

        if self.repo.hasItem(args['name']):
            return {'message': 'Product already exists'}, 409
        
        if not self.__isValidPrice(args):
            return Product.invalidPriceMessage, 400

        if not self.__isValidSize(args):
            return Product.invalidAmountMessage, 400
 
        self.repo.save(args)
        return {'message': 'Product registered', 'product': args}, 201
    
    def put(self):
        args = self.parser.parse_args()

        if not self.repo.hasItem(args['name']):
            return Product.notFoundMessage, 404

        if not self.__isValidPrice(args):
            return Product.invalidPriceMessage, 400
        
        if not self.__isValidSize(args):
            return Product.invalidAmountMessage, 400
         
        self.repo.update(args)
        return {'message': 'Product updated', 'product': args}, 200

    def delete(self, name):
        if not self.repo.hasItem(name):
            return Product.notFoundMessage, 410

        self.repo.remove(name)
        return {'message': 'Product removed'}, 200

    def __isValidPrice(self, args):
        return int(args['unitPrice']) >= 5

    def __isValidSize(self, args):
        return int(args['unitSize']) >= 1

