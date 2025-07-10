from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, TIMESTAMP
from datetime import datetime

Base = declarative_base()

class StudentEngagement(Base):
    __tablename__ = "student_engagement"

    student_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    course_id = Column(String)
    course_name = Column(String)
    last_activity_date = Column(TIMESTAMP)
    total_engagement_minutes = Column(Integer)
    source_system = Column(String)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow)
