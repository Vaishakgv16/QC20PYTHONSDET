#Ex1:
"""
class Engine:
   a=10
   def __init__(self):
       self.b=20

   def m1(self):
       print("Engine Specific Functionality")


class Car:
   def __init__(self):
       self.engine=Engine()
   def m2(self):
       print("Car using engine class functionalities")
       print(self.engine.a)
       print(self.engine.b)
       self.engine.m1()

c=Car()
c.m2()
"""

#Ex 2

"""
class Car:


   def __init__(self,name,model,color):
       self.name=name
       self.model=model
       self.color=color


   def getinfo(self):
       print("Car Name is :{} ,Model is :{}, Color is :{}".
             format(self.name,self.model,self.color))


class Employee:
   def __init__(self,ename,eno,car):
       self.ename=ename
       self.eno=eno
       self.car=car


   def empinfo(self):
       print("The Name of an employee is :",self.ename)
       print("The Employee Number is :",self.eno)
       print("The Car Information of an employee")
       self.car.getinfo()


c=Car("I20",2016,"Red")
e=Employee("Rohit",121,c)
e.empinfo()
"""
"""
class Person:
    def property(self):
        print("Gold+Land+Cash")
    def house(self):
        print("3 BHK House")
class Child(Person):
    def house(self):
        super().house()
        print("4 BHK New house with interiors")
c=Child()
c.property()
c.house()

import keyword
print(keyword.kwlist)

'''thyu 'hnkjh jjhg' hhjhh hnj'''

print(int(0x1274af))

print(float("11.5"))

x=[251,253,255,255]
b=bytes(x)
for i in b:
    print(i)

s={10,20,20,10,"Hello",True}
print(s)
s.add("Hello")
print(s)
s.remove(True)
print(s)
s2={10,20,49,"trrg",30,30,20,49}
for i in s2:
    print(i)
   
MAX_VAL=100
print(MAX_VAL)
MAX_VAL=200
print(MAX_VAL)
"""
"""
from sys import argv
for x in argv[1:]:
    print(x)
print(len(argv))
print(int(argv[1])+int(argv[3]))
"""
# Connect to the database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Vaishak@16")
print(mydb)

# Create database
mycursor=mydb.cursor()
#mycursor.execute("create database qc20python")

# Create Table
mydb=mysql.connector.connect(host="localhost",user="root",password="Vaishak@16",database="qc20python")
mycursor=mydb.cursor()
#mycursor.execute("create table training(name VARCHAR(255),Address VARCHAR(255))")
#mycursor.execute("drop table training")
#mycursor.execute("create table Training(name VARCHAR(255),Address VARCHAR(255))")
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)

# Create Primary Key(if table exists we can alter the table)
# mydb=mysql.connector.connect(host="localhost",user="root",password="Vaishak@16",database="qc20python")
# mycursor=mydb.cursor()
# mycursor.execute("Create Table Customer(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),Address VARCHAR(255))")
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)

#Alter the table
mycursor.execute("ALTER TABLE TRAINING ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")