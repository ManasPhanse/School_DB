use school;

-- Create States Table
CREATE TABLE states (
    state_id INT PRIMARY KEY,
    state_name VARCHAR(255) NOT NULL
);

-- Create Counties Table
CREATE TABLE counties (
    county_id INT PRIMARY KEY,
    state_id INT,
    FOREIGN KEY (state_id) REFERENCES states(state_id)
);

-- Create Schools Table
CREATE TABLE schools (
    school_id INT PRIMARY KEY,
    county_id INT,
    FOREIGN KEY (county_id) REFERENCES counties(county_id)
);

-- Create Students Table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    school_id INT,
    class_id INT,
    FOREIGN KEY (school_id) REFERENCES schools(school_id)
);

-- Create Subjects Table
CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(255) NOT NULL
);

-- Create Marks Table
CREATE TABLE marks (
    student_id INT,
    subject_id INT,
    marks INT,
    PRIMARY KEY (student_id , subject_id),
    FOREIGN KEY (student_id)
        REFERENCES students (student_id),
    FOREIGN KEY (subject_id)
        REFERENCES subjects (subject_id)
);
