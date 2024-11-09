# Python writing files (.txt, .json, .csv)


# Type-1 Practise:

txt_data = "I am continuosly learning it from past 20 days."

file_path = "Writing Files/output.txt"

try:
    with open(file=file_path , mode="a") as file:
        file.write(" " + txt_data)
        print(f"File {file_path} was created.")
        
except FileExistsError:
    print("That file already exists.")



