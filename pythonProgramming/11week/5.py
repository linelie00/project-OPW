def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

students = [ {'name': 'John', 'age': 18, 'score': 70}, {'name': 'Jane', 'age': 20, 'score': 90}, {'name': 'Smith', 'age': 19, 'score': 85}, {'name': 'Taehyun', 'age': 20, 'score': 99} ]

filtered = filter(lambda x: x['age'] <= 24 and x['score'] > 80, students)
students = list(filtered)


students = list(map(lambda x: {'name': x['name'], 'age': x['age'] + 3, 'score': x['score'], 'grade': grade(x['score'])}, students))
print("변환된 데이터: ", students)

print("최고 점수 학생: ", max(students, key=lambda x: x['score'])['name'])
print("최저 점수 학생: ", min(students, key=lambda x: x['score'])['name'])