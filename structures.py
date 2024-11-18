from dbConnector import get_db_connection

class Marksheet:
    def __init__(self, student_id):
        self.student_id = student_id

    def add_subject_mark(self, subject_id, marks):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO marks (student_id, subject_id, marks) VALUES (%s, %s, %s)', 
                           (self.student_id, subject_id, marks))
            connection.commit()

    def get_marks(self):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT subject_id, marks FROM marks WHERE student_id = %s', (self.student_id,))
            rows = cursor.fetchall()
        return rows

    def __str__(self, subjects):
        marks_str = ", ".join([f"{subjects[sub_id]}: {mark}" for sub_id, mark in self.get_marks()])
        return f"Student ID: {self.student_id}, Marks: {marks_str}"

class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.marksheet = Marksheet(student_id)

    def add_subject_mark(self, subject_id, marks):
        self.marksheet.add_subject_mark(subject_id, marks)

    def __str__(self, subjects):
        return self.marksheet.__str__(subjects)

class School:
    def __init__(self, school_id):
        self.school_id = school_id

    def find_student(self, student_id):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT student_id FROM students WHERE student_id = %s AND school_id = %s', 
                           (student_id, self.school_id))
            row = cursor.fetchone()
        return Student(row[0]) if row else None

class County:
    def __init__(self, county_id):
        self.county_id = county_id

    def find_student(self, student_id):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT school_id FROM schools WHERE county_id = %s', (self.county_id,))
            schools = cursor.fetchall()
            for school in schools:
                student = School(school[0]).find_student(student_id)
                if student:
                    return student
        return None

class State:
    def __init__(self, state_id):
        self.state_id = state_id

    def find_student(self, student_id):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT county_id FROM counties WHERE state_id = %s', (self.state_id,))
            counties = cursor.fetchall()
            for county in counties:
                student = County(county[0]).find_student(student_id)
                if student:
                    return student
        return None
