from datetime import time, datetime
from constants.consts import TIME_FORMAT

class Note():
    def __init__(self, time: time, name: str, content: str):
        self.time = time
        self.name = name
        self.content = content

    @classmethod
    def from_json(cls, data):
        _time = datetime.strptime(data['time'], TIME_FORMAT)
        return cls(
                time    = _time, 
                name    = data['name'], 
                content = data['content'])

    def to_dict(self):
        time_beauty = self.time.strftime('%H.%M')
        return {
                'time' : time_beauty,
                'name' : self.name,
                'content' : self.content,
                }

    def display(self) -> None:
        time_beauty = self.time.strftime('%H.%M')
        print(
                f"\n{time_beauty} : {self.name}"
                f"\n    {self.content}"
                )
