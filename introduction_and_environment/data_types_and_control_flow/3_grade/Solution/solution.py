# Code your solution here
marks = int(input())
if marks >= 90:
    grade = "A+ GRADE"
elif marks < 90 and marks >= 70:
    grade = "B GRADE"
elif marks < 70 and marks >= 50:
    grade = "C GRADE"
elif marks < 50 and marks >= 35:
    grade = "D GRADE"
else:
    grade = "FAIL"

print(grade)