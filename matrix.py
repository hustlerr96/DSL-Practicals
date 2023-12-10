
row=int(input("\nEnter the no. of rows"))
col=int(input("\nEnter the no. of columns"))

m1=[[0 for i in range(col)] for i in range(row)]
m2=[[0 for i in range(col)] for i in range(row)]
ans=[[0 for i in range(col)] for i in range(row)]

for i in range (2):
    print("\nEnter data for matrix", i+1)
    if i==0:
        matrix=m1
    else:
        matrix=m2
    for i in range(row):
        for j in range(col):
            matrix[i][j]=int(input(f"Enter the data for row {i+1} and col {j+1}: "))

def addition(m1,m2):
    for i in range(row):
        for j in range(col):
            ans[i][j]=m1[i][j]+m2[i][j]
    return (ans)

def subtraction(m1,m2):
    for i in range(row):
        for j in range(col):
            ans[i][j]=m1[i][j]-m2[i][j]
    return (ans)

def transpose(m,r,c):
    ans=[[0 for i in range(row)] for i in range(col)]
    for i in range(r):
        for j in range(c):
            ans[i][j]=m[j][i]
    return (ans)

def multiplication(m1,m2):
    ans=[[0 for i in range(len(m2[0]))] for i in range(len(m1))]
    if (len(m1[0])==len(m2)):
        print("Multiplication possible")
        for i in range(row):
            for j in range(col):
                for k in range(row):
                    ans[i][j]+=m1[i][k]*m2[k][j]
        return (ans)
    else:
        print("Multiplication not possible")

flag=1
while flag==1:
    print("\n**********MENU**********")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Exit")
    ch=int(input("\nEnter the no. of the operation you want to perform"))

    if ch==1:
        print("Addition: ", addition(m1,m2))
        flag=1
    
    elif ch==2:
        print("Subtraction: ", subtraction(m1,m2))
        flag=1
    
    elif ch==3:
        print("Multiplication: ", multiplication(m1,m2))
        flag=1
    
    elif ch==4:
        print("\nOn which matrix do you want to perform transpose operation?")
        a=int(input("\n1. Matrix 1  |  2. Matrix 2"))
        if a==1:
            print("Transpose: ", transpose(m1,row,col))
        else:
            print("Transpose: ", transpose(m2,row,col))
        flag=1
    
    else:
        flag=0
