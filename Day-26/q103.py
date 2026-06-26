def check_balance(balance):
    # with open ("atm.csv","r") as f:
    #     balance=int(f.readline(Balance))
    # f.close()
    if balance < 0:
        print(f"your balance is negative{balance}")
    elif balance ==0:
        print(f"your balance is zero{balance}")
    else:
        print(f"your balance is {balance} ")


def deposite(balance):
    dep=int(input("Enter the amount:  "))
    balance+=dep
    print(f"Available balance {balance}")
def withdrawl(balance):
    withdrl=int(input("Enter the amount:  "))
    if withdrl>balance:
        print("insufficient balance ")
    else:
        print(f"Available balance {balance}")



balance=100
while True:
    print("1. Check Balance ")
    print("2. Deposite ")
    print("3. Withdrawl ")
    print("4. Transaction Status ")
    print("5. Exit ")
    choice=int(input("Enter your choice: "))
    if choice==1:
        check_balance(balance)
    elif choice==2:
        deposite(balance)
    elif choice ==3:
        withdrawl(balance)
    elif choice==4:
        trans_sta(balance)
    elif choice==5:
        exit()