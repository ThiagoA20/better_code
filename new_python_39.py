"""
------------- merge dictionary -------------

<= 3.8:
dict1 = {'a': 10, 'b': 20}
dict2 = {'a': 50, 'c': 30}
dict3 = {**dict1, **dict2}
print(dict3)

>= 3.9:
dict1 = {'a': 10, 'b': 20}
dict2 = {'a': 50, 'c': 30}
dict3 = dict1 | dict2
print(dict3)

------------- remove prefix and sufix -------------

my_string = "Hello World"
print(my_string.removeprefix("Hello "))
print(my_string.removesuffix(" World"))

------------- Type hinting for collections -------------

my_int: int = 10
print(my_int)
my_collection: list[int] = [1, 2, 3, 4, 5]
"""
