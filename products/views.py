# from products.models import bikes
#
# class Bikes:
#     def list(self,*args,**kwargs):
#         return bikes
#     def retrieve(self,*args,**kwargs):
#         code=kwargs.get("code")
#         bike=[b for b in bikes if b.get("code")==code]
#         return bike
#     def create(self,*args,**kwargs):
#         bike=kwargs.get("data")
#         bikes.append(bike)
#         return bike
#     def update(self,*args,**kwargs):
#         code=kwargs.get("code")
#         data=kwargs.get("data")
#         instance=[b for b in bikes if b.get("code")==code][0]
#         instance.update(data)
#         return instance
#     def destroy(self,):
#         code=kwargs.get("code")
#         instance=[b for b in bikes if b.get("code")==code][0]
#         bikes.remove(instance)
#         return instance


# b=Bikes()
# print(b.retrieve(code=1003))
# data={"code":1006,"name":"ray",
#       "colors":["red","white"],
#       "price":200000,"brand":"yamaha",
#       "fuel_type":"petrol"},
# print(b.retrieve(code=1002))


# data={"code":1002,"name":"hynes","colors":["red","blue","black","grey","white"],"price":260000,"brand":"honda","fuel_type":"petrol"}
# print(b.update(code=1002,data=data))
# print(b.destroy(code=1002))




