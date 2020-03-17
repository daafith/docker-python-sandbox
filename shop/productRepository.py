from .db import Collection, get_db

class ProductRepository:
    def __init__(self):
        self.db = get_db(Collection.products)
    
    def hasItem(self, name):
        if name in self.db:
            return True
        return False

    def get(self, name):
        if not self.hasItem(name):
            return None
        return self.db[name]

    def all(self):
        keys = list(self.db.keys())
        ps = []
        for key in keys:
            ps.append(self.db[key])
        return ps

    def save(self, product):
        self.db[product['name']] = product

    def update(self, product):
        self.db[product['name']] = product

    def remove(self, name):
        del self.db[name]
