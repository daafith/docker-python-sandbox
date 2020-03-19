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
    echo "$2" TEST FAIL, result is 
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

echo
echo "------------------"
echo "Testing GET"
echo "------------------"
echo 

succesGet=$(curl --request GET http://localhost:1234/product/Sponges)

echo 
validate "$succesPost" "Product registered"
validate "$failPostConflict" "Product already exists"
validate "$succesGet" "Product found"

echo 
echo Test Summary:
echo "$testOK" Test Passed 
echo "$testFAIL" Test Failed