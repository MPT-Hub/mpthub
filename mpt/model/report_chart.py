import xlsxwriter


class ReportChart(xlsxwriter.chart):

    def __init__(self):
        super().__init__()
        self.sheet = None
        self.type = None
