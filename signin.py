
customers=[
    {
        'username':'Akshara',
        'userPassword':'akshara@26',
        'balance':15000
    },
    {
        'username':'vicky',
        'userPassword':"vicky@26",
        'balance':20000
    },
    {
        'username':'prashanth',
        'userPassword':'prashanth@26',
        'balance':25000
    }
]

name=input("Enter user name: ")
password=input("Enter user password: ")

for i in customers:

    if name==i["username"] and password==i["userPassword"]:
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
        balance=i["balance"]

        if choose==1:
            print("your balance amount is: ",balance)
        elif choose==2:
            amount=int(input("enter withdrawal amount: "))
            if amount<balance:
               balance-=amount
               i["balance"]=balance
               print("your withdrawal amount is :",amount )
               print("your current balace: ",balance)
            else:
               print("insufficient balance")
        elif choose==3:
             amount=int(input("enter deposit amount: "))
             balance+=amount
             print("your deposited amount is: ",amount)
             print("your current balance:",balance)
        else:
             print("exit")      
             break
                
            
        
            



    
              
          