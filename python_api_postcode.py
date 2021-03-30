# API for postcode

import requests

url = "http://api.postcodes.io/postcodes/"
postcode = "b421qr"

url_arg = url + postcode
print(url_arg)

response = requests.get(url_arg)

print(response.status_code)
response_dict = response.json()
response_keys = response_dict['result']

for items in response_keys.keys():
    if items == "postcode":
        print("Your Postcode location is " + str(response_keys["postcode"]))
    if items == "longitude":
        print("Your Longitude location is " + str(response_keys["longitude"]))

for keys in response_dict.keys():
    print(keys)

#print(type(response_dict))
# print(response.headers)
# print(response.content)
# print(response.cookies)
# print(response.encoding.isdigit())
