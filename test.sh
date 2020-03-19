echo
echo "------------------"
echo "Removing data"
echo "------------------"
. clean.sh
echo
echo "------------------"
echo "Testing POST"
echo "------------------"
echo 

testOK=0
testFAIL=0

addToOK() {
  ((testOK=testOK+1))
}

addToFail() {
  ((testFAIL=testFAIL+1))
}

validate() {
  if [[ "$1" == *"$2"* ]]; then
    echo "$2" TEST OK
    addToOK
    else
    echo "$2" TEST FAIL, the actual result is 
    echo "$1"
    addToFail
  fi
}

succesPost=$(curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Sponges","unitPrice":99,"unitSize":8,"unitType":"ITEM"}' \
  http://localhost:1234/product)

failPostConflict=$(curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Sponges","unitPrice":99,"unitSize":8,"unitType":"ITEM"}' \
  http://localhost:1234/product)

failPostWrongPrice=$(curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Foobar","unitPrice":4,"unitSize":8,"unitType":"ITEM"}' \
  http://localhost:1234/product)

failPostWrongSize=$(curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Foobar","unitPrice":55,"unitSize":0,"unitType":"ITEM"}' \
  http://localhost:1234/product)

failPostWrongItemType=$(curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Foobar","unitPrice":55,"unitSize":23,"unitType":"BOX"}' \
  http://localhost:1234/product)

failPostMissingParam=$(curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Foobar","unitPrice":55,"unitSize":30}' \
  http://localhost:1234/product)

echo
echo "------------------"
echo "Testing GET"
echo "------------------"
echo 

succesGet=$(curl --request GET http://localhost:1234/product/Sponges)
succesGetAll=$(curl --request GET http://localhost:1234/product)

echo 
validate "$succesPost" "Product registered"
validate "$failPostConflict" "Product already exists"
validate "$failPostWrongPrice" "Price must be 5 or higher"
validate "$failPostWrongSize" "Size must be 1 or higher"
validate "$failPostWrongItemType" "\"unitType\": \"BOX is not a valid choice"
validate "$failPostMissingParam" "\"unitType\": \"Missing required parameter"
validate "$succesGet" "Product found"
validate "$succesGetAll" "1 Product(s) found"

echo 
echo Test Summary:
echo "$testOK" Test Passed 
echo "$testFAIL" Test Failed