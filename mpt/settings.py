from pathlib import Path
import os
import sys


class Settings():
    def __init__(self) -> None:

        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        else:
            application_path = os.path.dirname(
                Path(os.path.abspath(__file__)).parent)

        self.APP_PATH = application_path
        self.ICON_PATH = os.path.join(self.APP_PATH, "mpt", "assets")
        self.DB_NAME = 'mpt.db'
        # self.BASE_PATH = Path.joinpath(Path.home(), ".mpt")
        self.BASE_PATH = os.path.join(self.APP_PATH, "data")
        self.DB_PATH = os.path.join(self.BASE_PATH, self.DB_NAME)
        self.EXPORT_PATH = os.path.join(self.BASE_PATH, "export")

        self.DEFAULT_OPEN_FOLDER = f"{Path.home()}"
        self.DEFAULT_SAVE_FOLDER = f"{Path.home()}"

        self.DEFAULT_DIFFUSIVE_MIN = 0.900
        self.DEFAULT_IMMOBILE_MAX = 0.199
        self.DEFAULT_DIFFUSIVE_MAX = 1.199

        self.DEFAULT_P_SIZE = 200
        self.DEFAULT_MIN_FRAMES = 590
        self.DEFAULT_FPS = 30
        self.DEFAULT_TOTAL_FRAMES = 606
        self.DEFAULT_WIDTH_PX = 512
        self.DEFAULT_WIDTH_SI = 160.01
        self.DEFAULT_TEMPERATURE_C = 37.01
        self.DEFAULT_TIME = 10.01
