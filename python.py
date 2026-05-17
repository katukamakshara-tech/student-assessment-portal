
#print("hello world")
#s="akshara"
#print(s.find('a'))
#print(s.find('a',s.find('a')+1))
#print(s.find('k',s.find('k')+1))
#s="venkataa"
#print(s.find('a',s.rfind('a')+1))
#print(s.index('h'))
#print(s.rindex('a'))
#print(s.lindex('a'))
#print(s.ljust(10,'#'))
#print(s.rjust(18,'#'))
#print(s.zfill(10))
#print(s.center(18,'#'))
#print(s.strip())
#print(s.lstrip())
#print(s.rstrip())
#s="python is hard to learn"
#print(s.replace('hard','easy'))
#s1='/'
#s2='akshara'
#print(s1.join(s2))
#print(s.split("a"))
#print(s.split(' ',2))
#s='katukamakshara@gmail.com'
#print(s.partition('g'))
#print(s.rpartition('a'))
#print(s.upper())
#print(s.lower())
#print(s.title())
#print(s.casefold())
#print(s.swapcase())
#print(s.capitalize())
#s1=" "
#print(s1.isspace())
#print(s.isalnum())
#print(s.isnumeric())
###string formatting
"""name="akshara"
age=21
salary=100000.34
print(f'hi,my name is {name} my age is {age} and my salary is {salary}')  ###f-strings"""
#print("hi,my name is {} my age is {} and my salary is {}" .format (name,age,salary))    ###format()
#print("hi,my name is {} my age is {} and my salary is {}" .format (age,name,salary))    
#print("hi my name is %s my age is %d and my salary is %G" %(name,age,salary))        ### %formatting
#print("hi i am akshara\nwho are you")
#name=input("enter your name: ")
#print("hi",name)
#n=int(input("enter any number :"))
#print("multiplication table of",n)
#for i in range (1,11):
 #   print(n,"x",i,"=",n*i)
#l=list("python")
#l1=[[1,2,3],[4,5,6],[7,8,9]]
#l2=[[9,8,7],[6,5,4],[3,2,1]]
#for i  in range (0,3):
 #   for j in range (0,3):
  #      print(l1[i][j]+l2[i][j],end=" ")
   # print()    

#l1=[[1,2,3],[4,5,6],[7,8,9]]
#l2=[[9,8,7],[6,5,4],[3,2,1]]
#for i  in range (0,3):
 #   for j in range (0,3):
  #      print(l1[i][j]*l2[i][j],end=" ")
   # print()   
"""
orders=["pizza","burger","coke"]
print(orders)
orders.extend(["fries","ice cream"])  
print(orders)  
orders.remove('coke')
print(orders)
orders.reverse()
print(orders)"""

"""
seats=['A1','A2','A3','A4']
seats.insert(0,"A1-VIP")
print(seats)
seats.remove('A3')
print(seats)
seats.pop()
print(seats)
"""

"""students=["aksh","vicky","prash","suppi","vicky","prash"]
print(students.count("vicky"))
print(students.index("prash"))
students.sort()
print(students)

"""
"""followers=["aksh","vicky","prash","suppi","vicky","prash"]
followers.remove("vicky")
followers.remove("prash")
print(followers)
followers.sort()
print(followers)
followers.reverse()
print(followers)"""


"""songs=["A","B","C","D"]
songs.extend(["E","F"])
print(songs)
songs.remove("B")
print(songs)
songs.insert(0,"z")
print(songs)
"""

"""items=["soap","rice","milk"]
(items.remove("milk"))
print(items)
items.clear()
print(items)"""
"""x = 10
if x>5:
    print("hello")
name = 'Python'
print(name[1:4])
for i in range(1, 4):
    print(i)
"""
"""n=int(input("enter any number: "))
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")"""
"""year=int(input("enter the year: "))
if year%4==0:
    print("leap year")
elif year%100==0:
    print("leap year")
else:
    print("not leap year")"""

#seats=[1,2,3,4,5,6,2]
"""seats.add(6)
print(seats)"""
#seats.remove(5)
"""print(seats)
seats.sort()
print(seats)
seats.reverse()
print(seats)"""

"""eats.insert(0,"A1-VIP")
print(seats)"""
#seats.remove('A1')
#print(seats)
"""print(seats)
seats.pop()
print(seats)
"""
"""for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print("*",end=" ")
    print()  """ 

"""rows = 5

for i in range(rows):
    # Print spaces
    print(" " * (rows - i - 1), end="")

    # Print stars
  """  
"""def calculating_total(items):
    total=sum(items)
    return total
items=[123,854,290,37833]
bill=(calculating_total(items))    
print("total: ",bill)"""



"""def eligibility(age):
    if age>18:
        return "eligible"
    else:
        return "not eligible"
age=int(input("enter age: "))    
print(eligibility(age))     """

"""def calculate_bill(units):
    total=sum(units)
    return total
units=[234,1963,76984,2574]
monthlybill=(calculate_bill(units))
print("total: ",monthlybill)
    
"""
"""def conversion_farhenheit(celsius):
    farhenheit=(9/5 *celsius) + 32
    return farhenheit
celsius=int(input("enter value :"))
print(conversion_farhenheit(celsius))

"""
"""def calculate_SI(interst,principal,time):
    SI=(interst*time*principal)/100
    return SI
principal=float(input("enter the principal amount :"))
interst=float(input("enter the interst value :"))
time=float(input("enter the time :"))
print(calculate_SI(interst,principal,time))"""


"""
def students_avg(total_marks,n):
    averagemarks=(total_marks)/n
    return averagemarks
n=int(input("enter value :"))
total_marks=int(input("enter marks :"))
print(students_avg(total_marks,n))
    """

"""
def students_report(marks):
    if marks>35:
        return "pass"
    else:
        return "fail"
marks=int(input("enter marks :"))    
print(students_report(marks))    """
"""

def students_grade(score):
    if score>80:
        return "A"
    elif 80>score>50:
        return "B"
    else:
        return "C"
score=int(input("enter score : "))
print(students_grade(score))    
        """
import random 
print(random.choice([1,2,3,4,5]))