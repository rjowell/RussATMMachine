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