#Python has two primitive loop commands:
#while loops
#for loops
#With the while loop we can execute a set of statements as long as a condition is true.
#Print i as long as i is less than 6:

i = 4
while i < 17:
  print(i)
  i += 1

"""The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
With the break statement we can stop the loop even if the while condition is true:
Exit the loop when i is 2:"""
i = 1
while i < 16:
  print(i)
  if i == 2:
    break
  i += 1

#With the continue statement we can stop the current iteration, and continue with the next:
#Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

"""With the else statement we can run a block of code once when the condition no longer is true:
Print a message once the condition is false:"""
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")






#Code
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

#output 
1
2
3
4
5








