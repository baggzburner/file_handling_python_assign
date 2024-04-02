def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, there Python\n")
            file.write("my book tells me you have 0 legs\n")
            file.write("Should i sell it to 3 other students with a 211IQ?.\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Access denied.")
    else:
        print("File created successfully.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Access denied.")
    else:
        print("File read successfully.")

def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Coding is a lifestyle.\n")
            file.write("which is 100% satisfactory\n")
            file.write("And of course a great career.\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Access denied.")
    else:
        print("Content appended successfully.")

def main():
    create_file()
    read_file()
    append_file()

if __name__ == "__main__":
    main()
