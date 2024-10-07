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
8
4
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
8.4
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
2. Mathematical tables - print tables from 3 to 20
```
print(3,1,3*1)
print(3,2,3*2)
print(3,3,3*3)
```
Here, we can see that there is a sequence in the 2nd and 3rd term. So, we can have a For Loop with iterator i   
Start_value=1   
Stop_value=4   
Step_value=1   
```
for i in range(1,4,1):
    print(3,i,3*i)
```
Now, we need table upto 3 times 10.  So
```
for i in range(1,11,1):
    print(3,i,3*i)
```
Next, we need to repeat same block for table of 4
```
for i in range(1,11,1):
    print(3,i,3*i)
for i in range(1,11,1):
    print(4,i,4*i)
```
It will be nice to have a blank line as a separator between the blocks 3 and 4
```
for i in range(1,11,1):
    print(3,i,3*i)
print()
for i in range(1,11,1):
    print(4,i,4*i)
print()
```
The spacing and indentation determines whether the line of code is within the For Loop or outside the For Loop.  For example, what would be the output for this program ?
```
for i in range(1,11,1):
    print(3,i,3*i)
    print()
for i in range(1,11,1):
    print(4,i,4*i)
print()
```
In the above program, the print() in line 3 is happening within the For Loop. If we need it outside the For Loop, we need to indent this line to the left. Let us add one more block for 5.
```
for i in range(1,11,1):
    print(3,i,3*i)
print()
for i in range(1,11,1):
    print(4,i,4*i)
print()
for i in range(1,11,1):
    print(5,i,5*i)
print()
```
In above code, observe lines 2,5,8. The parameter 3 is changing as per sequence 3,4,5. So, this is a candidate for an Outer For Loop with   
Start_value=3   
Stop_value=6   
Step_value=1   
Since the iterator i is busy, we need to use another iterator j. The existing block of code can be selected, click *tab* so that it gets indented to the right.
```
for j in range(3,6,1):
    for i in range(1,11,1):
        print(j,i,j*i)
    print()
```
```
for j in range(3,21,1):
    for i in range(1,11,1):
        print(j,i,j*i)
    print()
```
To enable printing of any mathematical tables, let us create 2 variables *start* and *stop*   
```
start=3
stop=8
for j in range(start,stop+1,1):
    for i in range(1,11,1):
        print(j,i,j*i)
    print()
```
Next, we can create a function *table1(start,stop)* to accept 2 parameters and print the mathematical table
```
def table1(start,stop):
    for j in range(start,stop+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()
table1(3,8)
```
Next, accept start and stop through keyboard






