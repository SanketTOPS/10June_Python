import requests

url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()
print(data)

"""pid=int(input("Enter a product ID:"))

for i in data:
    if i["id"]==pid:
        print(f"ID:{i["id"]}")
        print(f"Product Name:{i["title"]}")
        print(f"Price:{i["price"]}")"""




"""for i in data:
    print(f"ID:{i["id"]}")
    print(f"Product Name:{i["title"]}")
    print(f"Price:{i["price"]}")
    print("-----------------------")"""
