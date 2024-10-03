SELECT students.fullname
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group A'; -- замініть на потрібну групу