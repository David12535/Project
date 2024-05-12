#There are three numeric types in Python:

int
float
complex
#Variables of numeric types are created when you assign a value to them, for example:
num1 = 1 #int
num2 = 1.6 #float
num3 = 15j #complex

#To verify the type of any object in Python, use the type() function, for example:
print(type(num1))
print(type(num2))
print(type(num3))

#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
num4 = -152787979
num5 = 87
num6 = -81
print(type(num4))
print(type(num5))
print(type(num6))

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
num7 = 7.12
num8 = 4.0
num9 = -35.59

print(type(num7))
print(type(num8))
print(type(num9))

#Float can also be scientific numbers with an "e" to indicate the power of 10.
num10 = 5e3
num11 = 6E6
num12 = -67.5e100

print(type(num10))
print(type(num11))
print(type(num12))

#Complex numbers are written with a "j" as the imaginary part:
num13 = 3+5j
num14 = 5j
num15 = -5j

print(type(num13))
print(type(num14))
print(type(num15))

#You can convert from one type to another with the int(), float(), and complex() methods:

num16 = 1    # int
num17 = 2.8  # float
num18 = 1j   # complex

#convert from int to float:
a = float(num16)

#convert from float to int:
b = int(num17)

#convert from int to complex:
c = complex(num18)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))