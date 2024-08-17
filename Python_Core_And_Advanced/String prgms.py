# 1)
# With the help of while loop
"""
input="Learning Python is very Easy"
output="gninraeL nohtyP si yrev ysaE"
l=input.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
print(l1)
print(" ".join(l1))
"""
# With the help of for loop
'''
input="Learning Python is very Easy"
output="gninraeL nohtyP si yrev ysaE"
l=input.split()
l1=[]
for i in l:
    l1.append([i][::-1])
print(l1)
print(" ".join(l1))
'''
# 2)
"""
input="Learning Python is very Easy"
output="Easy very is Python Learning"
l=input.split()
l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i-=1
# print(l1)
# print(" ".join(l1))

for i in l[::-1]:
    l1.append(i)
print(l1)
print(" ".join(l1))
"""

#3
'''
s="QACircle"
Case 1
print(s[0::2])
print(s[1::2])
Case 2
print("Characters at even positions:",end=" ")
for i in range(len(s)):
    if i%2==0:
        print(s[i],end=" ")
print("")
print("Characters at odd positions:",end=" ")
for i in range(len(s)):
    if i%2!=0:
        print(s[i],end=" ")
'''
"""
num=20
if num<0:
  print("Please Enter the positive Number")
else:
  sum=0
  while num>0:
     sum=sum+num
     num=num-1


print("Sum of Natural numbers are",sum)
"""
"""
n = int(input("Enter the number"))
for i in range(n):
      for j in range(n):
          print(i+1, end='')
      print()

n=int(input("Enter the number"))
for i in range(n):
  for j in range(n):
     print(chr(65+j),end='')
  print()
"""
"""
n = int(input("Enter the number"))
for i in range(n):
      for j in range(n):
          print(chr(69-j), end='')
      print()
"""

s="Hello World"
print(s.swapcase())


