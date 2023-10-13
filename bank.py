class bank():
    bankname="SBI"
    def __init__(self,Name,Phon,Pan,Bal,Pin):
        self.Name=Name
        self.Phon=Phon
        self.Pan=Pan
        self.Bal=Bal
        self.Pin=Pin
    def statement(self):
        p=int(input("eanter your Pin :"))
        if p==self.Pin:
            print(f"my Name is :{self.Name}")
            print(f"my Phon number is :{self.Phon}")
            print(f"my Pan number is :{self.Pan}")
            print(f"my bank balance is : {self.Bal}")
        else:
            print("incorrect Pin")
    def deposite(self):
        n=int(input("eanter your Pin :"))
        if n==self.Pin:
            D=int(input("eanter your amount :"))
            self.Bal=self.Bal+D
            print(f"The deposite amount :{D}")
            print(f"The current bank balance :{self.Bal}")
        else:
            print("incorrect Pin")
    def withdraw(self):
        p=int(input("eanter your Pin :"))
        if p==self.Pin:
            W=int(input("eanter your amount :"))
            if W<=self.Bal:
                self.Bal=self.Bal-W
                print(f"The withdraw amount :{W}")
                print(f"The current bank balance :{self.Bal}")
            else:
                print("insufficent balance")
        else:
            print("incorrect Pin")
    def changenumber(self):
        p=int(input("eanter your Pin :"))  
        if p==self.Pin:
            C=int(input("eanter new mob number :"))
            print(f"the old phone nummber is :{self.Phon}")
            self.Phon=C
            print(f"the new phone nummber is :{self.Phon}")
        else:
            ("incorrect pin")
    @classmethod
    def changebankname(cls):
        B=input("enter your bank name :")
        print(f"the previous bank name is :{cls.bankname}")
        cls.bankname=B
        print(f"the new bank name is :{cls.bankname}")
N=input("Please eanter your Name :") 
P=int(input("Please eanter your phone nummber :"))
PAN=input("Please eanter your PAN nummber :")
balance=int(input("Please eanter a amount :"))
pin=int(input("Please eanter a Pin nummber :"))
userinput = bank(N,P,PAN,balance,pin)
for x in range(1,6):
    j=int(input("enter '1' for statement  enter '2' for deposite  enter '3' for withdraw  enter '4' for changenumber enter '5' for changebankname"))
    if j==1:
        userinput.statement()
    elif j==2:
        userinput.deposite()
    elif j==3:
        userinput.withdraw()
    elif j==4:
        userinput.changenumber()
    elif j==5:
        userinput.changebankname()
    else:
        print("invalid input")