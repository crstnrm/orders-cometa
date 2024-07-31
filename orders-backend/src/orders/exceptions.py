class EOrderDoesNotExist(Exception):
    def __init__(self, message: str = "The order does not exist.") -> None:
        self.message = message
