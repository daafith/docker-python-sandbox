from flask import Flask, g
import markdown
import os
from flask_restful import Api
from .product import Product

app = Flask(__name__)

api = Api(app)

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

product_routes = [
    '/product',
    '/product/<string:name>'
]

api.add_resource(Product, *product_routes)
