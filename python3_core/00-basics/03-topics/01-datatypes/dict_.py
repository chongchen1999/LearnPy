my_dict = {"name": "Alice", "age": 25, "city": "New York", 123: 456}
print(type(my_dict))
print(type(my_dict.items()))


for key, value in my_dict.items():
    print(key, value)

for temp in my_dict:
    print(type(temp))

for temp in my_dict.items():
    print(type(temp))