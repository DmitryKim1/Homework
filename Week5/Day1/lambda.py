students = [
    {"name":"Anna", "score": 88},
    {"name": "Ivan", "score": 95},
    {"name": "Boris", "score": 78},
]

result = sorted(students, key = lambda student: student["score"], reverse=True)
print(result)