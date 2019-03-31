# numeric operators

# Operators Priority
# P   Parentheses, then ()
# E   Exponents, then (**)
# MD  Multiplication and division, left to right, then (* /  //)
# AS  Addition and subtraction, left to right (+ -)

print ("This is the priority order, from highest to lessest: () ,", "** ,", "// ,", "%  *  / (Left to right) ,",
       "+ - (Left to right)")
print ("\n (2+5) + 2*3/3 ** 2 = ")
print("\n 7 + 6 / 9")
print("\n 7 + 0.67")
print("\n =", (2+5) + 2*3/3 ** 2)

# From left to right
print("\n 2 ** 2 ** 3 =", 2 ** 2 ** 3)


print("\n 2 ** 3 = ", 2 ** 3)
print("\n 2. ** 3. =", 2. ** 3.)
print("\n 2. * 3. =", 2. * 3.)

# Boolean operators
print("Binary Operators:", "<, >, >=, <=, !=, ==, and, or, not")
print("The run order is from left to right 5 > 4 and 5 == 6 or 5 > 4) :", 5 > 4 and 5 == 6 or 5 > 4)
print("The other way round 5 > 4 or 5 > 6 and 5 == 6: ", 5 > 4 or 5 > 6 and 5 == 6)

# String Operators
print("\n(String +)", "String1" + "String2")
print("\n(String *)", "String" * 2)

# Bitwise operators
# Binary Ones Complement
print("\n(~): It's the like NOT logical but in bytes. ~12 (00001100) = ", ~12, "(11110011)")
# Binary AND
print("\n(&): It's the like AND logical but in bytes. 12 (00001100) & 13 (00001101) = ", 12 & 13, "(00001100)")
# Binary OR
print("\n(|): It's the like OR logical but in bytes. 12 (00001100) & 13 (00001101) = ", 12 | 13, "(00001101)")
# Binary XOR
print("\n(^): XOR. 12 (00001100) & 13 (00001101) = ", 12 ^ 13, "(00000001)")
# Binary Left Shift
print("\n(<<): x << y, In this case it's added 0*y in the right side and the zeros before are ignored."
      " 10 (0000 1010) << 2 = 40 (0010 1000)")
# Binary right Shift
print("\n(>>): x >> y, In this case it's deleted bits*y of the right side. 10 (0000 1010) >> 2 = ", 10 >> 2,
      "(0000 0010)")
