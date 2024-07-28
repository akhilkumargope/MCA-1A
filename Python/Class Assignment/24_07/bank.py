class BankAccount:
    # __balance , __account_number

    def __init__(self):
        self.__account_number=0
        self.__balance=0.0    
    

    def set_account_number(self,account_number):
        self.__account_number=account_number

    def set_balance(self,balance):
        if(balance>0):
            self.__balance=balance
        else:
            print("Balance cannot be set to negative")
        
    def get_balance(self):
        return self.__balance
    
    def add_money(self,amount):
        self.__balance=self.__balance+amount
    
    def withdraw_money(self,amount):
        if(self.__balance-amount < 0):
            print("Insufficient Funds")
        else:
            self.__balance=self.__balance-amount

    def show_details(self):
        print("Acc_No.:- ", self.__account_number)
        print("Balance:- ",self.__balance)

def main():
    account_number=int(input("Enter The Account number"))
    balance=float(input("Enter the Balance"))
    account=BankAccount()

    account.set_account_number(account_number)
    account.set_balance(balance)
    account.show_details()

if __name__== "__main__":
    main()
        
