import random
print('''Hi.....Welcome
      Are You Ready...?
      Guess correct number from 1 to 15 and win the game
 ''')
n=(int(input("your guess :")))
value=n
score=20
guess=random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("Correct value:",guess)
if value==guess:
      print('''Hurraay!!!
          Won the game...
        ''')
      print("your score: ",score)
else:
    score-=5
    print("Try Again")   
    print("your score: ",score)
