from app.exceptions.error_messages import ZERO_DIVISION_ERROR


class DefaultException(Exception):
    pass


class ZeroDivisionException(ZeroDivisionError):
    def __init__(
            self,
            error_code: str,
            message: str = ZERO_DIVISION_ERROR,
            **kwargs
    ):
        super.__init__(**kwargs)
        self.message = message
        self.error_code = error_code

    def problem(self):
        return {
            'message': self.message,
            'error_code': self.error_code
        }
