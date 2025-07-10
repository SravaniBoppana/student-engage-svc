import logging
from datetime import datetime

from src.main.db_connection import SessionLocal
from src.main.model import StudentEngagement
from src.main.studentengageerror import DBError
from src.main.validation import is_valid

"""from sqlalchemy import func

from src.db_connection import SessionLocal
from src.model import StudentEngagement"""

_mock_db = []

"""
Mock Db call
"""


def mock_upsert_student(record: dict):
    global _mock_db
    existing = next((item for item in _mock_db if item["student_id"] == record["student_id"]), None)
    if existing:
        _mock_db = [item for item in _mock_db if item["student_id"] != record["student_id"]]
        record["updated_at"] = datetime.utcnow()
        _mock_db.append(record)
    else:
        record["updated_at"] = datetime.utcnow()
        _mock_db.append(record)


"""
Real Db call
"""


def upsert_student(record: dict):
    if is_valid(record):
        db = SessionLocal()
        try:
            existing = db.query(StudentEngagement).filter_by(student_id=record["student_id"]).first()
            if existing:
                for key, value in record.items():
                    setattr(existing, key, value)
                existing.updated_at = datetime.utcnow()
            else:
                new_student = StudentEngagement(**record)
                db.add(new_student)

            db.commit()
        except Exception as e:
            db.rollback()
            logging.error(f"Error connecting to db: {e}", exc_info=True)
            raise DBError("SE-100", f"error updating student records")
        finally:
            db.close()


"""
Mock db fetch call
"""


def mock_get_summary():
    summary = {}
    for record in _mock_db:
        course = record["course_name"]
        if course not in summary:
            summary[course] = {"count": 0, "total": 0}
        summary[course]["count"] += 1
        summary[course]["total"] += record["total_engagement_minutes"]

    return [
        {
            "course_name": c,
            "student_count": s["count"],
            "avg_engagement_minutes": round(s["total"] / s["count"], 2)
        } for c, s in summary.items()
    ]


"""
def get_summary():
    db = SessionLocal()
    try:
        results = db.query(
            StudentEngagement.course_name,
            func.count(StudentEngagement.student_id).label("student_count"),
            func.avg(StudentEngagement.total_engagement_minutes).label("avg_minutes")
        ).group_by(StudentEngagement.course_name).all()

        return [
            {
                "course_name": row[0],
                "student_count": row[1],
                "avg_engagement_minutes": round(row[2], 2)
            }
            for row in results
        ]
    finally:
        db.close()
"""
