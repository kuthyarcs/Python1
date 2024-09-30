def calc1(num1,num2):
    sum1=num1+num2
    dif1=num1-num2
    prd1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    print(sum1,dif1,prd1,div1,div2,rem1,exp1)
f1=open("in2.txt","r")
s1=f1.readline()
list1=s1.split(",")
num1=int(list1[0])
num2=int(list1[1])
calc1(num1,num2)
