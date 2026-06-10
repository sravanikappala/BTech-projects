lt1 = []  
n = int(input("enter no of students:"))
for i in range(1,n):
    name = input(f"enter name of the {i} student :")
    percentage = int(input(f"enter percentsge of {i} student: "))
    marks = input("enter 3 subject marks :")
    marks_lt = marks.split(" ")
    for i in range(len(marks_lt)):
        marks_lt[i] = int(marks_lt[i])
    print(marks_lt)    
#    percentage = int(input(f"enter percentsge of {i} student: "))
    lt1.append(((name),marks_lt,percentage))
print(lt1)    
#print(lt1[0])
#print(lt1[1][2])

average = []
for student in lt1:
    name = student[0]
    marks_1 = student[1]
    print(f"marks of {name} student is {marks_1}")
    avg = sum(marks_1)/len(marks_1)
    print(f"average od {name} is {avg}")
     
    average.append((name,avg))
          
print(average)          
eligible = []
for student in lt1:
    if avg >= 5 and student[2] >80:
        eligible.append(student[0])
        
print(f"the scholarship is for {student[0]}")    
