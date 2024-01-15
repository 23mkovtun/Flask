import requests

response = requests.post(
    "http://127.0.0.1:5000/ads/",
    json={"header": "test1", "description": "test1", "owner": "test1"},
)
print(response.status_code)
print(response.text)

response = requests.get("http://127.0.0.1:5000/ads/1",)
print(response.status_code)
print(response.json())

# response = requests.post(
#     "http://127.0.0.1:5000/ads/",
#     json={"header": "test2", "description": "test2", "owner": "test2"},
# )
# print(response.status_code)
# print(response.text)

# response = requests.get("http://127.0.0.1:5000/ads/2",)
# print(response.status_code)
# print(response.json())

# response = requests.patch(
#     "http://127.0.0.1:5000/ads/2",
#     json={"header": "new_test2", "description": "new_test2", "owner": "new_test2"},
# )
# print(response.status_code)
# print(response.text)

# response = requests.get("http://127.0.0.1:5000/ads/2",)
# print(response.status_code)
# print(response.json())

# response = requests.delete("http://127.0.0.1:5000/ads/2",)
# print(response.status_code)
# print(response.json())
#
# response = requests.get("http://127.0.0.1:5000/ads/2",)
# print(response.status_code)
# print(response.json())
