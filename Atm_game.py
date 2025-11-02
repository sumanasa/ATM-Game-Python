#ATM Simulation Game

# initial balance
balance = 1000

def check_balance():
    """Display the current balance"""
    print(f" Your current balance is: ₹{balance}")

def deposit():
    """Deposit money into the account"""
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f" ₹{amount} deposited successfully!")
    else:
        print(" Invalid amount!")

def withdraw():
    """Withdraw money from the account"""
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount > balance:
        print(" Insufficient balance!")
    elif amount <= 0:
        print(" Invalid amount!")
    else:
        balance -= amount
        print(f" ₹{amount} withdrawn successfully!")

def atm_menu():
    """Main menu for the ATM"""
    print("\n Welcome to Python Bank ATM ")
    print("1️ Check Balance")
    print("2️ Deposit Money")
    print("3️ Withdraw Money")
    print("4️ Exit")

# Main game loop
while True:
    atm_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using Python Bank ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1-4.")
