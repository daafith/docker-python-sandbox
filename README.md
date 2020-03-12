# Webservice
A simple python web service running in docker

## Start
Run `. start.sh` to have a clean start of the service without data on port 1234.

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