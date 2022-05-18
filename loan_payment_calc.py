# Get the loan details
money_owed = float(input("How much money do you owe, in dollars?\n")) # $50,000
apr = float(input("What is the annual percentage rate?\n")) # 3%
payment = float(input("What will your  monthly payment be in dollars?\n")) # $1,000
months = int(input("How many months do you want to see results for?\n")) # 24

# Divive apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):

    # Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed += interest_paid

    if(money_owed - payment < 0):
        print("The last payment is", round(money_owed, 2))
        print("You paid off the loan in", i+1, "months")
        break
    
    # Make payment
    money_owed = money_owed - payment

    print("Paid", payment, "of which", round(interest_paid, 2), "was interest", end=" ")
    print("Now I owe", round(money_owed, 2))
