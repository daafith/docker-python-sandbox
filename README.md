# Webservice
A simple python web service running in docker

## Start
Run `. start.sh` to start the service on port 1234, the initial start is without data.

### Populate
Run `. populate.sh` to insert some data.

### Clean
Run `. clean.sh` to remove all data.

## API
The options so far.

```
GET /
```

Displays this README as HTML

### Product

```
GET /product/<identifier>
```

Returns the product linked to the identifier

```
POST /product/
```

Creates the product, BODY `{ "identifier": "product id", "name": "product name", "price": 1199 }`

```
PUT /product/
```

Updates the product, BODY `{ "identifier": "product id", "name": "product name", "price": 1299 }`

```
DELETE /product/<identifier>
```

Deletes the product linked to the identifier

```
GET /products/
```

Returns the list of registered products