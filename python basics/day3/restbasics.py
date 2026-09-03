import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"Name: {user['name']}, Email: {user['email']}")

print(response.status_code)
print(response.json())

data = {
    "name": "Prakhar",
    "username": "prakhar123",
    "email": "prakhar@example.com"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print(response.json())



# try catch error handling
try:
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    users = response.json()

    print(users)

except requests.exceptions.RequestException as e:
    print("API error:", e)
