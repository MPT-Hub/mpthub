from .report import Report


class EinsteinStokesReport(Report):

    def __init__(self) -> None:
        super().__init__()

    def create(self):
        print("Create method in Einstein Stokes class")

    def export(self):
        print("Export method in Einstein Stokes class")
