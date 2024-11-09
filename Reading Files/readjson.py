import json

file_path = "Writing Files/Employee.json"

with open(file_path, 'r') as file:
    content = json.load(file)
    print(content)
    