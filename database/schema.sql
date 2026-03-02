-- ===============================
-- STUDENT REGISTRATION TABLE
-- ===============================

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    age INTEGER,
    class TEXT,
    subject_interest TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);