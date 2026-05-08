balance = 0.0
history = []

print("💰 Welcome to Python Bank! 💰")
print("You can deposit, withdraw, check balance and view history.")


while True:
    print("\n==== Main Menu ====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. View History")
    print("5. Quit")


    choice = input("\nEnter your choice (1 - 5): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print(f"✅ Successfully deposited ${amount}")
            history.append(f"Deposited ${amount}")
        else:
            print("⚠️ Deposit amount must be positive")


    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("⚠️ Withdrawal amount has to be greater than 0")

        elif amount > balance:
            print("❌ Insufficient fund!")

        else:
            balance = balance - amount
            print(f"✅ Successfully withdrew ${amount:.2f}")
            history.append(f"Withdrawn ${amount}")



    elif choice == "3":
        print(f"💰 Current balance: ${balance:.2f}")

    elif choice == "4":
        for h in history:
            print(h)

    elif choice == "5":
        print("Have a nice day!")
        break

    else:
        print("❌ Invalid choice. Please enter 1 - 5 only.")








