balance = 10000
correct_pin = "8637"


def check_balance(balance):
    print("Your balance is Rs.", balance)


def deposit(balance):
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Money deposited successfully!")
        print("New balance: Rs.", balance)
    else:
        print("Enter a valid amount.")

    return balance

def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
    elif amount <= balance:
        balance = balance - amount
        print("Please collect your cash.")
        print("Remaining balance Rs:", balance)
    else:
        print("Insufficient Balance!!!")

    return balance


print("=" * 32)
print("     WELCOME TO ATM     ")
print("=" * 32)

pin = input("Enter your PIN: ")

if pin == correct_pin:
    print("\nLogin Successful!")

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance:")
        print("2. Deposit Money:")
        print("3. Withdraw Money:")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN! Access denied.")