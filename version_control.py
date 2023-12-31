def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode_password(in_str):
    en_str = ''
    for i in range(0, (len(in_str))):
        indiv_char = int(in_str[i])
        indiv_char -= 3
        en_str += str(indiv_char)
    return en_str


while True:
    print('')
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encode_password(password)
        print("Your password has been encoded and stored!")

    elif choice == "2":
        print('')
        if 'encoded_password' in locals():
            print(f"The encoded password is {encoded_password}, and the original password is {decode_password(encoded_password)}.")
        else:
            print("No encoded password has been stored yet.")

    elif choice == "3":
        break

