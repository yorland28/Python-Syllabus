# Boolean
print("\nBoolean")
flag = False
print(flag)
flag = True
print(flag)

# String
print("\nString")
print('Who said "to be or not to be"?')
print("DNA goes from 5' to 3'.")
print("\"That's not fair!\" yelled my sister.")
# use "r" to disable special symbols like \
print(r"\"That's not fair !\" yelled my sister.")

# Numeric
print("\nNumber")
numbers = [123, 1.5, -1.23, 1.23E45, 0x7b, 12+3*5, 2147483648]
for number in numbers:
    print(number, " : ", type(number))

# List
# list[init:End-1]
print("\nList")
numbers_list = [0, 1, 2, 3]
print(numbers_list[1:3])


# Tuple
print("\nDuple")
data = (1, 2, 3, 4)
print(data[0])
# You can't change the duple value
# data[0] = 0
print("The value didn't change, always will be: ", data[0])

# Dictionary
print("\nDictionary")
d = {"name": "Yorland", "lastName": "Garcia"}
print(d["name"])
print(d.keys())
print(d.items())