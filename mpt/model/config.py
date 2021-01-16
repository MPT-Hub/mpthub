from mpt.settings import Settings


class Config:

    def __init__(self, configuration: dict = None) -> None:
        default_config = Settings()
        # TODO: Check if there is saved configs and import them
        # self.load_config()

        # TODO: Refactor this attribution
        self.total_frames = (configuration['total_frames'] or
                             default_config['DEFAULT_TOTAL_FRAMES'])
        self.frames_to_be_valid = (configuration['frames_to_be_valid'] or
                                   default_config['DEFAULT_MIN_FRAMES'])
        self.fps = (configuration['fps'] or
                    default_config['DEFAULT_FPS'])
        self.video_width_in_px = (configuration['video_width_in_px'] or
                                  default_config['DEFAULT_WIDTH_PX'])
        self.video_width_in_si = (configuration['video_width_in_si'] or
                                  default_config['DEFAULT_WIDTH_SI'])
        self.particle_size_in_nm = (configuration['particle_size_in_nm'] or
                                    default_config['DEFAULT_P_SIZE'])
        self.analysis_time_in_s = (configuration['analysis_time_in_s'] or
                                   default_config['DEFAULT_TIME'])
        self.temperature_in_C = (configuration['temperature_in_C'] or
                                 default_config['DEFAULT_TEMPERATURE_C'])

        self.import_path = (configuration['import_path'] or
                            default_config['DEFAULT_OPEN_FOLDER'])
        self.export_path = (configuration['export_path'] or
                            default_config['DEFAULT_SAVE_FOLDER'])

        self.immobile_min = (configuration[''] or
                             default_config['DEFAULT_IMMOBILE_MIN'])
        self.immobile_max = (configuration[''] or
                             default_config['DEFAULT_IMMOBILE_MAX'])
        self.sub_diffusive_min = (configuration[''] or
                                  default_config['DEFAULT_SUB_DIFFUSIVE_MIN'])
        self.sub_diffusive_max = (configuration[''] or
                                  default_config['DEFAULT_SUB_DIFFUSIVE_MAX'])
        self.diffusive_min = (configuration[''] or
                              default_config['DEFAULT_DIFFUSIVE_MIN'])
        self.diffusive_max = (configuration[''] or
                              default_config['DEFAULT_DIFFUSIVE_MAX'])
        self.active_min = (configuration[''] or
                           default_config['DEFAULT_ACTIVE_MIN'])

    def _set_config(self, config, value):
        pass

    def load_config(self):
        pass

    def update_config(self):
        pass
