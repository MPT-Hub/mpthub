from .frame import Frame


class Trajectory():
    msd_mean = 0.00
    deff_mean = 0.00

    def __init__(self,
                 trajectory_number: int,
                 _frames: list(Frame) = []) -> None:

        self.trajectory_number = trajectory_number
        self.frames = _frames
        self.is_valid = False
        self.mean_squared_displacement = None
        self.diffusivity_coefficient = None

    def add_frame(self):
        self.frames.append(Frame())

    def compute_msd(self):
        pass

    def compute_deff(self):
        pass
