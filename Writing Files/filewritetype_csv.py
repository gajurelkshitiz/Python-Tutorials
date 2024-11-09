import csv

employees = [["Name","Age","Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 32, "Unemployed"],
             ["Sandy", 24, "Manager"]]

file_path = "Writing Files/Output.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file,)
    for row in employees:
        writer.writerow(row)
    print(f"CSV file at {file_path} was successfully created.")