import os
import time
from art import *

os.system("cls")

# Lists & Vars & Classes
num = 1

Accounts = []  # Accounts must be in order like (ID,PASS)
Account_data = []  # EX A1 = Account 1 But there will be to be a emtpy space so it will be like A1, "", A2, "", A3


class Info:
    def __init__(self, name, age, birthday, password, money, savings):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.password = password
        self.money = money
        self.savings = savings


def MainScreen():
    os.system("cls")
    tprint("Banking\nSouth")
    ID = Account_data[Accounts.index(Account_ID)]

    ID.money = (int(ID.money))
    ID.savings = (int(ID.savings))


    print(f"Welcome back, {ID.name}\n")
    print(f"Checking account : ${ID.money}")
    print(f"Saving account : ${ID.savings}\n")

    print("Transfer")
    print("Account")
    print("Logout\n")

    choice = input("> ")

    if choice == "Transfer":
        Sav_or_checking = input("Checking or Saving: ")
        if Sav_or_checking == "Checking":

            transer_to = input("Account to transfer to: ")
            amount = input("Amount: ")
            amount = int(amount)

            if transer_to == "Savings":
                ID.money -= amount
                ID.savings += amount
                print("Money sent")
                time.sleep(1)
                MainScreen()
            else:
                if transer_to in Accounts:
                    Location = Accounts.index(transer_to)
                    SEND_ACCOUNT = Account_data[Location]
                    ID.money -= amount

                    SEND_ACCOUNT.money = int(SEND_ACCOUNT.money)

                    SEND_ACCOUNT.money += amount
                    print("Money sent")
                    time.sleep(1)
                    MainScreen()
                else:
                    print("Account not found")
                    time.sleep(1)
                    MainScreen()


        elif Sav_or_checking == "Saving":
            transer_to = input("Account to transfer to: ")
            amount = input("Amount: ")
            amount = int(amount)

            if transer_to == "Checking":
                ID.savings -= amount
                ID.money += amount
                print("Money sent")
                time.sleep(1)
                MainScreen()
            else:
                if transer_to in Accounts:
                    Location = Accounts.index(transer_to)
                    SEND_ACCOUNT = Account_data[Location]
                    ID.savings -= amount

                    SEND_ACCOUNT.money = int(SEND_ACCOUNT.money)

                    SEND_ACCOUNT.savings += amount
                    print("Money sent")
                    time.sleep(1)
                    MainScreen()
                else:
                    print("Account not found")
                    time.sleep(1)
                    MainScreen()

        else:
            MainScreen()

    elif choice == "Account":
        os.system("cls")
        tprint("Banking\nSouth")
        print("     Your Information\n")
        print(f"Name : {ID.name}")
        print(f"Age : {ID.age}")
        print(f"Birthday : {ID.birthday}")
        print(f"Password : {ID.password}")
        print(f"Money : ${ID.money}")
        print(f"Savings : ${ID.savings}\n")

        print("Edit")
        print("Back\n")

        option = input("> ")

        if option == "Edit":
            print("Edit information")
            Name = input("Name: ")
            Age = input("Age: ")
            Birthday = input("Birthday: ")
            Password = input("Password: ")

            Location = Accounts.index(ID.name)
            Accounts[Location] = Name
            Location = Accounts.index(Name) + 1
            Accounts[Location] = Password

            ID.name = Name
            ID.age = Age
            ID.birthday = Birthday
            ID.password = Password
            print("Account Info updated")
            time.sleep(1)
            OptionScreen()

        elif option == "Back":
            MainScreen()

        else:
            MainScreen()

    elif choice == "Logout":
        OptionScreen()

    else:
        MainScreen()



def CreateScreen():
    global num

    os.system("cls")
    tprint("Banking\nSouth")
    Name = input("Name: ")
    Age = input("Age: ")
    Birthday = input("Birthday: ")
    Password = input("Password: ")
    Money = input("Money: ")
    Saving = input("Savings: ")
    num += 1
    Creation = f"A{num}"
    Creation = Info(Name, Age, Birthday, Password, Money, Saving)
    Account_data.append(Creation)
    Account_data.append("")
    Accounts.append(Name)
    Accounts.append(Password)
    print("Account Created")
    time.sleep(2)
    os.system("cls")
    OptionScreen()


def LoginScreen():
    global Account_ID

    os.system("cls")
    tprint("Banking\nSouth")

    Account_ID = input("Account ID: ")
    Account_Pass = input("Account Pass: ")

    if Account_ID in Accounts:
        Location = Accounts.index(Account_ID) + 1  # Finds the ID in list and add 1 to the index to find password
        if Account_Pass == Accounts[Location]:
            MainScreen()
        else:
            print("\nAccount ID or Account Password not found")
            time.sleep(2)
            OptionScreen()
    else:
        print("\nAccount ID or Account Password not found")
        time.sleep(2)
        OptionScreen()


def OptionScreen():
    os.system("cls")
    tprint("Banking\nSouth")
    option = input("Login or Create account: ")
    if option == "Login":
        LoginScreen()
    elif option == "Create account":
        CreateScreen()
    else:
        OptionScreen()


# Start
OptionScreen()
