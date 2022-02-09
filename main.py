
#This is a code that simulates how an ATM behaves

def password_validate():
    pswd_1 = input("Please enter your password!\n")
    pswd_2 = input("Please confirm your password!\n")
    if pswd_1 != pswd_2:
        print("Your password does not match, please try again")
    else:
        print("welcome! What would you like to do?")
        choose = input('To WITHDRAW press 1\n'
              'To Confirm Account Balance press 2\n'
              'To Change PIN press 3\n'
              'To TRANSFER funds press 4\n')
        if choose.isdigit():
            choice = int(choose)
            if choice == 1:
                print("How much would you like to withdraw?\n")
            elif choice <= 0:
                print("Please choose one of the options 1, 2, 3 or 4")
            elif choice >= 5:
                print("Please choose one of the options 1, 2, 3 or 4")
        else:
            print("Please enter a digit. 1, 2, 3 or 4!")


password_validate()