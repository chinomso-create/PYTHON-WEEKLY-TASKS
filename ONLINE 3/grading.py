def calculate_grade(score):
    if score >= 70 and score <= 100:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

name = input("Enter student name: ")
score = int(input("Enter your score: "))
if score <0 or score >100:
    print("Invalid score")
else:
    grade = calculate_grade(score)

print("\n Student Result")
print("Name: ", name)
print("Score: ", score)
print("Grade: ", grade)