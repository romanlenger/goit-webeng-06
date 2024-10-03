import random
import psycopg2
from faker import Faker

faker = Faker()
DB = "hw-06"

conn = psycopg2.connect(host="localhost", database=DB, user="postgres", password="mort")
cursor = conn.cursor()


def populate_db():
    # Додавання груп
    group_names = ['Group A', 'Group B', 'Group C']
    group_ids = []
    for group_name in group_names:
        cursor.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,))
        group_id = cursor.fetchone()[0]
        group_ids.append(group_id)

    # Додавання викладачів
    teacher_names = [faker.name() for _ in range(5)]
    teacher_ids = []
    for teacher_name in teacher_names:
        cursor.execute("INSERT INTO teachers (fullname) VALUES (%s) RETURNING id", (teacher_name,))
        teacher_id = cursor.fetchone()[0]
        teacher_ids.append(teacher_id)
    
    # Додавання предметів і прив'язка до викладачів
    subject_names = ['Math', 'History', 'Science', 'Literature', 'Physics', 'Chemistry', 'Biology', 'Art']
    subject_ids = []
    for subject_name in subject_names:
        teacher_id = random.choice(teacher_ids)
        cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s) RETURNING id", (subject_name, teacher_id))
        subject_id = cursor.fetchone()[0]
        subject_ids.append(subject_id)
    
    # Додавання студентів
    student_ids = []
    for _ in range(50):
        student_name = faker.name()
        group_id = random.choice(group_ids)  # Select from actual group_ids
        cursor.execute("INSERT INTO students (fullname, group_id) VALUES (%s, %s) RETURNING id", (student_name, group_id))
        student_id = cursor.fetchone()[0]
        student_ids.append(student_id)
    
    # Додавання оцінок для кожного студента
    for student_id in student_ids:
        for subject_id in subject_ids:
            for _ in range(random.randint(1, 20)):
                grade = random.randint(1, 12)
                grade_date = faker.date_between(start_date='-1y', end_date='today')
                cursor.execute("""
                    INSERT INTO grades (student_id, subject_id, grade, grade_date)
                    VALUES (%s, %s, %s, %s)
                """, (student_id, subject_id, grade, grade_date))

    conn.commit()

populate_db()

cursor.close()
conn.close()
