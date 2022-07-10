class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber=cardNumber
        self.pin=pin
        self.balence=1000000
    def checkBalence(self):
        print("Your Balence Is")
        print(self.balence)
    def withdraw(self,amount):
        if(amount>self.balence):
            print("Insufficent Balence")
        else:
            self.balence=self.balence-amount
            print("Your Balence Is")
            print(self.balence)
    def deposit(self,amount):
        self.balence=self.balence+amount
        print("Your Balence Is")
        print(self.balence)
def main():
    cardNumber=input("Insert Your Card Number")
    pin=input("Enter Your Pin Number")
    user1=Atm(cardNumber,pin)
    print("Select Any One Option")
    print("1 for Balence, 2 for Withdraw, 3 for Deposit")
    choice=int(input("Enter Your Choice"))
    if(choice==1):
        user1.checkBalence()
    elif(choice==2):
        amount=int(input("Enter The Amount"))
        user1.withdraw(amount)
    else:
        amount=int(input("Enter The Amount"))
        user1.deposit(amount)
main()