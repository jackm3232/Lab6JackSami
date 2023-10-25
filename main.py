def encode(password):

    encoded_password = ""
    for i in password:
        if int(i) in range(0, 7):
            encoded_password += str(int(i) + 3)
        elif int(i) == 7:
            encoded_password += "0"
        elif int(i) == 8:
            encoded_password += "1"
        elif int(i) == 9:
            encoded_password += "2"

    return encoded_password


# Define and write decode function here

if __name__ == "__main__":
    loop = True
    while loop is True:
        print("Menu")
        print("-" * 13)
        print("1. Encode\n2. Decode\n3. Quit\n")
        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        # elif user_input == 2:
            # Call decode function here

        elif user_input == 3:
            loop = False
