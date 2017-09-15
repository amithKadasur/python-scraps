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
emptying_the_list = ["hi", "bye"]
del emptying_the_list[1]
del emptying_the_list[0]
print("empty list: "+ str(emptying_the_list))
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

'''sorting'''
sort_this_list = ["one", "two", "three", "four"]
print("original list to sort: " + str(sort_this_list))
sort_this_list.sort()
print("asc sorted list: "+ str(sort_this_list))

#in reverse order
sort_this_list = ["one", "two", "three", "four"]
print("original list to sort: " + str(sort_this_list))
sort_this_list.sort(reverse=True)
print("desc reversed sorted list: "+ str(sort_this_list))

#temp sort the list
sort_this_list = ["one", "two", "three", "four"]
print("original list to sort: " + str(sort_this_list))
print("temp sorted list" + str(sorted(sort_this_list)))
print("temp sorted desc reverse list" + str(sorted(sort_this_list, reverse=True)))
print("original list after temp sort: " + str(sort_this_list))

#printing a list in reverse order (not desc or asc)
sort_this_list = ["one", "two", "three", "four"]
print("original list to sort: " + str(sort_this_list))
sort_this_list.reverse()
print("reversed unsorted list: " + str(sort_this_list))

#length of a list
sort_this_list = ["one", "two", "three", "four"]
print("original list to sort: " + str(sort_this_list))
print("length of the list: " + str(len(sort_this_list)))
print("last item of the list: " + sort_this_list[-1])

'''slice'''
# Don’t worry about the details in this example for now. Basically, if you’re trying to
# work with a copy of a list and you see unexpected behavior, make sure you are copying
# the list using a slice, as we did in the first example.

my_foods = ["dal", "rice", "koorma"]
friend_foods = my_foods  #to connect the new variable friend_foods to the list that is already contained in
                        # my_foods, so now both variables point to the same list
friend_foods.append("bhindi")
print(friend_foods)
print(my_foods)

friend_foods = my_foods[:] #use slice to copy list
friend_foods.append("masala")
print(friend_foods)
print(my_foods)

'''loops'''
greetings = ["hello", "hi", "hallo", "namaskar"]
for greeting in greetings:
    if greeting == "namaskar":
        print(greeting.title())
    else:
        print(greeting)