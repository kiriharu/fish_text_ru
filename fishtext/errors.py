class TooManyContentExceeded(Exception):
    def __init__(self, message):
        super().__init__(message)


class CallLimitExceeded(Exception):
    def __init__(self, message):
        super().__init__(message)


class BannedForever(Exception):
    def __init__(self, message):
        super().__init__(message)


class InternalServerError(Exception):
    def __init__(self, message):
        super().__init__(message)


class TextFormatRequired(Exception):
    def __init__(self):
        super().__init__("Required text format in FishTextAPI class")
