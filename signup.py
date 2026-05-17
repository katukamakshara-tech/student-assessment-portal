
customers = [
    {
        'username': 'Akshara',
        'userPassword': 'akshara@26',
        'balance': 15000
    },
    {
        'username': 'vicky',
        'userPassword': "vicky@26",
        'balance': 20000
    },
    {
        'username': 'prashanth',
        'userPassword': 'prashanth@26',
        'balance': 25000
    }
]

while True:

    print('''
      WELCOME TO THE BANK
      1.signin
      2.signup
      3.exit
    ''')

    choose = int(input("enter your choice: "))

    if choose == 1:

        name = input("Enter user name: ")
        password = input("Enter user password: ")

        for i in customers:

            if name == i["username"] and password == i["userPassword"]:

                print(f"Hi {name} welcome!! LOGIN SUCCESSFULLY!!!")

                print('''
               WELCOME TO THE APPLICATION
               MENU:
               1.BALANCE ENQUIRY
               2.WITHDRAWAL OF AMOUNT
               3.DEPOSIT
               4.EXIT
                ''')

                choose = int(input("enter your choice: "))

                balance = i["balance"]

                if choose == 1:

                    print("your balance amount is: ", balance)

                elif choose == 2:

                    amount = int(input("enter withdrawal amount: "))

                    if amount < balance:

                        balance -= amount
                        i["balance"] = balance

                        print("your withdrawal amount is :", amount)
                        print("your current balance: ", balance)

                    else:

                        print("insufficient balance")

                elif choose == 3:

                    amount = int(input("enter deposit amount: "))

                    balance += amount
                    i["balance"] = balance

                    print("your deposited amount is: ", amount)
                    print("your current balance:", balance)

                else:

                    print("exit")

                break

    elif choose == 2:

        username = input("enter your name: ")
        userPassword = input("enter password: ")
        balance = int(input("enter your balance: "))

        person = {}

        person["username"] = username
        person["userPassword"] = userPassword
        person["balance"] = balance

        customers.append(person)

        print("Account created successfully")

    else:

        print("Thank You")
        break