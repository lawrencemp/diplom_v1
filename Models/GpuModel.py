import json


class GpuModel:
    def __init__(self, gpu_name, score):
        self.gpu_name: str = gpu_name
        self.score: int = score

    def __str__(self):
        return f'GPU name - {self.gpu_name}, score - {self.score}'

    def __eq__(self, other):
        if type(self) is type(other):
            return self.gpu_name == other.gpu_name
        else:
            return False

    def __hash__(self):
        return hash(self.gpu_name)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

