from GHCDSAccount import Account
#import GHCDSAccount

KaisAccount = Account("Kai","Los Angeles","savings","56789")
MayaAccount = Account("Maya","Washington, DC","savings","12345")
MrRussAccount = Account("Mr. Russ","Washington, DC","checking","friedshrimp1")
AmaruAccount = Account("Amaru","Tokyo","Checking","109876")

bank_customer_names = ["Kai","Maya","Mr Russ","Amaru","JJ","Jayden","Cole"]

#print(bank_customer_names[-3])

account_list = []

#print(len(account_list))

account_list.append(KaisAccount)
account_list.append(MayaAccount)
account_list.append(MrRussAccount)
account_list.append(AmaruAccount)

print(account_list[2].name)




























''''
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


BiancasAccount = BankAccount("checking","Bianca","Acnaib","bianca@bigmoney.com","7034440000")

AlexAccount = BankAccount("")

print(BiancasAccount.type)
print(BiancasAccount.firstName)



from account import Account, ATM

newAcct = ATM()
newAcct.homeScreen()

'''




