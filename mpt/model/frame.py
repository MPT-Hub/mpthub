class Frame(object):

    def __init__(self,
                 frame_number: int,
                 x_coordinate: float,
                 y_coordinate: float) -> None:
        self.id = frame_number
        self.x = x_coordinate
        self.y = y_coordinate
