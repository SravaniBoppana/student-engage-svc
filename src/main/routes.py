from fastapi import APIRouter

from src.main.data_mapper import normalize_canvas, normalize_student_info
from src.main.http_connector import fetch_canvas_data, fetch_student_info_data
from src.main.repository import mock_upsert_student, mock_get_summary
from src.main.studentengageerror import StudentEngageError, DBError

router = APIRouter()


@router.get("/consolidate")
def consolidate():
    try:
        canvas_data = normalize_canvas(fetch_canvas_data())
        student_data = normalize_student_info(fetch_student_info_data())
    except StudentEngageError as e:
        return {"status": "error", "error_code": e.error_code, "message": e.message}

    all_records = canvas_data + student_data
    try:
        for record in all_records:
            mock_upsert_student(record)
    except DBError as e:
        return {"status": "error", "error_code": e.error_code, "message": e.message}

    return {"status": "success", "records_processed": len(all_records)}


@router.get("/summary")
def summary():
    """
    Return aggregated engagement summary by course.
    """
    try:
        data = mock_get_summary()
        return {"status": "success", "summary": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
