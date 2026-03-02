import sqlite3

DB_PATH = "database/db.sqlite"

def create_student(name, email, password, age, student_class, subject_interest):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students (name, email, password, age, class, subject_interest)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, email, password, age, student_class, subject_interest))

        conn.commit()
        conn.close()

        return {"status": "success", "message": "Student registered successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}