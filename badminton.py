def rmv_duplicate(lst):
    temp = []
    for val in lst:
        if val not in temp:
            temp.append(val)
    return temp

def intersection(l1,l2):
    l3= []
    for val in l1:
        if val in l2:
            l3.append(val)
    return l3

def union(l1,l2):
    l3 = l1.copy()
    for val in l2:
        if val not in l1:
            l3.append(val)
    return l3

def difference(l1,l2):
    l3 = []
    for val in l1:
        if val not in l2:
            l3.append(val)
    return l3

def CnB(l1,l2):   #CnB(C,B)
    l3 =intersection(C,B)
    print("List of students who play BOTH CRICKET AND BADMINTON: ", l3)
    return len(l3)

def eCeB(l1,l2):  #eCeB(C,B)
    l3 =union((difference(C,B)),difference(B,C))    
    print("\n\nList of students who play EITHER CRICKET OR BADMINTON but not both is : ", l3)
    return len(l3)

def nCnB(U,l1,l2):  #nCnB(U,C,B)
    l3 = difference(U,union(l1,l2))
    print("Number of students who play NEITHER CRICKET NOR BADMINTON: ",l3)
    return len(l3)

def CuB(l1,l2,l3):  #CuB(C,B,F)
    list = difference(intersection(l1,l3),l2)
    print("Number of students who play CRICKET & FOOTBALL but NOT BADMINTON: ",list)
    return len(list)

stud = []    #UNIVERSAL SET
total = int(input("Enter number of students in the class: "))
for i in range(total):
    temp = input("Enter names of students in class: ")
    stud.append(temp)

print("Original list of students in class: ", stud)

C = []        #CRICKET SET
n = int(input("Enter no. of students who play CRICKET: "))
for i in range(n):
    temp = input()
    C.append(temp)
C = rmv_duplicate(C)     #DUPLICATIONS ARE REMOVED

B = []         #BADMINTON SET
n = int(input("Enter no. of students who play BADMINTON: "))
for i in range(n):
    temp = input()
    B.append(temp)
B = rmv_duplicate(B)        #DUPLICATIONS ARE REMOVED

F = []     #FOOTBALL SET
n = int(input("Enter no. of students who play FOOTBALL: "))
for i in range(n):
    temp = input()
    F.append(temp)
F = rmv_duplicate(F)            #DUPLICATIONS ARE REMOVED

print("No. of students who play BOTH CRICKET AND BADMINTON: ",CnB(C,B),"\n")
print("List of students who play EITHER CRICKET OR BADMINTON but not both is : ", eCeB(C,B),"\n")
print("Number of students who play NEITHER CRICKET NOR BADMINTON: ", nCnB(stud,C,B), "\n")
print("Number of students who play CRICKET & FOOTBALL but NOT BADMINTON: ",CuB(C,B,F), "\n")



"""flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        print("Number of students who play both cricket and badminton : ", CB(Cricket,Badminton))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==2:
        print("Number of students who play either cricket or badminton but not both : ", eCeB(Cricket, Badminton))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==3:
        print("Number of students who play neither cricket nor badminton : ", nCnB(SEComp,Cricket,Badminton))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==4:
        print("Number of students who play cricket and football but not badminton : ", CBnF(Cricket,Football,Badminton))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==5:
        flag=0
        print("Thanks for using this program!")

    else:
        print("!!Wrong Choice!! ")
        a=input("\n\nDo you want to continue (yes/no) :")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program!")"""
