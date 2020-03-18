echo "------------------"
echo "inserting products"
echo "------------------"
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Pringles","unitPrice":149,"unitSize":1,"unitType":"ITEM"}' \
  http://localhost:1234/product
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Fire Balls","unitPrice":89,"unitSize":1,"unitType":"ITEM"}' \
  http://localhost:1234/product
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Chocolate Chip Cookies","unitPrice":299,"unitSize":1,"unitType":"ITEM"}' \
  http://localhost:1234/product
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Bananas","unitPrice":119,"unitSize":500,"unitType":"GRAM"}' \
  http://localhost:1234/product
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Energyless Drink","unitPrice":119,"unitSize":750,"unitType":"MILLILITER"}' \
  http://localhost:1234/product

