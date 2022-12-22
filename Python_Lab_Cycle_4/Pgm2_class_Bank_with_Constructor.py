class bank:
    Name=""
    AccountNo=0
    AccountType=""
    AccountBalance=0.0;
    def __init__(self):
        self.Name=input("Enter the name of the account holder: ")
        self.AccountNo=int(input("Enter the Account number: "))
        self.AccountType=input("Enter the account type: ")
        self.AccountBalance=float(input("Enter the account balance: "))
    def details(self):
        print("Account Details: ")
        print("Name :",self.Name)
        print("Account Number: ",self.AccountNo)
        print("Account Type: ",self.AccountType)
        print("Account Balance: ",self.AccountBalance)
    def deposit(self):
        print("DEPOSIT")
        self.AccountBalance=self.AccountBalance+float(input("enter the amount: "));
        self.details();
    def withdraw(self):
        print("WITHDRAW")
        self.AccountBalance=self.AccountBalance-float(input("enter the amount: "));
        self.details();
account=bank();
account.details();
account.deposit();
account.withdraw();
