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
        self.DB_NAME = 'config.db'
        self.BASE_PATH = Path.joinpath(Path.home(), ".mpt")
        self.DB_PATH = Path.joinpath(self.BASE_PATH, self.DB_NAME)
        self.EXPORT_PATH = Path.joinpath(self.BASE_PATH, "export")

        self.DEFAULT_OPEN_FOLDER = f"{Path.home()}"
        self.DEFAULT_SAVE_FOLDER = f"{Path.home()}"

        self.DEFAULT_IMMOBILE_MIN = 0.000
        self.DEFAULT_SUB_DIFFUSIVE_MIN = 0.200
        self.DEFAULT_DIFFUSIVE_MIN = 0.900
        self.DEFAULT_ACTIVE_MIN = 1.200

        self.DEFAULT_IMMOBILE_MAX = 0.199
        self.DEFAULT_SUB_DIFFUSIVE_MAX = 0.899
        self.DEFAULT_DIFFUSIVE_MAX = 1.199

        self.DEFAULT_P_SIZE = 200
        self.DEFAULT_MIN_FRAMES = 590
        self.DEFAULT_FPS = 30
        self.DEFAULT_TOTAL_FRAMES = 606
        self.DEFAULT_WIDTH_PX = 512
        self.DEFAULT_WIDTH_SI = 160

        self.MENU = {
            1: {
                "menu_name": "&File",
                "menu_items": {
                    1: {
                        "submenu_name": "&Open files",
                        "submenu_value": "Open ImageJ result file(s)",
                        "submenu_action": "on_mnuImport",
                        "submenu_visible": True
                    },
                    1: {
                        "submenu_name": "&Save reports",
                        "submenu_value": "Save analysis report files",
                        "submenu_action": "on_mnuExport",
                        "submenu_visible": False
                    }
                }
            },
            2: {
                "menu_name": "&Edit",
                "menu_items": {
                    1: {
                        "submenu_name": "App configuration",
                        "submenu_value": "General configuration",
                        "submenu_action": "on_mnuGeneral",
                        "submenu_visible": True,
                    },
                    2: {
                        "submenu_name": "Diffusivity configuration",
                        "submenu_value": "Diffusivity ranges configuration",
                        "submenu_action": "on_mnuDiffusivity",
                        "submenu_visible": True,
                    },
                    3: {
                        "submenu_name": "",
                        "submenu_value": "",
                        "submenu_action": "",
                        "submenu_visible": True,
                    },
                    4: {
                        "submenu_name": "Start analysis",
                        "submenu_value": "Starts MPT analysis",
                        "submenu_action": "on_mnuAnalysis",
                        "submenu_visible": False,
                    },
                    5: {
                        "submenu_name": "",
                        "submenu_value": "",
                        "submenu_action": "",
                        "submenu_visible": True,
                    },
                    6: {
                        "submenu_name": "Clear summary",
                        "submenu_value": "Clear current summary list",
                        "submenu_action": "on_mnuClear",
                        "submenu_visible": False,
                    },
                }
            },
            3: {
                "menu_name": "&Help",
                "menu_items": {
                    1: {
                        "submenu_name": "&Documentation",
                        "submenu_value": "Application documentation",
                        "submenu_action": "on_mnuHelp",
                        "submenu_visible": False
                    },
                    2: {
                        "submenu_name": "&About",
                        "submenu_value": "About this program",
                        "submenu_action": "on_mnuAbout",
                        "submenu_visible": False
                    },
                }
            }
        }
