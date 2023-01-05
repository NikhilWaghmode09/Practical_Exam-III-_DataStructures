def absent(marks,n):
    global count 
    count = 0
    for i in range (n):
        if(marks[i]==0):
            count +=1
    return count

def avg_marks(marks,n):
    sum = 0
    for i in range(n):
        sum = sum + marks[i]
    temp = n - count
    avg = sum/temp
    return avg

def highest(marks,n):
    high = marks[0]
    for i in range(n):
        if(marks[i]>high):
            high = marks[i]
    return high

def lowest(marks,n):
    low = marks[0]
    for i in range(n):
        if(marks[i]<low and marks[i] != 0):
            low = marks[i]
    return low

def freq(marks,n):
    s = set(marks)
    hf = 0
    for i in s:
        cnt = 0
        for j in range (n):
            if(i==marks[j]):
                cnt += 1
        if(cnt>hf):
            hf = cnt
            k = i
    print(k,"marks have the highest frequency of",hf)

marks = []

n = int(input("Enter no. of students in class:"))
for i in range(n):
    j = i+1
    temp=int(input("Enter marks of student %i:"%j))
    marks.append(temp)
print("Marks",marks)
print("No. of absent students:",absent(marks,n))
print("Average score of class:",avg_marks(marks,n))
print("Highest score of the class:",highest(marks,n))
print("Lowest score of the class:", lowest(marks,n))
freq(marks,n)

#print(set(marks))
