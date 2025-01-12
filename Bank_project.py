class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount'{self.name}' created.\nBalance = ${self.balance: .2f}")

    def getBalance(self):
        print(f"\nAccount'{self.name}'balance = $ {self.balance: .2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException ( f"\nsorry, account '{self.name}' only has a balance of ${self.balance: .2f}")
    

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nwithdraw complete. ")
            self.getBalance()
        except BalanceException as error:
            print(f"\nwithdraw interupted: '{error}'")

    
    def transfer(self, amount, account):
        try:
            print('\n********\n\nBeginning Transfer..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete..!')
        except BalanceException as error:
            print(f'\nTransfer Interrupted..! {error}')
        
class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + ( amount * 1.05)
        print("\nDeposit Complete..")
        self.getBalance()
    
class SavingsAccount(InterestRewardsAcc):
    def __init__(self, InitialAmount, accName):
        super().__init__(InitialAmount, accName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete..!")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
            



