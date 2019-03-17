# Created by Yoland Garcia


# This is a comments
print("""You can write  # one line
multiple lines          # Second Line
here                    #Third """)     # This comment is outside of string
print('\nyou can use this symbol', ' \",\" to separate two operations in a print statement and this' +
      ' \"+\" to sum variables and add string')
print("you can use this symbol \""" or this \' to contain a string")
print("you can add a newline with \\n")

# Variables in Python
variable_name = "Use \"_\" separate to variables words"
print(variable_name + " like this:  variable_name")
days_name = ['Monday', 'Tuesday', 'Wednesdays', 'thursday', 'Friday', 'Saturday']
print("\nThis a array: " + days_name[0] + days_name[1])
print("\nYou can use a variable to store any value")
variable = 'first value'
print(type(variable))
variable = 2
print(type(variable))
variable = 0.5
print(type(variable))


# keywords
key_words = """False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise """
print("\nThis is a keyword: ", "else" in key_words)


# Indentation
# Python doesn't need ";" at the line end
# Use : when you have to implement a function and statements
if variable != 0:
    print("\nvariable != 0 : ", variable)


# You have to defined the function first to be able to used it later
def loop(days):
    for day in days:
        print(day)


print("\nThis a loop")
# Here we call to the function already defined
loop(days_name)
