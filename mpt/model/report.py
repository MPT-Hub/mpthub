import abc


class Report(abc.ABC):

    def __init__(self, _name: str = "") -> None:
        self.name = _name
        self.sheets = []

    @abc.abstractmethod
    def create(self):
        print("Create method in Report class")

    @abc.abstractmethod
    def export(self):
        print("Export method in Report class")
