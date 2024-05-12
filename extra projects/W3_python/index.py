'''A data structure is a way to organize and store data that enables efficient access and modification. Lists are a type of data structure 
that store a collection of heterogeneous items and are inbuilt data structures. Python also provides many functions or methods that you can use
 to work with lists.'''


'''In this tutorial, you will learn about the Python index() function. The index() method searches
 an element in the list and returns its position/index. First, this tutorial will introduce you to lists, 
 and then you will see some simple examples to work with the index() function.'''
name = ["gega", "luka", "David", "data"]
print(name[2])
print(name[1])
print(name[0])
print(name[3])
#What is Indexing in Python?
'''In Python, indexing refers to the process of accessing a specific element in a sequence, such as a string or list, using its position or
index number. Indexing in Python starts at 0, which means that the first element in a sequence has an index of 0, the second element has 
an index of 1, and so on. For example, if we have a string "Hello", we can access the first letter "H" using its index 0 by using the square 
bracket notation: string[0].'''


'''Python's built-in index() function is a useful tool for finding the index of a specific element in a sequence. 
This function takes an argument representing the value to search for and returns the index of the first occurrence of that value in the sequence.'''

'''If the value is not found in the sequence, the function raises a ValueError. For example, if we have a list [1, 2, 3, 4, 5], 
we can find the index of the value 3 by calling list.index(3), which will return the value 2 (since 3 is the third element in the list,
and indexing starts at 0).'''

'''The index() function is a powerful tool in Python as it simplifies the process of finding the index of an element in a sequence,
eliminating the need for writing loops or conditional statements. This function is especially useful when working with large datasets or complex
 structures, where manual searching could be time-consuming and error-prone.'''