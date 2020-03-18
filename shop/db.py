from flask import g
import shelve
import enum 

class Collection(enum.Enum): 
    products = "products.db"
    inventory = "inventory.db"

def get_db(Collection):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open(Collection.value)
    return db