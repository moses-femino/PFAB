my_string = "I said hey, wassup, hello."
empty = ""

for letter in my_string:
    if letter .isalnum() or letter .isspace() or letter == "'" or letter == "-":
        empty += letter

    print(empty.split())
    print(len(empty))


