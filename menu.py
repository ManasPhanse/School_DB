from structures import *
from dbConnector import get_db_connection

def create_state_structure():
    with get_db_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT state_id FROM states')
        states_data = cursor.fetchall()

    states = {}
    for state in states_data:
        state_id = state['state_id']
        states[state_id] = State(state_id)

    return states

def find_student_in_state(state_objects, student_id):
    for state in state_objects.values():
        student = state.find_student(student_id)
        if student:
            return student
    return None

def get_subjects():
    with get_db_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT subject_id, subject_name FROM subjects')
        subjects_data = cursor.fetchall()

    subjects = {subject['subject_id']: subject['subject_name'] for subject in subjects_data}
    return subjects

def main_menu():
    state_objects = create_state_structure()
    subjects = get_subjects()

    while True:
        print("\nSchool Marksheet System")
        print("1. Find Student by ID")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ").strip()
            if not student_id:
                print("Student ID cannot be empty. Please try again.")
                continue
            
            student = find_student_in_state(state_objects, student_id)
            if student:
                print("\nStudent Found:")
                print(student.__str__(subjects))
            else:
                print("\nStudent not found. Please check the ID and try again.")

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1 to find a student or 2 to exit.")

if __name__ == "__main__":
    main_menu()
