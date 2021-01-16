from .report import Report


class TransportModeReport(Report):

    def __init__(self) -> None:
        super().__init__()

    def create(self):
        print("Create method in Transport Mode class")

    def export(self):
        print("Export method in Transport Mode class")
