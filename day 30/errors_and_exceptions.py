# Erros and exceptions

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key2"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} doesn't exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    