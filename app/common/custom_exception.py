# import sys

# class CustomException(Exception):
#     def __init__(self, message: str, error_detail: Exception = None):
#         self.error_message = self.get_detailed_error_message(message, error_detail)
#         super().__init__(self.error_message)

#     @staticmethod
#     def get_detailed_error_message(message, error_detail):
#         _, _, exc_tb = sys.exc_info()
#         file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
#         line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
#         return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

#     def __str__(self):
#         return self.error_message

import traceback

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        if error_detail:
            tb = "".join(traceback.format_exception(type(error_detail), error_detail, error_detail.__traceback__))
            return f"{message}\nCaused by: {tb}"
        return message

    def __str__(self):
        return self.error_message
