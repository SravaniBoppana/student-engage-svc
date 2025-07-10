def normalize_canvas(documents):
    return [
        {
            "student_id": data["student_id"],
            "name": data["name"],
            "email": data["email"],
            "course_id": data["course_id"],
            "course_name": data["course_name"],
            "last_activity_date": data["last_activity"],
            "total_engagement_minutes": data["engagement_time"],
            "source_system": "canvas_system"
        }
        for data in documents
    ]

def normalize_student_info(documents):
    return [
        {
            "student_id": data["id"],
            "name": data["full_name"],
            "email": data["email_address"],
            "course_id": data["course"]["id"],
            "course_name": data["course"]["name"],
            "last_activity_date": data["activity_log"]["last_seen"],
            "total_engagement_minutes": data["activity_log"]["engagement"],
            "source_system": "student_info_system"
        }
        for data in documents
    ]
