#file handling

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents) # read the entire contents of the file and store it as one long string in contents.
    #hence str() is not needed here
''' The blank line appears because
read() returns an empty string when it reaches the end of the file; this empty
string shows up as a blank line'''

#remove the extra blank line you can use rstrip() in the print statement
with open('pi_digits.txt', 'r') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
you to read and write to the file ('r+')'''