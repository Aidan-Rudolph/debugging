def encode(password):
    result = ""
    for i in range(0, 7):
        result += str(int(password[i]) + 3)
    return result


def decode(password):
    result = ""
    for i in range(0, 7):
        result += str(int(password[i]) - 3)
    return result


pw = ""

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    menu = input("\nPlease enter an option: ")

    if menu == "1":
        pw = encode(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!")
    elif menu == "2":
        print("The encoded password is " + pw + ", and the original password is " + decode(pw))
    else:
        quit()
