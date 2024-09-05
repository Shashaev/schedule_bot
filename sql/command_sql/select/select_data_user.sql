WITH data_user AS (
    SELECT *
    FROM students
    WHERE students.user_name = %(user_name)s
)

SELECT *
FROM lessons
LEFT JOIN lecturers ON lessons.id_lecturer = lecturers.id
LEFT JOIN time_pairs ON lessons.id_time_pair = time_pairs.id 
WHERE `group` = (SELECT `group` FROM data_user)
AND (local_group = (SELECT local_group FROM data_user) OR local_group is NULL)
AND (local_group_english = (SELECT local_group_english FROM data_user) OR local_group_english is NULL) 
AND (parity_week = (SELECT parity_week FROM data_user) OR parity_week IS NULL)
AND lessons.day_week = %(day_week)s
