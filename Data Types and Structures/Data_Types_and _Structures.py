import random

# 1. Create a string with your name and print it
name = "Kiran"
print("Q1:", name)

# 2. Find the length of the string "Hello World"
text = "Hello World"
print("Q2:", len(text))

# 3. Slice the first 3 characters from "Python Programming"
text = "Python Programming"
print("Q3:", text[:3])

# 4. Convert the string "hello" to uppercase
text = "hello"
print("Q4:", text.upper())

# 5. Replace "apple" with "orange"
text = "I like apple"
print("Q5:", text.replace("apple", "orange"))

# 6. Create a list with numbers 1 to 5
numbers = [1, 2, 3, 4, 5]
print("Q6:", numbers)

# 7. Append number 10 to the list
numbers = [1, 2, 3, 4]
numbers.append(10)
print("Q7:", numbers)

# 8. Remove number 3 from list
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print("Q8:", numbers)

# 9. Access second element in list
letters = ['a', 'b', 'c', 'd']
print("Q9:", letters[1])

# 10. Reverse a list
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print("Q10:", numbers)

# 11. Create a tuple
t = (100, 200, 300)
print("Q11:", t)

# 12. Access second-to-last element of tuple
colors = ('red', 'green', 'blue', 'yellow')
print("Q12:", colors[-2])

# 13. Find minimum number in tuple
t = (10, 20, 5, 15)
print("Q13:", min(t))

# 14. Find index of "cat"
animals = ('dog', 'cat', 'rabbit')
print("Q14:", animals.index("cat"))

# 15. Check if "kiwi" is in tuple
fruits = ("apple", "banana", "mango")
print("Q15:", "kiwi" in fruits)

# 16. Create a set
s = {'a', 'b', 'c'}
print("Q16:", s)

# 17. Clear all elements from set
s = {1, 2, 3, 4, 5}
s.clear()
print("Q17:", s)

# 18. Remove element 4 from set
s = {1, 2, 3, 4}
s.remove(4)
print("Q18:", s)

# 19. Union of two sets
a = {1, 2, 3}
b = {3, 4, 5}
print("Q19:", a.union(b))

# 20. Intersection of two sets
a = {1, 2, 3}
b = {2, 3, 4}
print("Q20:", a.intersection(b))

# 21. Create dictionary
person = {"name": "John", "age": 25, "city": "New York"}
print("Q21:", person)

# 22. Add key-value pair
person = {'name': 'John', 'age': 25}
person["country"] = "USA"
print("Q22:", person)

# 23. Access value of "name"
person = {'name': 'Alice', 'age': 30}
print("Q23:", person["name"])

# 24. Remove key "age"
person = {'name': 'Bob', 'age': 22, 'city': 'New York'}
person.pop("age")
print("Q24:", person)

# 25. Check if "city" exists
person = {'name': 'Alice', 'city': 'Paris'}
print("Q25:", "city" in person)

# 26. Create list, tuple and dictionary

my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_dict = {"a": 1, "b": 2}

print("Q26 List:", my_list)
print("Q26 Tuple:", my_tuple)
print("Q26 Dictionary:", my_dict)

# 27. List of 5 random numbers and sort
numbers = [random.randint(1, 100) for i in range(5)]
numbers.sort()
print("Q27:", numbers)

# 28. Print element at third index
words = ["apple", "banana", "cherry", "mango", "grape"]
print("Q28:", words[3])

# 29. Combine two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print("Q29:", d1)

# 30. Convert list of strings into a set
words = ["apple", "banana", "apple", "orange"]
s = set(words)
print("Q30:", s)