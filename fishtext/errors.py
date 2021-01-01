class TooManyContentExceededError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CallLimitExceededError(Exception):
    def __init__(self, message):
        super().__init__(message)


class BannedForeverError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InternalServerError(Exception):
    def __init__(self, message):
        super().__init__(message)


class TextFormatRequired(Exception):
    def __init__(self):
        super().__init__("Required text format in FishTextAPI class")
