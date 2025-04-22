avg = 0
grade = [0] * 5  

for x in range(5):  
    while True:
        grade[x] = int(input("Put a grade between 0 - 100 : \n"))

        if 0 <= grade[x] <= 100:
            break

        else:
            print("Enter a valid grade between 0 and 100.\n")  

    avg = avg + grade[x]  

for x in range(4):

    if grade[x] < grade[x+1]:

        temp = grade[x]

        grade[x] = grade[x+1]

        grade[x+1] = temp



print(f" The average grade of the class is {avg/5}.")
print(f"\n The lowest mark of the class is : {grade[4]}")
print(f"\n The highest mark of the class is : {grade[0]}")

