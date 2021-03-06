
class ATM:
  
  def homeScreen(self):
    print("**************************")
    print("Welcome to the ATM!")
    option = input("1 - Open Account  2 - Load Account  3 - Deposit  4 - Withdraw E - Exit H - Help: ")
    #print("**************************")
    if option == "1":
      name = input("What is your name?: ")
      city = input("What city do you live in?: ")
      checking = input("Do you want C-hecking or S-avings?: ")
      while checking != "C" and checking != "S":
        checking = input("Do you want C-hecking or S-avings?: ")
      isChecking = True
      if checking == "S":
        isChecking = False
      self.accountList.append(Account(name,city,isChecking))
      print("Account successfully added!")
      return self.homeScreen()
    elif option == "2":
      if len(self.accountList) == 0:
        print("There are no accounts to load, try creating one!")
        return self.homeScreen()
      else:
        self.loadAccount()
        return self.homeScreen()
    elif option == "3":
      if self.currentAccount == None:
        print("No Account Loaded")
        return self.homeScreen()
      else:
        self.processDeposit()
    elif option == "4":
      if self.currentAccount == None:
        print("No Account Loaded")
        return self.homeScreen()
      else:
        self.processWithdraw()
    elif option == "H":
      print("First, you need to create an account, Then you need to load an account, and then, you can do stuff with it!")
      return self.homeScreen()
    else:
      print("Toodles!!!")

  def processDeposit(self):
    depositAmt = int(input("How much do you want to deposit?: "))
    if depositAmt < 0:
        print("That's called a withdraw silly!")
        return self.processDeposit()
    elif depositAmt == 0:
      print("You're no closer to a million dollars!")
      return self.processDeposit()
    else:
      self.currentAccount.deposit(depositAmt)
      print("New Balance: "+str(self.currentAccount.getCurrentBalance()))
      return self.homeScreen()
  
  def addAccount(self,nameIn,cityIn,typeOfAccount):
    self.accountList.append(Account(nameIn,cityIn,typeOfAccount))

  def processWithdraw(self):
    withdrawAmt = input("How much do you want to withdraw? E to Exit: ")
    if withdrawAmt == "E":
      return self.homeScreen()
    else:
      withdrawAmt = int(withdrawAmt)
      if withdrawAmt < 0:
        print("That's called a deposit silly!")
        return self.processWithdraw()
      elif withdrawAmt == 0:
        print("Well what's the point??")
        return self.processWithdraw()
      else:
        if self.currentAccount.withdraw(withdrawAmt) == False:
          print("Do you think money grows on trees? You don't have enough!")
          return self.processWithdraw()
        else:
          self.currentAccount.withdraw(withdrawAmt)
          print("New Balance: "+str(self.currentAccount.getCurrentBalance()))
          return self.homeScreen()



  '''
  Get input of name to search
  If you find an account with that name, load it in to current account
  IF no account with that name exists, print out an error
  '''


  def loadAccount(self):
    nameInput = input("Enter the name of the account you want to load: ")

    for accts in self.accountList:
      if accts.name == nameInput:
        self.currentAccount = accts
        break
      
    if self.currentAccount != None:
      print("Your account has been loaded!")
      print("Name: "+self.currentAccount.name)
      print("Balance: "+str(self.currentAccount.currentBalance))
      return True
    else:
      print("No account with that name exists. Please try again")
      return self.loadAccount()
  
  
  def __init__(self):
    self.accountList = []
    self.currentAccount = None

  














    





class Account:

  def __init__(self,name,city,isChecking):
    self.currentBalance = 0
    self.isChecking = isChecking
    self.name = name
    self.city = city

  def deposit(self,depositAmount):
    self.currentBalance += depositAmount
    return True

  def withdraw(self,withdrawAmount):
    if withdrawAmount > self.currentBalance:
      return False
    else:
      self.currentBalance -= withdrawAmount
      return True






















class Account:

  def __init__(self,name,city,isChecking):
    self.name = name
    self.city = city
    self.isChecking = isChecking
    self.currentBalance = 0

  def deposit(self,amount):
    self.currentBalance += amount
    return True

  def withdraw(self,amount):
    if self.currentBalance - amount < 0:
      return False
    else:
      self.currentBalance -= amount
      return True

  def getCurrentBalance(self):
    return self.currentBalance


'''
Class Account:

Initialize: Name, City, isChecking
self.currentBalance = 0

define depoist and withdraw methods.
'''




