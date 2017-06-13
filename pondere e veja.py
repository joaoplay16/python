lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Adicione sua funcao abaixo!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
    
def get_average(students):
    homework = 0.1 * average(students['homework'])
    quizzes = 0.3 * average(students['quizzes'])
    tests = 0.6 * average(students['tests'])
    
    return homework + quizzes + tests
print (get_average(tyler))
