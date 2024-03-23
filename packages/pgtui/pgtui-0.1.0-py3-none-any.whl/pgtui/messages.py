from textual.message import Message


class RunQuery(Message):
    def __init__(self, query: str):
        self.query = query
        super().__init__()
