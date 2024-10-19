def calc1(num1,num2):
    sum1=num1+num2
    diff1=num1-num2
    prd1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    result=str(sum1)+" "+str(diff1)+" "+str(prd1)+" "+str(div1)+" "+str(div2)+" "+str(rem1)+" "+str(exp1)
    return result
f1=open("in2.txt","r")
f2=open("out1.txt","w")
s1=f1.readline()
list1=s1.split(",")
num1=int(list1[0])
num2=int(list1[1])
result=calc1(num1,num2)
print(result)
f2.write(result)
f2.close()
