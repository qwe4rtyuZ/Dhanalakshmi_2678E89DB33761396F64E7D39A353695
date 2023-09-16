class BankAccount:
  def __init__(self,name,no,abalance):
    self.__account_name=name
    self.__account_no= no
    self.__account_balance=abalance
  def deposit(self,deposit):
    b._BankAccount__account_balance=b._BankAccount__account_balance+deposit
  def withdraw(self,withdraw):
    b._BankAccount__account_balance=b._BankAccount__account_balance-withdraw
  def accountbalance(self):
    print('The balance amount is ',b._BankAccount__account_balance)
b=BankAccount("dhanalakshmi",123456789,50000)
print("The account holder name:",b._BankAccount__account_name)
print("The account number:",b._BankAccount__account_no)
DA=int(input("Enter deposit amount:"))
b.deposit(DA)
WD=int(input("Enter with drawamount:"))
b.withdraw(WD)
b.accountbalance()