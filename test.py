import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"user_name": "bigmonkey123", "passwd": "monkeymonkey", "email": "monkey@hotmail.com"},
#         {"user_name": "123123", "passwd": "123123", "email": "123123@gmail.com"},
#         {"user_name": "321321", "passwd": "321321", "email": "321@gmail.com"}]

# for i in range(len(data)):
#     response = requests.put(BASE + "vpn/" + str(i), data=data[i])
#     print(response.json())

# response = requests.put(BASE + "vpn/0", {"user_name": "big)

input()
response = requests.patch(BASE + "vpn/2", {"user_name": "smallmonkey123", "passwd" : "smallmonkeymonkey", "email": "smallmonkey@hotmail.com"})
print(response.json())