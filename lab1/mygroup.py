groupmates = [
    {

        "name": "Иван",
        "surname": "Иванов",
        "exams": ["СИИ", "РКПО", "СПО"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Павел",
        "surname": "Павлов",
        "exams": ["СИИ", "РКПО", "СПО"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Илья",
        "surname": "Ильин",
        "exams": ["СИИ", "РКПО", "СПО"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Василий",
        "surname": "Васильев",
        "exams": ["СИИ", "РКПО", "СПО"],
        "marks": [3, 3, 3]
    }
]

def print_data(students):
    for student in students:
        print(student["name"], student["surname"], str(student["exams"]), str(student["marks"]))

def print_filter_data(students,mid):
    for student in students:
        if sum(student["marks"])/len(student["marks"]) > float(mid):
            print(student["name"], student["surname"], str(student["exams"]), str(student["marks"]))

print_data(groupmates)
mid = input("Введите среднюю оценку:\n")
print_filter_data(groupmates, mid)
