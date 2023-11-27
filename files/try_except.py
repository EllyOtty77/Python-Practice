# ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# FileNotFoundError exception
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# try-except-else
try:
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Handling the specific exception (ZeroDivisionError in this case)
    print("Cannot divide by zero!")
else:
    # Code to execute if the try block is successful
    print("Division successful. Result:", result)

# Count the approximate number of words in the file.
with open(filename, encoding='utf-8') as f:
    contents = f.read()
    words = contents.split()
