import logging

import requests

from src.main.studentengageerror import StudentEngageError

logger = logging.getLogger("fetcher")



def fetch_canvas_data():
    try:
        logger.info(f"Fetching data from Canvas API: http://127.0.0.1:8086/")
        response = requests.get("http://127.0.0.1:8086/")

        if response.status_code != 200:
            logger.error(f"Canvas API returned status {response.status_code}")
            return []

        data = response.json()
        logger.info(f"Fetched {len(data)} records from Canvas API")
        return data

    except requests.exceptions.RequestException as e:
        logger.exception("Error fetching data from Canvas API")
        raise StudentEngageError("SE-001", "error fetching data from canvas api")

def fetch_student_info_data():
    try:
        logger.info(f"Fetching data from Student Info API: http://127.0.0.1:9090/")
        response = requests.get("http://127.0.0.1:9090/", timeout=5)

        if response.status_code != 200:
            logger.error(f"Student Info API returned status {response.status_code}")
            return []

        data = response.json()
        logger.info(f"Fetched {len(data)} records from Student Info API")
        return data

    except requests.exceptions.RequestException as e:
        logger.exception("Error fetching data from Student Info API")
        raise StudentEngageError("SE-002", "error fetching data from student info api")
