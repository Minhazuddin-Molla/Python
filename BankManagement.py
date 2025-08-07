class BankAccount:
    def __init__(self,value):
        self.__balance=value
        print("Creating account with",value)
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        if value<0:
            print("Error: Negative amount is not accepted.")
        else:
            self.__balance=value
    def deposit(self,amount):
        if amount<=0:
            print("Only positive amount is accepted.")
        else:
            self.__balance+=amount
            print("Depositing",amount)
    def withdraw(self,amount):
        if self.__balance-amount>0:
            self.__balance-=amount
            print("Withdrawing",amount)
        else:
            print("Insufficient funds. Try again.")
if __name__=="__main__":
    amount=int(input("Enter initial amount to be stored:"))
    obj=BankAccount(amount)
    c=-1
    while c!=0:
        ch=int(input("Choose from the following:\n 1.Set Balance\n 2.Deposit Amount\n 3. Withdraw Amount\n 4.Current Balance\n 5.Quit"))
        match(ch):
            case 1:
                amount=int(input("Set balance:"))
                obj.balance=amount
            case 2:
                amount=int(input("Enter amount to be deposited: "))
                obj.deposit(amount)
            case 3:
                amount=int(input("Enter amount to be withdrawn: "))
                obj.withdraw(amount)
            case 4:
                print("Balance = Rs.",obj.balance)
            case 5:
                c=0
            case _:
                print("Wrong choice. Try again.")