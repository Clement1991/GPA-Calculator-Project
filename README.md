# GPA CALCULATOR

## Video Demo: [Watch Demo](https://www.youtube.com/watch?v=l33BAx8uqTs)

## Description:

The source code for the GPA calculator is contained in the `project.py` file. This project is a Python program designed to calculate the GPA of students in a Science class based on their exam scores in Mathematics, Biology, Chemistry, Physics, and English. The students' names and their exam scores are provided in a CSV file named `students.csv`.

The program has been refactored to use object-oriented programming (OOP) principles. It includes two classes: `Student` and `GPA_Calculator`. The `Student` class represents each student, with attributes for the student's name and their scores in various subjects. The `GPA_Calculator` class is responsible for reading student data from the CSV file, creating `Student` objects, and providing methods to retrieve a student and calculate their GPA.

The program begins by importing the `csv` and `sys` modules. The `csv` module is utilized to read the contents of the `students.csv` file, while the `sys` module is employed to handle certain conditions and command-line arguments.

A `main` function is defined to orchestrate the program's execution. Within the `main` function, the `GPA_Calculator` object is initialized with the CSV file, and the student's name is provided as a command-line argument to calculate their GPA.

### Usage

Run `python project.py students.csv "name"` where:
* `project.py` is the name of the Python file.
* `students.csv` is the CSV file containing the students' exam information.
* `name` is the name of the student from `students.csv` whose GPA is to be calculated.

## Testing of Functions

The testing module utilizes the `pytest` package and is contained in the `test_project.py` file. The testing covers relevant functions from the `project.py` file.

### Usage

Run `pytest test_project.py` to execute the tests. The testing includes:
* Verifying the correct number and authenticity of command-line arguments.
* Checking the accuracy of the total exam score calculation for a student.
* Validating the correctness of the GPA calculation obtained by the student.
