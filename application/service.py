from db.client import Client


class Service:
    def __init__(self) -> None:
        self.db = Client()

