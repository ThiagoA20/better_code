"""
List comprehension é mais rápido do que .append()
"""

fruits = ["banana", "maçâ", "uva", "melancia", "abacate"]
fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

bits = [False, True, True, False, False, False, True, False]
bits = [0 if bit == False else 1 for bit in bits]
# print(bits)

name = "HelloMyNameIsThiago"
name = "".join(
    [palavra if palavra.islower() else " " + palavra.lower() if palavra in ["N", "I"] else " " + palavra for palavra in name]
)[1:]
print(name)