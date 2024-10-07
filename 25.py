def genPassword1(size):
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
    for i in range(0,size-3,1):
        r1=rd.randint(0,61)
        pwd1=pwd1+s4[r1]
    list1=list(pwd1)
    rd.shuffle(list1)
    pwd2="".join(list1)
    return pwd2

for i in range(0,20,1):
    result=genPassword1(8)
    print(result)
