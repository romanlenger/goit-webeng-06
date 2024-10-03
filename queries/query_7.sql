SELECT students.fullname, grades.grade, grades.grade_date
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group A'
AND subjects.name = 'Math';