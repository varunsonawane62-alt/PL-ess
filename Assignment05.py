
n = int(input("Enter the number of students: "))

total_class_score = 0


for i in range(1, n + 1):
    print("\nStudent", i)
    total_student_score = 0

    
    for j in range(1, 6):
        score = float(input(f"Enter marks for test {j}: "))
        total_student_score += score

    
    average = total_student_score / 5
    print("Average score of student", i, "=", average)

    
    total_class_score += total_student_score


class_average = total_class_score / (n * 5)

print("\nOverall class average =", class_average)