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
GET /product/<name>
```

Returns the product linked to the name

```
GET /product
```

Returns the list of registered products

```
POST /product
```

Creates the product, BODY `{ "name": "product name", "unitPrice": 1199, "unitSize": 1, "unitType": "ITEM" }`

```
PUT /product
```

Updates the product, BODY `{ "name": "product name", "unitPrice": 1299, "unitSize": 1, "unitType": "ITEM" }`

```
DELETE /product/<name>
```

Deletes the product linked to the name

### Test
Run `. test.sh` to run tests. Or you can use the Postman collection if you like that (bash is better though ;)).
