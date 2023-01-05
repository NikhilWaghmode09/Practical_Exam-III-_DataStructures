def get_mtx(mat,r,c):
    print("Enter values:")
    for i in range(r):
        a=[]
        for j in range(c):
            temp = int(input())
            a.append(temp)
        mat.append(a)

def display(mat,r,c):
    for i in range(r):
        for j in range(c):
            print(mat[i][j],end="\t")
        print()

def add(mat1,mat2,r,c):
    result = []
    print("Addition of matrices is: ")
    for i in range(r):
        a = []
        for j in range(c):
            a.append(mat1[i][j]+mat2[i][j])
        result.append(a)
    display(result,r,c)

def sub(nat1,mat2,r,c):
    result = []
    print("Substraction of matrices is: ")
    for i in range(r):
        a =[]
        for j in range(c):
            a.append(mat1[i][j] - mat2[i][j]) 
        result.append(a)
    display(result,r,c)

def mul(mat1,mat2,r1,c1,r2,c2):
    result = []
    print("Multiplication of the matrices is: ")
    for i in range(r1):
        a = []
        for j in range(c2):
            mul = 0
            for k in range(c1):
                mul = mul+ mat1[i][k]* mat2[k][j]
            a.append(mul)
        result.append(a)
    display(result,r1,c2)

def transpose(mat,r,c):
    result = []
    for i in range(r):
        a = []
        for j in range(c):
            print(mat[j][i], end = "\t")
        print()

mat1 = []
mat2 = []

print("For 1st matrix : ")
r1=int(input("Enter num of rows : "))
c1=int(input("Enter num of columns : "))

print("For 2nd matrix : ")
r2=int(input("Enter num of rows : "))
c2=int(input("Enter num of columns : "))


get_mtx(mat1,r1,c1)
get_mtx(mat2,r2,c2)


print("1st matrix : ")
display(mat1,r1,c1)
print("2nd matrix : ")
display(mat2,r2,c2)

if (r1==r2 and c1==c2):
    add(mat1,mat2,r1,c1)
else:
    print("Addition is not possible.")
if (r1==r2 and c1==c2):
    sub(mat1,mat2,r1,c1)
else:
    print("Substraction is not possible.")

if(r2==c1):
    mul(mat1,mat2,r1,c1,r2,c2)
else:
    print("Multiplication is not possible.")

print("Transpose of matrix 1: ")
transpose(mat1,r1,c1)
print("Transpose of matrix 2: ")
transpose(mat2,r2,c2)
