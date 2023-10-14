files_number = int(input("How many files created: "))
operations = {'W': "write", 'X': "execute", 'R': "read"}
files = dict()
operations_input = dict()

# Getting input files
for _ in range(files_number):
    key_value = input("File name and rights: ")

    key_value_splitted = key_value.split(' ')
    files[key_value_splitted[0]] = key_value_splitted[1:4]

operations_numbers = int(input("How many operations will be completed: "))

# Getting input operations
for _ in range(operations_numbers):
    operation_file = input("Which operation and file: ")
    key_value_splitted = operation_file.split(' ')
    key = ''
    value = ''

    match (len(key_value_splitted)):
        case 2:
            key = key_value_splitted[1]
            value = key_value_splitted[0]
        case 3:
            key = key_value_splitted[2]
            value = key_value_splitted[0] + ' ' + key_value_splitted[1]
        case 4:
            key = key_value_splitted[3]
            value = key_value_splitted[0] + ' ' + key_value_splitted[1] + ' ' + key_value_splitted[2]
        case _:
            print("Too many arguments")

    current_rights = ''

    # Comparing and setting correct operations
    for k, v in operations.items():
        values = value.split(' ')

        if v in values:
            current_rights += k

    operations_input[key] = current_rights

# Comparing both inputs
for k, v in operations_input.items():
    counter = 0

    for vv in files[k]:
        for vvv in vv:
            counter += 1 if vvv in vv else 0

    print("OK" if counter == len(v) else "Access denied")
# a = {}
# b = {"W": "запись", "R": "чтение", "X": "запуск"}
# for i in range(int(input())):
#     file = input().split()
#     a[file[0]] = [b[i] for i in file[1::]]
#
# for i in range(int(input())):
#     c = input().split()
#     print("OK" if c[0] in a[c[1]] else "Access denied.")

a = """First, we pulled data from the data.txt file using the genfromtxt function. In this function we need to specify the file to be read, and then the delimiter - so that NumPy understands where numbers begin and end. In our case, the separator will be ,.

Then we need to convert the numbers to the int32 format using the astype function, passing the type we need into it.

Boolean expressions. Another feature of NumPy is Boolean expressions for array elements. They allow you to find out which elements meet certain conditions - for example, whether each array number is greater than 50.

Suppose we have an array a and we want to check if all its elements are greater than 5:

Translated with www.DeepL.com/Translator (free version)"""
