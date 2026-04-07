def average_grades(student):
    return sum(student["grades"])/len(student["grades"])

def best_student(students):
    return max(students, key = average_grades)

def students_with_debts(students):
    return [s for s in students if min(s["grades"]) < 4]

def group_words_by_lenght(words):
    result = {}
    for word in words:
        result.setdefault(len(word), []).append(word)
    return result

def sort_by_price(products):
    return sorted(products, key = lambda x: x["price"])

def sort_by_rating(products):
    return sorted(products, key = lambda x: x["rating"], reverse = True)

def grade_statistics(students):
    stats = {}
    for student in students:
        for grade in student["grades"]:
            stats[grade] = stats.get(grade, 0) + 1
    return stats

def get_names(students):
    return [s["name"] for s in students]