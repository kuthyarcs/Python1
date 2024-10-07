def table1(start,stop):
    for j in range(start,stop+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()
table1(3,8)
