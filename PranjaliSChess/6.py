def calc1(num1,num2):
    sum1=num1+num2
    diff1=num1-num2
    prd1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    print(sum1,diff1,prd1,div1,div2,rem1,exp1)
f1=open("in1.txt","r")
num1=int(f1.readline())
num2=int(f1.readline())
calc1(num1,num2)
