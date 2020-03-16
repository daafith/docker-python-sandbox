echo "------------------"
echo "inserting products"
echo "------------------"
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"identifier":"PR101","name":"Pringles","price":149}' \
  http://localhost:1234/product
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"identifier":"FI101","name":"Fire Balls","price":89}' \
  http://localhost:1234/product
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"identifier":"CC101","name":"Chocolate Chip Cookies","price":299}' \
  http://localhost:1234/product
