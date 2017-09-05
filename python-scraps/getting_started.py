message = "Hello World!!!"
print(message)

message = "Hello World! We meet again"
print(message)

'''playing 
with strings'''
# and comments
print("\nstring manipulation".title())
testingString = "all lowercase "
print(testingString.title())
print(testingString.upper())
print(testingString.strip())

# numbers
'''best practice to get decimal(float) values is to have at least one value as 'float' (difference b/w py2 to py3)'''
print("\ncrunching numbers".title())
print(3/2)#in py3 it's 1.5 but in py2 it's 1(dec truncaded)
print(3**3)#to the power of...

#str()
'''str()'''
print("\ntype error demo".title())
age = 30
# print("Happy " + age + "th Birthday") #Error - TypeError: Can't convert 'int' object to str implicitly
#solution
print("Happy " + str(age) + "th Birthday")

# The Zen of Python
#import this


print("\n.............................................")
# list
print("list".upper())
namesAndNumbers = ['zeros', 000, 'ones', 111]
print(namesAndNumbers)
