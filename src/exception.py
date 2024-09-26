import sys

def error_message_details(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename 
    error_message = "Error occured [{0}], line: [{1}], exception: [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_details:sys):
        super().__init__(error_details)
        self.error_message = error_message_details(error, error_details)

    def __str__(self) -> str:
        return self.error_message
    