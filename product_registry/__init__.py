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

api.add_resource(ProductList, '/products')