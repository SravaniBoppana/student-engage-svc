SELECT
    course_name,
    COUNT(DISTINCT student_id) AS student_count,
    AVG(total_engagement_minutes) AS avg_engagement_minutes,
    MIN(total_engagement_minutes) AS min_engagement_minutes,
    MAX(total_engagement_minutes) AS max_engagement_minutes,
    MAX(last_activity_date) AS last_activity
FROM
    "student_engagement"
GROUP BY
    course_name
ORDER BY
    avg_engagement_minutes DESC;
