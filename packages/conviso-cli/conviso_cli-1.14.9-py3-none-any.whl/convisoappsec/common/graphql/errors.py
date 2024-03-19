class Error(Exception):
    pass


class AuthenticationError(Error):
    pass


class ServerError(Error):
    pass


class ReponseError(Error):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code
