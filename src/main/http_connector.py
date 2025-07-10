import requests

def fetch_canvas_data():
    response = requests.get("http://127.0.0.1:8086/")  # adjust if running on another port
    return response.json()

def fetch_student_info_data():
    response = requests.get("http://127.0.0.1:9090/")  # adjust accordingly
    return response.json()
