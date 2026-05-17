
username="Akshara"
userPassword="akshara@26"
balance=15000

name=input("Enter user name: ")
password=input("Enter user password: ")

if username==name and userPassword==password:
    print("Hi {} welcome!! LOGIN SUCCESSFULLY!!!".format(name))
    while True:
        print ('''
        WELCOME TO THE APPLICATION
               MENU:
               1.BALANCE ENQUIRY
               2.WITHDRAWAL OF AMOUNT
               3.DEPOSIT
               4.EXIT
        ''')
        choose=int(input("enter your choice: "))

        if choose==1:
            print("your balance amount is: ",balance)
        elif choose==2:
            amount=int(input("enter withdrawal amount: "))
            if amount<balance:
               balance-=amount
               print("your withdrawal amount is :",amount )
               print("your current balace: ",balance)
            else:
               print("insufficient balance")
        elif choose==3:
             amount=int(input("enter deposit amount: "))
             balance+=amount
             print("your deposited amount is: ",amount)
             print("your cuttent balance:",balance)
        else:
             print("exit")      
             break
                
            
        
            



    
              
          