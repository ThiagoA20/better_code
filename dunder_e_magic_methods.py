##################################################################### Deletar objeto

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __del__(self):
#         print("Object is being deconstructed!")


# p = Person("Mike", 25)

##################################################################### Somar com outra coisa

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

# v1 = Vector(10, 20)
# v2 = Vector(50, 60)
# v3 = v1 + v2

# print(v3.x)
# print(v3.y)

##################################################################### Calling the object

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __call__(self):
#         print("Hello, I was called!")

# v1 = Vector(12, 15)
# v1()

##################################################################### Aplying built in functions like len

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __len__(self):
#         return 10

# v1 = Vector(19, 42)
# print(len(v1))