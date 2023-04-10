import json


class CpuModel:
    def __init__(self, cpu_name, score):
        self.cpu_name: str = cpu_name
        self.score: int = score

    def __str__(self):
        return f'CPU name - {self.cpu_name}, score - {self.score}'

    def __eq__(self, other):
        if type(self) is type(other):
            return self.cpu_name == other.cpu_name
        else:
            return False

    def __hash__(self):
        return hash(self.cpu_name)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


