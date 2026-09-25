
students = []
courses = []
marks = {}


def input_number_of_students():
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                return n
            print("Number of students must be greater than 0.")
        except ValueError:
            print("Please enter an integer.")


def input_students(n):
    for i in range(n):
        print(f"\n--- Student {i + 1} ---")
        while True:
            student_id = input("ID: ").strip()
            if student_id and not any(s["id"] == student_id for s in students):
                break
            print("ID must not be empty and must be unique.")

        name = input("Name: ").strip()
        dob = input("Date of birth (DD/MM/YYYY): ").strip()

        # Dictionary is used for student information.
        students.append({
            "id": student_id,
            "name": name,
            "dob": dob
        })


def input_number_of_courses():
    while True:
        try:
            n = int(input("\nEnter number of courses: "))
            if n > 0:
                return n
            print("Number of courses must be greater than 0.")
        except ValueError:
            print("Please enter an integer.")


def input_courses(n):
    for i in range(n):
        print(f"\n--- Course {i + 1} ---")
        while True:
            course_id = input("Course ID: ").strip()
            if course_id and not any(c["id"] == course_id for c in courses):
                break
            print("Course ID must not be empty and must be unique.")

        name = input("Course name: ").strip()

        # Dictionary is used for course information.
        courses.append({
            "id": course_id,
            "name": name
        })

        # A dictionary stores marks of students for each course.
        marks[course_id] = {}


def list_students():
    print("\n========== STUDENTS ==========")
    if not students:
        print("No students.")
        return

    print(f"{'ID':<12}{'Name':<25}{'Date of birth'}")
    print("-" * 55)

    for student in students:
        print(
            f"{student['id']:<12}"
            f"{student['name']:<25}"
            f"{student['dob']}"
        )


def list_courses():
    print("\n========== COURSES ==========")
    if not courses:
        print("No courses.")
        return

    print(f"{'ID':<12}{'Course name'}")
    print("-" * 40)

    for course in courses:
        print(f"{course['id']:<12}{course['name']}")


def input_marks_for_course():
    if not courses:
        print("No courses available.")
        return

    list_courses()
    course_id = input("\nSelect course ID: ").strip()

    course = next((c for c in courses if c["id"] == course_id), None)
    if course is None:
        print("Course not found.")
        return

    print(f"\nEntering marks for: {course['name']}")

    for student in students:
        while True:
            try:
                mark = float(input(
                    f"Mark for {student['id']} - {student['name']}: "
                ))

                if 0 <= mark <= 10:
                    marks[course_id][student["id"]] = mark
                    break

                print("Mark must be between 0 and 10.")
            except ValueError:
                print("Please enter a number.")


def show_student_marks_for_course():
    if not courses:
        print("No courses available.")
        return

    list_courses()
    course_id = input("\nEnter course ID: ").strip()

    course = next((c for c in courses if c["id"] == course_id), None)
    if course is None:
        print("Course not found.")
        return

    print(f"\n========== MARKS: {course['name']} ==========")
    print(f"{'Student ID':<15}{'Name':<25}{'Mark'}")
    print("-" * 50)

    course_marks = marks[course_id]

    for student in students:
        student_id = student["id"]

        if student_id in course_marks:
            mark = course_marks[student_id]
            print(f"{student_id:<15}{student['name']:<25}{mark:.2f}")
        else:
            print(f"{student_id:<15}{student['name']:<25}Not entered")


def menu():
    while True:
        print("\n" + "=" * 45)
        print("       STUDENT MARK MANAGEMENT")
        print("=" * 45)
        print("1. List students")
        print("2. List courses")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_students()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            show_student_marks_for_course()
        elif choice == "5":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please choose 1-5.")


def main():
    print("=" * 45)
    print("   PRACTICAL WORK 1: STUDENT MARK MANAGEMENT")
    print("=" * 45)

    number_of_students = input_number_of_students()
    input_students(number_of_students)

    number_of_courses = input_number_of_courses()
    input_courses(number_of_courses)

    menu()


if __name__ == "__main__":
    main()
