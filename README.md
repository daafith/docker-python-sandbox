# Webservice
A simple python web service running in docker

## Start
Run `. start.sh` to start the service on port 1234, the initial start is without data.

### Populate
TODO

### Clean
Run `. clean.sh` to remove all data.

## API
```
GET /
```

Displays this README as HTML

```
GET /product/<identifier>
```

Returns the product linked to the identifier or returns a 404

```
POST /product/
```

Creates the product, BODY `{ "identifier": "product id", "name": "product name", "price": "product price" }`

```
GET /products/
```

Returns the list of registered products