class StudentEngageError(Exception):
    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message
        super().__init__(self.message)


class DBError(Exception):
    def __init__(self, error_code: str, message: str):
        self.error_code = error_code
        self.message = message
        super().__init__(self.message)
