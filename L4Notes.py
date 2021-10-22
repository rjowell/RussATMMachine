
class ATM:

  def __init__(self,bankName,bankCity,listOfAccounts):
    self.name = bankName
    self.city = bankCity
    self.accountList = listOfAccounts

'''

Add an ATM class: Init should take: bankName, bankCity, list of accounts


Using your Bank Account class, create instances of 3 different bank accounts for each of your fellow classmates.


'''


class BankAccount:

  #def deposit():

  #def withdraw():
  
  #def checkBalance():

  def __init__(self,accountType,firstNameInput,lastNameInput,eMailInput,phoneNumberInput):
    self.type = accountType
    self.firstName = firstNameInput
    self.lastName = lastNameInput
    self.eMail = eMailInput
    self.phone = phoneNumberInput
    self.balance = 0


MrRussAccount = BankAccount("investment","Bigmac","Whopper","king@burgerking.com","7034440000")



  


'''
User Input/Output
-Opening an account
-Current Balance
-Help
-Number input - 
-

BLUEPRINT FOR ACCOUNT:
Legal Name: First/Last
Withdraw/Deposit
Help / Pizza Syste,
Address
PhoneNumber
Type checking, savings, investment
Date of Birth
E-mail



'''