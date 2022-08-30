from json import load


with open("bikes.json") as f:
    data=load(f)
print(data)


bike_names=[bike.get("name") for bike in data]
print(bike_names)

costly_bike=max(data,key=lambda b:b.get("price"))
print(costly_bike)

red_bikes=[bike.get]
