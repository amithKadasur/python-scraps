# using try-except blocks

# print(5/0)

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# multiple files
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")


silent_fail_filenames = ['alice.txt', 'pi_digits.txt', 'moby_dick.txt', 'little_women.txt']
for filename in silent_fail_filenames:
    count_words(filename)

print('\n\n\n')


# failing silently
def count_words(filename):
       """Count the approximate number of words in a file."""
       try:
           with open(filename) as f_obj:
               contents = f_obj.read()
       except FileNotFoundError:
           pass
       else:
           # Count approximate number of words in the file.
           words = contents.split()
           num_words = len(words)
           print("The file " + filename + " has about " + str(num_words) + " words.")

silent_fail_filenames = ['alice.txt', 'pi_digits.txt', 'moby_dick.txt', 'little_women.txt']
print('failing silently')
for filename in silent_fail_filenames:
    count_words(filename)
