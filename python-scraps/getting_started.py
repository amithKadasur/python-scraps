# message = "Hello World!!!"
# print(message)
#
# message = "Hello World! We meet again"
# print(message)
#
# '''playing
# with strings'''
# # and comments
# print("\nstring manipulation".title())
# testingString = "all lowercase "
# print(testingString.title())
# print(testingString.upper())
# print(testingString.strip())
#
# # numbers
# '''best practice to get decimal(float) values is to have at least one value as 'float' (difference b/w py2 to py3)'''
# print("\ncrunching numbers".title())
# print(3/2)#in py3 it's 1.5 but in py2 it's 1(dec truncaded)
# print(3**3)#to the power of...
#
# #str()
# '''str()'''
# print("\ntype error demo".title())
# age = 30
# # print("Happy " + age + "th Birthday") #Error - TypeError: Can't convert 'int' object to str implicitly
# #solution
# print("Happy " + str(age) + "th Birthday")
#
# # The Zen of Python
# #import this


print("\n.............................................")
'''list'''
print("list".upper())
names_and_numbers = ['zeros', 000, 'ones', 111]
# print(namesAndNumbers)
print(names_and_numbers[2].title())

'''Negetive index'''
#access last element / second last element / etc...(sometimes we dont know the index of list)
print(names_and_numbers[-1])
print(names_and_numbers[-3])

'''list manipulation'''
names_and_numbers.append("appended element")
print(names_and_numbers)

'''insert()'''
names_and_numbers.insert(1, "inserted element")
print(names_and_numbers)

'''del'''
del names_and_numbers[0]
print(names_and_numbers)

# del namesAndNumbers
# print(namesAndNumbers)

'''pop()'''
popped_item = names_and_numbers.pop()
print("popped item is: " + popped_item)

'''pop() at given position'''
popped_at_any_position = names_and_numbers.pop(1)
print("value of popped item at '1' position: " + str(popped_at_any_position)) #handling non string object (this is the problem with lists!!!!)

'''NOTE abt pop() and del'''
# when you want to delete an item from a list
# and not use that item in any way, use the del statement; if you want to use an
# item as you remove it, use the pop() method

'''remove() item by value'''
removed_item = 111
names_and_numbers.remove(111)
print(str(removed_item) + " is removed from " + str(names_and_numbers))
print(names_and_numbers)
'''NOTE abt remove()'''
# The remove() method deletes only the first occurrence of the value you specify. If there’s
# a possibility the value appears more than once in the list, you’ll need to use a loop to
# determine if all occurrences of the value have been removed
