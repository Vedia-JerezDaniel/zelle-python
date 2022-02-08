# ATM Simulator
#     Takeaways:
#         1. Requires OOP
#         2. Requires good data structures for convenient user lookup
#         3. Requires file access read from disk on program startup, write to disk when ??? (your call here).
        
#     Initial screen ask for User ID and PIN
#          class GraphicsInterface:
#               Screen 1
#                   Entry["User ID", "Pin"]
#     Initialize new screen to display possible functions
#               Screen 2
#                   Buttons["Check Balance", "Withdraw Cash", "transacsfer Money", "Exit", "Quick Cash $100"]
#                   Txt["Checking", "Savings"]
#                       format left and right aligned label and $
#                       use template variable for formatting
#               def update(self):
#                   update values to screen
#          class TextInterface:
#               same functionality, for testing purposes
#               
#     User id will lookup info for user's accounts(including PIN to see if match)

class TextInterface:
    def __init__(self):
        self.active = True
        print("Welcome to the ATM")

    def getUserInput(self):
        #get UserID and Pin
        a = input("Username >> ")
        b = input("Enter PIN >> ")
        return a, b

    def choosetransacsaction(self):
        #give user choice of "Check Balance", 
        # "Withdraw Cash", "transacsfer Money", "Exit", "Quick Cash $100"
        #Display user balance

        transac = "xxx"
        while transac[0] != ("C" or "W" or "T" or "S" or "E" or "Q"):
            transac = input('Please select a transacsaction from the approved list. "Check Balance", \n "Withdraw/Deposit Cash", "transfer Money", "Send Money", "Exit", "Quick Cash $100 >> ')
            if transac[0] == "E":
                self.active = False
            return transac
            
    def displayBalance(self, checking, savings):
        print("Checking: {0}    Savings: {1}".format(checking, savings))

    def withdrawCash(self):
        print("This function will withdraw or deposit cash.")
        value = eval(input("How much should we deposit/withdraw? Enter negative value to withdraw. >> "))
        account = input("Checking or Savings? >> ")
        print("Your transacsaction is complete.\n")
        return value, account

    def gettransacsferInfo(self):
        outaccount = input("Select account to withdraw money from: >> ")
        inaccount = input("Select account to deposit money in: >> ")
        value = eval(input("How much would you like to move?"))
        print("Your transacsaction is complete.\n")
        return inaccount, outaccount, value

    def getSendInfo(self):
        recipient = input("Recipient User id")
        type_sender = input("Sender: Checking or Savings?  >> ")
        type_recipient = input("Recipient: Checking or Savings?  >> ")
        value = eval(input("How much to send? >> "))
        print("Your transacsaction is complete.\n")
        return recipient, type_sender, type_recipient, value

    def close(self):
        if self.active != False:
            return False
        print("\nPlease come again.")
        return True
