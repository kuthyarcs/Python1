**Python Sample Assignments for Practice**   

1. Calculator Program
```
num1=8
num2=4
sum1=num1+num2
print(sum1)
```
Next, print difference, product, decimal division, integer division, remainder, exponential on same line
```
num1=8
num2=4
sum1=num1+num2
dif1=num1-num2
prd1=num1*num2
div1=num1/num2
div2=num1//num2
rem1=num1%num2
exp1=num1**num2
print(sum1,dif1,prd1,div1,div2,rem1,exp1)
```
Next, convert this into a function taking 2 parameters num1, num2

```
def calc1(num1,num2):
    sum1=num1+num2
    dif1=num1-num2
    prd1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    print(sum1,dif1,prd1,div1,div2,rem1,exp1)
calc1(8,4)
calc1(4,8)
calc1(10,2)
calc1(20,5)
```
Next, take num1, num2 as input values from user through keyboard
```
def calc1(num1,num2):
    sum1=num1+num2
    dif1=num1-num2
    prd1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    print(sum1,dif1,prd1,div1,div2,rem1,exp1)
num1=input("Enter first number")
num2=input("Enter second number")
calc1(num1+num2) #you may get a error. Why ?
```
```
num1=int(s1) #To convert String to Integer   
s2=str(num2) #To convert Integer to String   
```
```
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
```
Next, take num1, num2 in 2 separate lines in input file in1.txt 
3
8
```
f1=open("in1.txt","r")
num1=f1.readline()# You may get error since num1, num2 are string
num2=f1.readline()   
calc1(num1,num2)
```
You may get error since num1, num2 are string.  How do you resolve it?
```
num1=int(f1.readline())
num2=int(f1.readline())
```
Next, take num1, num2 in a single line separated by a comma, in input file in2.txt
3,8
```
f1=open("in2.txt","r")
s1=f1.readline()
list1=s1.split(",") # When string is split, the contents go into a list
num1=int(list1[0])  # By default the values read from a file are String.
num2=int(list1[1])
calc1(num1,num2)
```
Next, send the output to a new file out1.txt
```
def calc2(num1,num2):
    sum1=num1+num2
    dif1=num1-num2
    prd1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    return(sum1,dif1,prd1,div1,div2,rem1,exp1) # instead of print, return
f1=open("in2.txt","r")
f2=open("out1.txt","w")
s1=f1.readline()
list1=s1.split(",")
num1=int(list1[0])
num2=int(list1[1])
out=calc2(num1,num2)
s2=out[0]+" "+out[1]+" "+out[2]+" "+out[3]+" "+out[4]+" "+out[5]+" "+out[6]
f2.write(s2)
f2.close()
```
The above program will give an error - "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
```
f1=open("in2.txt","r")
f2=open("out1.txt","w")
s1=f1.readline()
list1=s1.split(",")
num1=int(list1[0])
num2=int(list1[1])
out=calc2(num1,num2)
s2=str(out[0])+" "+str(out[1])+" "+str(out[2])+" "+str(out[3])+" "+str[4]+" "+str(out[5])+" "+str(out[6])
f2.write(s2)
f2.close()
```
2. 


