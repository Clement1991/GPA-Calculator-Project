import pytest
from project import GPA_Calculator, Student

def main():
    test_GPA_calculator()

def test_GPA_calculator():
    # Create a temporary CSV file for testing
    with open("test_data.csv", "w") as file:
        file.write("name,maths,biology,chemistry,physics,english\n")
        file.write("Clement,76,80,65,60,85\n")

    # Initialize GPA calculator with test data
    gpa_calculator = GPA_Calculator("test_data.csv")

    # Test get_student method
    student = gpa_calculator.get_student("Clement")
    assert student.name == "Clement"
    assert student.scores == [76, 80, 65, 60, 85]

    # Test calculate_gpa method
    assert student.calculate_gpa() == 73.2

    # Clean up test data file
    import os
    os.remove("test_data.csv")

if __name__ == "__main__":
    main()
