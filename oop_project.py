from Bank_project import *

Deepak = BankAccount(1000, "Deepak")
Naresh = BankAccount(2000, "Naresh")

# Deepak.getBalance()
# Naresh.getBalance()

# Deepak.deposit(500)

# Deepak.withdraw(10000)
# Deepak.withdraw(100)

# Deepak.transfer(100,Naresh)

#########################
Bobby = InterestRewardsAcc(1000, "Bobby")
Bobby.getBalance()
Bobby.deposit(100)

Bobby.transfer(100, Deepak)

Bunny = SavingsAccount(1000, "Bunny")

Bunny.getBalance()
Bunny.deposit(100)

Bunny.transfer(10000, Bobby)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             


