# basic input and output
name = str(input("What is your name? "))
print("This is your name: ", name, type(name))

number = int(input("What is your favorite number? "))
multiple = number * 2
print("This is your number (int): ", number, type(number))

number = float(number)
div = number / 3
print("This is your number (float): ", number, type(number))

number = str(number)
print("This is your number (str): ", number, type(number))

# Output with end= and sep= arguments
print("\n" + name, int(float(number)), sep="@", end=".com")