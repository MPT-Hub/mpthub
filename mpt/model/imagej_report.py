from .trajectory import Trajectory
import pandas as pd
import mpt.database as db


class ImageJReport:

    total_trajectory_count = 0
    total_valid_trajectory_count = 0

    def __init__(self,
                 _path: str = "",
                 _name: str = "",
                 _trajectories: list(Trajectory) = []) -> None:

        self.path = _path
        self.name = _name
        self.trajectories = _trajectories
        self.trajectory_count = 0
        self.valid_trajectory_count = 0

    def add_trajectory(self):
        self.trajectories.append(Trajectory())

    def update_trajectory_count(self, _new_trajectory_count: int) -> None:
        self.trajectory_count = _new_trajectory_count

    def update_valid_trajectory_count(
            self, _new_valid_trajectory_count: int) -> None:
        self.valid_trajectory_count = _new_valid_trajectory_count

    def save_to_DB(self):
        summary_df = pd.DataFrame({
            'full_path': self.full_path,
            'path': self.path,
            'file_name': self.file_name,
            'trajectory_count': self.trajectory_count,
            'valid_trajectory_count': self.valid_trajectory_count
        })

        conn = db.connect()
        summary_df.to_sql('summary', con=conn, index=False, if_exists='fail')
