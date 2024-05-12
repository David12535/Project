#The type of booleans is greater than, less than, equal to, less than or equal to, for example:
print(10 > 9)
print(10 == 9)
print(10 < 9)
print(5 != 10)
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


a=17000
b=8000
c=2.4
if b / a == c:
    print ("17000/8000=2.4")
else:
   print("you don't know math")


#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

x=2
x=2.5
print(bool(x))

x=0
print(bool(x))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool({})
bool([])


#Print "" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int))

y = "KH"
print(isinstance(y, int))