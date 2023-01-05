percent = []
n = int(input("Enter total no. of students: "))

for i in range(n):
    temp = float(input("Enter the percentage of students: "))
    percent.append(temp)

print("\nOrignial array: \n", percent)

def selection_sort(arr,n):
    for i in range(n):
        for j in range(i+1,n):       # ---------- time cmplxty = O(n^2), space =O(1) ---------- #
            if (arr[i]>arr[j]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    print("\nArray sorted using Selection sort: \n",arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):    #n-i-1 make us ignore the last sorted element in everyround
            if(arr[j]>arr[j+1]):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    print("\nArray sorted using Bubble sort: \n",arr)
    if(n>=5):
        print("\nThe top five scores are:\n")
        for i in range(0,5):
            print(arr[6-i])
    else:
        print("\nCannot display top five scores since no. of students are <5.\n")
            

flag = 1
while(flag ==1):
    print("\n\n --MENU--")
    print("\n1. Selection sort.")
    print("\n2. Bubble sort.")
    print("\n3. Exit.")
    print("\nEnter your choice...")
    ch = int(input())
    if(ch == 1):
       selection_sort(percent,n) 
    elif(ch == 2):
        bubble_sort(percent)
    elif(ch == 3):
        flag == 0
        break
    else:
        print("\nInvalid choice.")

