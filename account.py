

'''
Write a homeScreen Method
Prints out prompts for the user: Open Account, Load Account, Deposit, withdraw, exit, help
Write out if/else structure for responses


RANDOM NUMBER GUESSER GAME
-Generate a random number between 1 and 20 and store it in a variable
Ask the user to guess the number
Say whether the number is too high or too low after each guess
Maximum of 5 guesses


'''
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

  ''' 
  Define an ATM Class:
  Init method should take a single parameter: Bank name,
  set this as a property, then initialize 2 other properies:
  accountList - blank array
  current account - 'None'

  '''
  '''
  def addAccount(self,name,city,isChecking):
    self.accountList.append(Account(name,city,isChecking))
    return True
    '''











  '''
  Create an Add Account method - params should inlcude the params you used for your account
    - use those parameters to append a new account to your accountlist

  '''

  def addAccount(self,nameIn,cityIn,typeOfAccount):
    self.accountList.append(Account(nameIn,cityIn,typeOfAccount))

    


















'''
Write a class for an account. It should take the following parameters:
  -name
  -city
  -type of account

'''


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



