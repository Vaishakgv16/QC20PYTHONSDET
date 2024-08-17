# 1. Arithmetic Operator
#For  multi line comment - 1)first select the lines and ctrl + /
"""
x=160
y=80
print("x+y =",x+y)
print("x-y =",x-y)
print("x*y =",x*y)
print("x/y =",x/y)
print("x//y =",x//y)
print("x%y =",x%y)
print("x**y =",x**y)

print(0/160)
Below lines will get  Error
print(160/0)
print(160%0)

a="QACircle"
b="Training Academy"
c=8
print(a+b)
#Below 2 lines we will get type Error
print(a+c)          ******** String with number cannot be added
print(b+c)
print(a+b*c)        ******** Based on order precedence will be executed
print(a*c)
print(b*c)
print(a*b)          ********* We will get error since 2 strings cannot be multiplied
"""

#2. Relational Operator or Comparison Operator
'''
Ex1
a=16
b=25
print(" a > b =",a>b)
print(" a >= b =",a>=b)
print(" a < b =",a<b)
print(" a <= b =",a<=b)

Ex 2
x="qacircle"
y="qAcircle"
print(" x > y =",x>y)     ******** Based on Ascii values will be executed
print(" x >= y =",x>=y)
print(" x < y =",x<y)
print(" x <= y =",x<=y)

Ex 3
a=160
b=16
if a>b:
   print("Test is Pass")
else:
   print("Test Fail")

# Chaining of relational operator

print(15>5<40>36>53) ********* If one condition fails the o/p will be false
print(16<25<34<43<52)
'''
#3. Equality Operators
"""
print(16==16)
print("QAC"==16)
print("QAC"!=16)
print("QACircle"=="Qacircle")
print("QACircle"=="QACircle")
print(10==10==10==10)
print(20==20==10==30)
"""

#4. Logical Operator
"""
Boolean Type Behaviour Example
x=True
y=False
print(x and x)         ********* If both arguments true o/p will be true otherwise false
print(True and True)
print(y and x)
print(x or y)          **********If anyone argument true o/p will be true
print(not x)
print(not y)

Non Boolean Type Behaviour Example
print(16 and 25)        ******** since both are nonzero, always last value will be printed
print(340 and 520)
print(0 and 250)        ******** false and true means false so 0 will be printed
print(100 and 0)
print(160 or 0)         ******** True or false means true so true value ie 160 will be printed
print(0 or 2000)
print(not 0)
print(not 100)
print("" and "qacircle")  ******* Empty string-false and true means false so empty line will be printed
print("qacircle" and "QACircle")
print(" " or "QAC")         ******* contains space means True or True so space will be printed
print("QAC" or " ")
print("QAC" or "")
print(not "")
print(not " ")
"""
#5. Bitwise Operator
'''
print(7&16)
print(25&34)
print(7|25)
print(5^15)
print(16^7)
print(~0)
print(~-8)
print(20>>2)
print(10<<3)
'''
#6. Assignment Operator
'''
Ex.1
x=16
x+=20
print(x)
Ex.2
y=10
y**=3
print(y)
'''

#7. Ternary Operator or Conditional Operator
"""
Ex.1
a,b=-120,-100
x=a if a>b else b
print(x)

Ex.2 Read two inputs from the keyboard and print bigger value.

a=int(input("Enter First Value"))
b=int(input("Enter Second Value"))
x=a if a>b else b
print(x)

Ex.3 Read two numbers from the keyboard and print minimum value.

a=int(input("Enter First Value"))
b=int(input("Enter Second Value"))
min=a if a<b else b
print(min)

Ex.4 Write a program to read 3 numbers from the keyboad and print max value.

n1=int(input("Enter the First number"))
n2=int(input("Enter the Second number"))
n3=int(input("Enter the Third number"))
max_val=n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
print("The Maximum value =",max_val)

Ex.5 Write a program to read 3 numbers from the keyboard and print min value.

n1=int(input("Enter the First number"))
n2=int(input("Enter the Second number"))
n3=int(input("Enter the Third number"))
min_val=n1 if n1<n2 and n1<n3 else n2 if n2<n3 else n3
print("The Minimum value =",min_val)

Ex.6 Write a program to read 3 numbers from the keyboard ,
if 2 numbers are equal validate and print min and max value.

n1=int(input("Enter the First number"))
n2=int(input("Enter the Second number"))
n3=int(input("Enter the Third number"))
min_val=n1 if n1<n2 and n1<n3 else n2 if n2<n3 else n3
max_val=n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
print("The Maximum value =",max_val)
print("The Minimum value =",min_val)
"""

#8. Special Operator
"""
1. Identity Operator
   is
   is not
2. Membership Operator
   in
   not in
"""
'''
Ex.1 for Identity Operator
a=100
b=100
print(id(a),"==",id(b))
print(a is b)

Ex.2
x=120
y=200
print(x is y)                  ******** is used for object address comparison
print(a==b)                    ******** == used for content comparison
print(x is not y)

Ex.3
s1="QACircle"
s2='QACircle'
print(s1 is s2)

Ex4.
list1=["one","two","three"]
list2=["one","two","three"]
print(list1 is list2)        ****** o/p is false since lis1 and list2 are content so == operator used for
print(id(list2))              content comparison not is operator
print(id(list1))
print(list1==list2)         ******* o/p is true since == is used for content comparison 

Ex.1 for Membership operator
s1="Learning Python is Very Easy"
print("Easy" in s1)
print("eAsY" in s1)
print("v" not in s1)
print("LE" in s1)
print("Ki" not in s1)

Ex.2
list=["Bunny","Pinny","Billi","Sunny"]
print("sunny" in list)
print("Sunny" in list)
print("Bunny" not in list)
'''

# Operator Precedence
"""
1. () 
2. ** 
3. * ,/,//,% 
4. +,- 
5. << ,>> 
6. & 
7. | 
8. ==,!=,>,>=,<,<= ,is, is not,in , not in
9. not 
10. and 
11. or

Ex1.
a=7
b=-16
c=-25
d=32
print((a+b)*c/d)
print(a+(b*c)/d)
"""