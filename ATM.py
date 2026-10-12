# ATM

# Write a program that simulates an ATM withdrawal.

# Ask the user to enter their PIN.
# Allow a maximum of 3 PIN attempts.

# The program should accept the withdrawal amount.
# A withdrawal should only be allowed if:
# - The withdrawal amount is greater than 0.
# - The withdrawal amount does not exceed the account balance.
# - At least ₹500 must remain in the account after the withdrawal.

# The program should display whether the withdrawal was successful
# and the remaining balance.


accountBalance = 15000

pin = 1234

correctPin = False

for i in range(3):# range shifted to 3 from 2 because we want 3 wrong attempts

    userPin = int(input("Enter PIN:"))# ADDED int and () because we want to convert the input to an integer and also to take input from the user

    if userPin == pin:
        correctPin = True
        break

    else:
        if i < 2:
           print("Incorrect PIN, try again")

        else:
            print("3 attempts failed")

if correctPin == True:
    amount = int(input("Enter The Withdrawal Amount:"))

    if amount <= 0:# changed <  to <= because we want to check for 0 as well                
        print("Please enter a value greater than 0")

    else:

        if amount == accountBalance:
            print("Amount is equal to Account Balance") 

        elif amount > accountBalance:
            print("Amount is greater than Account Balance")

        else:
            if (accountBalance - amount) < 500:# changed <= to < because we want to check for 500 as well
                print("Account Balance can't be less than 500")

            else:
                
                print(f"Amount Withdrawal: {amount}")
                accountBalance = accountBalance - amount #shifted + to - because we want to deduct the amount from the account balance
                print(f"Balance:{accountBalance}")

else:
    print("3 Attempts Failed")