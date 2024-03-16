def calculate_average(grades):
    return sum(grades) / len(grades)

def find_highest_grade(grades):
    return max(grades)

def find_lowest_grade(grades):
    return min(grades)

def count_above_threshold(grades, threshold):
    return sum(1 for grade in grades if grade > threshold)

def main():
    # Define list of student grades
    student_grades = [85, 90, 92, 88, 78, 95, 85, 80, 88, 92]

    # Calculate average grade
    average_grade = calculate_average(student_grades)

    # Find highest grade
    highest_grade = find_highest_grade(student_grades)

    # Find lowest grade
    lowest_grade = find_lowest_grade(student_grades)

    # Define threshold
    threshold = 90

    # Count number of students with grades above threshold
    above_threshold_count = count_above_threshold(student_grades, threshold)

    # Print results
    print("Student Grades:", student_grades)
    print("Average Grade:", average_grade)
    print("Highest Grade:", highest_grade)
    print("Lowest Grade:", lowest_grade)
    print(f"Number of students with grades above {threshold}: {above_threshold_count}")


if __name__ == "__main__":
    main()
