roll_calls=[]
n=int(input("Enter number of students in club:"))
for i in range(0,n):
    r=int(input("Enter roll number of student:"))
    roll_calls.append(r)
print("list of roll numbers:",roll_calls)

def sort(l1):
    temp=0
    for i in range (1,len(l1)):
        for j in range (0,len(l1)):
            if( l1[i]<l1[j]):
                temp = l1[i]
                l1[i] = l1[j]
                l1[j] = temp
    #log base 3 n
    print("Roll calls in ascending order:",roll_calls)
sort(roll_calls)

def Ternary_Search(left,right,key,list):
    
    if (right>=left):
        mid1 = left+(right-left) // 3 
        mid2 = right-(right-left) // 3 
    
        if (list[mid1] == key): 
            return mid1
          
        elif (list[mid2] == key): 
            return mid2 
          
        if (key < list[mid1]): 
              return Ternary_Search(left, mid1 - 1, key, list)
          
        elif (key > list[mid2]): 
              return Ternary_Search(mid2 + 1, right, key, list)
          
        else: 
              return Ternary_Search(mid1 + 1, mid2 - 1, key, list)
    return 0
          

roll=int(input("enter roll number which you want to search:"))
left =0
right = len(roll_calls)-1

find = Ternary_Search(left,right,roll,roll_calls)
if find != 0:
    print("The Roll Number ",roll,"is member of club.")
else:
    print("Roll Number ",roll,"is not member of club.")
