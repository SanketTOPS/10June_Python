"""products=[
    {'pid':101,'pname':'mouse','price':[120,150]},
    {'pid':102,'pname':'keyboard','price':[200,250]},
    {'pid':103,'pname':'mobile','price':[5000,8000]},
    {'pid':104,'pname':'charger','price':[45,80]}
]

print(products)

for i in products:
    print(i['price'][0])"""


products={"pid":[101,102,103],
          "pname":["mouse","charger","keyboard"],
          "price":[120,80,230]}

#print(products)

for i,j in products.items():
    print(i,j[0])