file_path = "Writing Files/EmployeesList.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("That FileName was not found.")