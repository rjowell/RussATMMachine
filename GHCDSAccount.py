'''
Create an "Account" class
It should take 4 parameters in the init method: name, city, accountType, password input
-These should be set to the respective properties of that class.
-Also in the init method, set a "balance" property to 0 


'''




class Account:

  def __init__(self,nameInput,cityInput,accountTypeIn,passwordIn):
    self.name = nameInput
    self.city = cityInput
    self.accountType = accountTypeIn
    self.password = passwordIn
    self.balance = 0

  def withdraw(self,amount):
    if amount < self.balance:
      self.balance -= amount

  def deposit(self,amount):
    self.balance += amount