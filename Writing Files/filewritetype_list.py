
# Type 2 Practise

employees = ['Eugene', 'Squidward', 'Spongebob', 'Patrick']

file_path = "Writing Files/EmployeesList.txt"

with open(file=file_path, mode='w') as file:
    file.write("List of Employees:\n\n")
    for employee in employees:
        file.write(employee + "\n")
    print(f"File {file_path} was successfully created.")
    

