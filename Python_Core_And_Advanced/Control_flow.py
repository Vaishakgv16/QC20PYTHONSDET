# Pin Generation 3 attempts
'''
pin_num=0
attempts=3
while attempts > 0:
    pin_num=int(input("Enter the number"))
    if pin_num==1602:
        print("Pin accepted",pin_num)
        break
    attempts-=1
else:
    print("Card is blocked")
    '''
# WAP to print vowels present in the given word
"""
vowels={'a','e','i','o','u'}
name="qacirclesoftwaretrainingacademy"
s1={x for x in name if x in vowels}
print(s1)
"""
#WAP to get the number of vowels present in the given name
vowels=['a','e','i','o','u']
name="qacirclesoftwaretrainingacademy"
s2=[x for x in name if x in vowels]
print(s2)
print(len(s2))



