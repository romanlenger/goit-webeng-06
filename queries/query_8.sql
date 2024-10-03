SELECT AVG(grades.grade) AS avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.fullname = 'John Doe';
