n1=int(input('enter any number '))
n2=int(input('enter second num '))
n3=int(input('enter third num '))
if n1>n2 and n1>n3:
    m=n1
elif n2>n1 and n2>n3:
    m=n2
else:
    m=n3
print('largest no. is ',m)
