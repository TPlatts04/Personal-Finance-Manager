import os
import csv
import sys

FILENAME = "finance.csv"
CSV_FIELDNAMES = []

def assignCSVFieldnames():
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        i = 0
        while i < 1:
            CSV_FIELDNAMES.extend(lines[0].strip().split(","))
            i+=1

def main():
    print("\nThank you for choosing Tom's Personal Finance Manager!")
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        if len(lines) > 1:
            del lines[0]
            print("\nData in file consists of:")
            for line in lines:
                print(' '.join(line.strip().split(",")))
    name = input("Please enter your name here: ").capitalize()
    optionSelector(name)

def optionSelector(name):
    options = int(input("\nIs this an:\n(1) Income\nOr\n(2) Expense\n(3) to view more options\nEnter your number here: "))
    match options:
        case 1:
            typeIncome(name)
        case 2:
            typeExpense(name)
        case 3:
            moreOptions(name)
        case "_":
            print("Invalid Option, Please try again...")
            main()

def typeIncome(username):
    income = float(input("\nHow much was this Income? £"))
    incomeReason = input("\nWhere did this Income come from? (e.g - Savings, salary etc.) ").capitalize()
    with open(FILENAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDNAMES)
        writer.writerow({CSV_FIELDNAMES[0]: username, CSV_FIELDNAMES[1]: "Income", CSV_FIELDNAMES[2]: incomeReason, CSV_FIELDNAMES[3]: income})
    optionSelector(username)
    

def typeExpense(username):
    expense = float(input("\nHow much was this Expense? £"))
    expenseReason = input("\nWhere did this Expense go to? (e.g - Food, rent etc.) ").capitalize()
    with open(FILENAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDNAMES)
        writer.writerow({CSV_FIELDNAMES[0]: username, CSV_FIELDNAMES[1]: "Income", CSV_FIELDNAMES[2]: expenseReason, CSV_FIELDNAMES[3]: f"-{expense}"})
    optionSelector(username)

def moreOptions(username):
    print("\nHere are the other options:\n(1) Generate a summary of Income:Expense Ratio\n(2) Create a budget based on monthly salary\n(3) Exit program")
    optionSelect = int(input("Enter your number here: "))
    match optionSelect:
        case 1:
            generateSummary(username)
        case 2:
            createBudget(username)
        case 3:
            print("Goodbye...")
            sys.exit()
        case "_":
            print("Invalid Option, Try again...")
            moreOptions(username)

def generateSummary(username):
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        newLines, incomeList, expenseList = [], [], []
        incomeSummary, expenseSummary = 0, 0
        for x in range(len(lines)):
            if x >= 1:
                newLines.append(lines[x].strip().split(","))
            else:
                continue
        for a in range(len(newLines)):
            if float(newLines[a][3]) < 0:
                expenseList.append(float(newLines[a][3]))
            else:
                incomeList.append(float(newLines[a][3]))
        for b in incomeList:
            incomeSummary += b
        for c in expenseList:
            expenseSummary += c
        print(f"\n{username}, your total summary is as follows:\nTotal Income = £{incomeSummary}\nTotal Expenses = -£{str(expenseSummary).strip("-")}")    
        optionSelector(username)        


def createBudget(username):
    monthlyIncome = float(input("\nWhat is your monthly salary after tax? £"))
    needs = monthlyIncome * 0.5
    wants = monthlyIncome * 0.3
    investments = monthlyIncome * 0.2
    print(f"\nThe budget goes as follows:\n* For needs you should aim to spend no more than 50% of your monthly salary, for you this is £{needs:.2f}\n* For wants you should aim to spend no more than 30% of your monthly salary, for you this is £{wants:.2f}\n* Finally, you should aim to invest the other 20% of what you have left over, either into a high yield\nsavings account ~5% APR or more, or into the S&P 500 on an Investment Account like Trading 212. For you this would be £{investments:.2f}.")
    optionSelector(username)

if __name__ == "__main__":
    if os.path.isfile(FILENAME):
        assignCSVFieldnames()
        main()
    else:
        with open(FILENAME, "w") as file:
            file.writelines("name,typeOfSpend,spendReason,amount\n")
        assignCSVFieldnames()
        main()