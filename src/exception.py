import sys

def error_message_details(err, error_detail: sys):
    _, _, exc_tb = error_detail
    # by using this, we can find where actually the error occurred
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = 'Error occurred in script name [{0}] line number [{1}] error message [{2}]'.format(
        filename, exc_tb.tb_lineno, str(err)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details)

    def __str__(self):
        return self.error_message
