import random as rd
s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2="abcdefghijklmnopqrstuvwxyz"
s3="0123456789"
s4=s1+s2+s3
pwd1=""


r1=rd.randint(0,25)
pwd1=pwd1+s1[r1]
r1=rd.randint(0,25)
pwd1=pwd1+s2[r1]
r1=rd.randint(0,9)
pwd1=pwd1+s3[r1]
for i in range(0,5,1):
    r1=rd.randint(0,61)
    pwd1=pwd1+s4[r1]
print(pwd1)
