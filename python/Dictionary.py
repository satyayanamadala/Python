dict = {"name":"satya","age":19,"list":[2,3,4,5,6],0:"CSE"}
print(dict)
print(dict["name"])
print(dict["list"])

#Dictionary Methods
print(dict.items())
print(dict.values())
print(dict.keys())
print(dict.get("name")) # the difference between get and  print(dict["name"]) is in get function if the key is incorrect then it will print none whereas in print(dict["name"]) its shows error thats the only diff.

dict.update({"age":20, "section":"AI1"})
print(dict)

copy_dict = dict.copy()
print(copy_dict)

print(dict.pop("name"))
print(dict)

print(dict.clear())
