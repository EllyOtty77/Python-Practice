# Reading from a file
file_path = "C:/Users/Eliud/Documents/GitHub/product_mart/workbench.txt"
with open(file_path) as file_object:
    for line in file_object:
        print(line)

    # Making a list of lines

    # lines = file_object.readlines()
    # for line in lines:
    #     print(line.rstrip())

# Writing to a file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    # multiple
    file_object.write("\nI love creating new games.")

# Append
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")