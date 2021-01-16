from mpt.model.report import Report
from mpt.model.report_individual_analysis import IndividualAnalysisReport
from mpt.model.report_transport_mode import TransportModeReport
from mpt.model.report_einstein_stokes import EinsteinStokesReport
from mpt.model.config import Config
from mpt.model.imagej_report import ImageJReport
# import pandas as pd


class Analysis:

    def __init__(self,
                 analysis_configuration: Config = None,
                 imagej_reports: list(ImageJReport) = [],
                 reports: list(Report) = []) -> None:

        self.config = analysis_configuration
        self.imagej_reports = imagej_reports
        self.reports = reports

    def import_imagej_reports(self):
        self.reports.append(ImageJReport())
        pass

    def perform_analysis(self):
        pass

    def export_reports(self):
        pass

    def _create_reports(self):
        self.reports.append(IndividualAnalysisReport())
        self.reports.append(TransportModeReport())
        self.reports.append(EinsteinStokesReport())
