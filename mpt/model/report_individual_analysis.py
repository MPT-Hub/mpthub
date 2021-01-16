from .report import Report


class IndividualAnalysisReport(Report):

    def __init__(self) -> None:
        super().__init__()

    def create(self):
        print("Create method in Individual Analysis class")

    def export(self):
        print("Export method in Individual Analysis class")
