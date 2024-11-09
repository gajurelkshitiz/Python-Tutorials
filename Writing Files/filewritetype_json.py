
# Type-3 Practise

'''

import json

employee = {
    "name" : "Spoongebob",
    "age" : 30,
    "job" : "cook"
}

file_path = "Writing Files/Employee.json"

with open(file_path, "w") as file:
    json.dump(employee, file)
    print(f"Json file at {file_path} was created.")

'''



import json

employee_detail =  {
        "firstName" : "Joe",
        "lastName" : "Jackson",
        "gender" : "male",
        "age" : 28,
        "address" :{
            "streetAddress" : "101",
            "city" : "San Diego",
            "state" : "CA"
        },
        "phoneNumbers" : [
            {"type" : "home", "number" : "7349282382"}
        ]
    }


file_path = "Writing Files/Details.json"

with open(file_path, "w") as file:
    json.dump(employee_detail, file, indent= 5)
    print(f"Json file at location {file_path} was created sucessfully.")