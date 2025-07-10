import re

EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"

_seen_ids = set()

def is_valid(record: dict) -> bool:
    required_fields = ["student_id", "name", "email"]

    for field in required_fields:
        if not record.get(field):
            print(f"[Validation] Missing required field: {field}")
            return False

    if not re.match(EMAIL_REGEX, record["email"]):
        print(f"[Validation] Invalid email: {record['email']}")
        return False

    if record.get("total_engagement_minutes", 0) < 0:
        print(f"[Validation] Negative engagement time")
        return False

    return True
