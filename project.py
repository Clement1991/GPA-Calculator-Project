import csv
import sys

class Student:
    def __init__(self, name, math, biology, chemistry, physics, english):
        self.name = name
        self.scores = [int(math), int(biology), int(chemistry), int(physics), int(english)]

    def calculate_gpa(self):
        total = sum(self.scores)
        return round(total / len(self.scores), 2)

class GPA_Calculator:
    def __init__(self, filename):
        self.students = self.read_students_from_csv(filename)

    def read_students_from_csv(self, filename):
        students = []
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row["name"], row["maths"], row["biology"], row["chemistry"], row["physics"], row["english"])
                    students.append(student)
        except FileNotFoundError:
            sys.exit("Couldn't read csv file")
        return students

    def get_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        sys.exit("Student's name not found")

def main():
    check_args()
    gpa_calculator = GPA_Calculator(sys.argv[1])
    name = sys.argv[2]
    student = gpa_calculator.get_student(name)
    gpa = student.calculate_gpa()
    print(gpa)

def check_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")

if __name__ == "__main__":
    main()
