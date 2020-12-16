import random
class CreditCard:
    accounts = dict()
    def create_an_account():
        IIN = str(400000)
        account_identifer = str(random.randint(0, 999999999)).rjust(9, '0')
        checksum = str(random.randint(0, 9))
        credit_card_number = IIN + account_identifer + checksum
        pin = str(random.randint(0, 9999)).rjust(4, '0')
        CreditCard.accounts[credit_card_number] = {}
        CreditCard.accounts[credit_card_number]["pin"] = pin
        CreditCard.accounts[credit_card_number]["balance"] = 0
        print("Your card has been created")
        print("Your card number:")
        print(credit_card_number)
        print("Your card PIN:")
        print(pin)
        
    def log_into_account(cc_number, cc_pin):
        account = CreditCard.accounts.get(cc_number)
        if account:
            return account.get("pin") == cc_pin
        return False
        
    def showMenu():
        print("""
        1. Balance
        2. Log out
        0. Exit""")
        
    def getBalance(cc_number):
        return CreditCard.accounts[cc_number]["balance"]
        
menu = """
1. Create an account
2. Log into account
0. Exit
"""
print(menu)
user_input = int(input())
while user_input != 0:
    if user_input == 1:
        CreditCard.create_an_account()
    elif user_input == 2:
        cc_number = input("Enter your card number: ")
        cc_pin = input("Enter your PIN: ")
        while CreditCard.log_into_account(cc_number, cc_pin):
            print("You have successfully logged in!")
            CreditCard.showMenu()
            cc_operation = int(input())
            if cc_operation == 1:
                CreditCard.getBalance(cc_number)
            elif cc_operation == 2:
                print("You have successfully logged out!")
                break
            elif cc_operation == 0:
                user_input = 0
                break
            cc_operation = int(input())
        print("Wrong card number or PIN!")
    if user_input != 0:
        print(menu)
        user_input = int(input())

print("Bye!")
        