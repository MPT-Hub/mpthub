import io
import base64
import pandas as pd
import numpy as np
from mpt import database as db
from timeit import default_timer as timer


class Config:

    def __init__(self) -> None:
        self._update_config()
        self.slider_marks = {0: {'label': '0.0'},
                             0.5: {'label': '0.5'},
                             1: {'label': '1.0'},
                             1.5: {'label': u'\u221E'}}

    def get_config(self) -> pd.DataFrame:
        conn = db.connect()
        config = pd.read_sql_table("config", conn).squeeze()

        return config

    def set_config(self, new_data: pd.DataFrame) -> bool:
        return True

    def update_from_list(self, new_data: list):
        new_data_df = pd.DataFrame([new_data], columns=self.get_config().index)

        message = db.update_table('config', new_data_df,
                                  list(new_data_df.columns), True)

        success = (len(message) > 0)
        if success:
            self._update_config()

        return success

    def _update_config(self):
        values = self.get_config()
        self.p_size = values.p_size
        self.fps = values.fps
        self.frame_count = values.total_frames
        self.frames_to_valid = values.min_frames
        self.width_px = values.width_px
        self.width_si = values.width_si
        self.temperature_C = values.temperature_C
        self.time = values.time
        self.immobile_max = values.immobile_max
        self.diffusive_min = values.diffusive_min
        self.diffusive_max = values.diffusive_max
        self.open_folder = values.open_folder
        self.save_folder = values.save_folder

        self.analysis = self._get_analysis_data()
        self.diffusivity = self._get_diffusivity_data()

    def _get_diffusivity_data(self):
        # TODO:Get data from DB
        diffusivity_data = {
            1: {"label": "Immobile",
                "html_for": "immobile",
                "input_id": "immobile",
                "min": 0,
                "max": 1.5,
                "step": 0.001,
                "range_value": self.immobile_max,
                "disabled": False, },
            2: {"label": "Sub-diffusive",
                "html_for": "sub_diffusive",
                "input_id": "sub_diffusive",
                "min": 0,
                "max": 1.5,
                "step": 0.001,
                "range_value": [self.immobile_max + 0.001,
                                self.diffusive_min - 0.001],
                "disabled": True, },
            3: {"label": "Diffusive",
                "html_for": "diffusive",
                "input_id": "diffusive",
                "min": 0,
                "max": 1.5,
                "step": 0.001,
                "range_value": [self.diffusive_min,
                                self.diffusive_max],
                "disabled": False, },
            4: {"label": "Active",
                "html_for": "active",
                "input_id": "active",
                "min": 0,
                "max": 1.5,
                "step": 0.001,
                "range_value": self.diffusive_max + 0.001,
                "disabled": True, }, }

        # d = {'label': [1, 2], 'col2': [3, 4]}
        # df = pd.DataFrame(data=diffusivity_data)
        # print(df.head())

        return diffusivity_data

    def _get_analysis_data(self):
        # TODO:Get data from DB
        analysis_data = {
            1: {"label": "Size (nm)",
                "html_for": "size",
                "input_type": "number",
                "input_id": "size",
                "input_value": self.p_size,
                "tip": "Particle size in 'nm'"},
            2: {"label": "FPS",
                "html_for": "fps",
                "input_type": "number",
                "input_id": "fps",
                "input_value": self.fps,
                "tip": "Video Frames Per Second"},
            3: {"label": "Width (px)",
                "html_for": "width_px",
                "input_type": "number",
                "input_id": "width_px",
                "input_value": self.width_px,
                "tip": "Video width in px"},
            4: {"label": "Filter",
                "html_for": "filter",
                "input_type": "number",
                "input_id": "filter",
                "input_value": self.frames_to_valid,
                "tip": """Minimum number of fraems to be considered a
                valid trajectory"""},
            5: {"label": "Frames",
                "html_for": "frames",
                "input_type": "number",
                "input_id": "frames",
                "input_value": self.frame_count,
                "tip": "Total frames in each video"},
            6: {"label": u"Width (\u03BCm)",
                "html_for": "width_si",
                "input_type": "number",
                "input_id": "width_si",
                "input_value": self.width_si,
                "tip": u"Video width in \u03BCm"},
            7: {"label": "Time (s)",
                "html_for": "time",
                "input_type": "number",
                "input_id": "time",
                "input_value": self.time,
                "tip": "Trajectory time to analyze"}, }

        # d = {'label': [1, 2], 'col2': [3, 4]}
        # df = pd.DataFrame(data=analysis_data)
        # print(df.head())

        return analysis_data


class Analysis():

    def __init__(self) -> None:
        self.config = Config()
        self.summary = pd.DataFrame(columns=["File", "Trajectory", "Valid"])
        self.summary_total = pd.DataFrame()
        self.trajectories = pd.DataFrame(
            columns=['Trajectory', 'Frame', 'x', 'y'])
        self.msd = pd.DataFrame()

        self.use_DB = False

    def summarize(self, file_data_list, file_name_list) -> pd.DataFrame:

        if self.use_DB:
            full_data = self._clean_import(file_data_list, file_name_list)
            summary = self._summarize(full_data)
            summary_total = self._summary_total(summary)

            return summary, summary_total
        else:
            # ----------------------------------------------------------- No DB
            self.trajectories = self._clean_import(file_data_list,
                                                   file_name_list)
            self.summary = self._summarize(self.trajectories)
            self.summary_total = self._summary_total(self.summary)

            return self.summary, self.summary_total

    def load_summary(self) -> pd.DataFrame:

        if self.use_DB:
            summary = pd.read_sql_table('summary', db.connect())
            summary_total = self._summary_total(summary)

            return summary, summary_total
        else:
            # ----------------------------------------------------------- No DB
            return self.summary, self.summary_total

    def load_msd(self) -> pd.DataFrame:

        if self.use_DB:
            msd = pd.read_sql_table('msd', db.connect())

            return msd
        else:
            # ----------------------------------------------------------- No DB
            return self.msd

    def remove_report(self, report_index: int) -> bool:

        if self.use_DB:
            summary, _ = self.load_summary()
            report_name = summary.iloc[report_index]['File']

            summary.drop(report_index, inplace=True)
            summary = summary.reset_index().drop('index', axis=1)
            # summary_total = self.__summary_total(summary)

            db.update_table(
                'summary', summary, ['file_name', 'trajectories', 'valid'],
                True)

            self._remove_trajectories(summary['File'])

            return True
        else:
            # ----------------------------------------------------------- No DB
            report_name = self.summary.iloc[report_index]['File']
            self.summary.drop(report_index, inplace=True)
            self.summary = self.summary.reset_index().drop('index', axis=1)
            self.summary_total = self._summary_total(self.summary)

            self._remove_trajectories(report_name)

            return True

    def clear_summary(self) -> bool:

        if self.use_DB:
            summary, _ = self.load_summary()
            summary.drop(summary.index, inplace=True)

            db.update_table('summary', summary,
                            ['file_name', 'trajectories', 'valid'], True)

            self._clear_trajectories()

            return True
        else:
            # ----------------------------------------------------------- No DB
            self.summary.drop(self.summary.index, inplace=True)

            self._clear_trajectories()

            return True

    def analyze(self) -> bool:
        self.msd = pd.DataFrame()
        self._sanitize_trajectories()

        time_step = 1 / self.config.fps
        max_time = self.config.frame_count / self.config.fps
        tau = np.linspace(time_step, max_time, self.config.frame_count)

        trajectories_group = self.trajectories.groupby(
            ['File', 'Trajectory'], as_index=False)

        msd_init = timer()
        i = 0
        msd = pd.DataFrame()
        for (file, trajectory), trajectory_data in trajectories_group:
            init = timer()
            pixel_size = self.config.width_px / self.config.width_si
            frames = len(trajectory_data)
            t = tau[:frames]
            xy = trajectory_data.values

            position = pd.DataFrame({"t": t, "x": xy[:, -2], "y": xy[:, -1]})
            shifts = position["t"].index.values + 1

            msdp = np.zeros(shifts.size)
            for k, shift in enumerate(shifts):
                diffs_x = position['x'] - position['x'].shift(-shift)
                diffs_y = position['y'] - position['y'].shift(-shift)
                square_sum = np.square(diffs_x) + np.square(diffs_y)
                msdp[k] = square_sum.mean()

            msdm = msdp * (1 / (pixel_size ** 2))
            msdm = msdm[:self.config.frames_to_valid]
            msd[i] = msdm

            end = timer()
            print(f"Time to proccess {i:0d}: {end - init}")

            i += 1

        tau = tau[:self.config.frames_to_valid]

        msd.insert(0, "tau", tau, True)
        msd = msd[msd[msd.columns[0]] < self.config.time]

        msd.name = "MSD"
        msd.set_index('tau', inplace=True)
        msd.index.name = f'Timescale ({chr(120591)}) (s)'
        msd.columns = [f'MSD {col}' for col in msd.columns.values]
        msd['mean'] = msd.mean(axis=1)

        msd_end = timer()
        print(f"Time to proccess: {msd_end - msd_init}")

        if self.use_DB:
            db.update_table('msd', msd.reset_index(),
                            msd.reset_index().columns.values,
                            True)
        else:
            self.msd = msd.reset_index()

        return (not msd.empty)

    def _clean_import(self, data_list, name_list) -> pd.DataFrame:

        full_data = pd.DataFrame()
        for content, name in zip(data_list, name_list):
            file_data = self._import(content, name)
            if file_data.empty:
                continue
            file_data.insert(0, "File", name, allow_duplicates=True)
            full_data = full_data.append(file_data)

        # --------------------------------------------------------------- No DB
        if self.use_DB:
            db.update_table('trajectories', full_data,
                            ['file_name', 'trajectories', 'frame', 'x', 'y'],
                            True)

        return full_data

    def _import(self, content, name) -> pd.DataFrame:

        content_type, content_string = content.split(',')
        decoded_data = base64.b64decode(content_string)

        try:
            if 'csv' in name:
                file_data = pd.read_csv(
                    io.StringIO(decoded_data.decode('utf-8')))
                return self._is_valid_csv(file_data)

            # elif 'txt' in name:
            #     df = pd.read_excel(io.BytesIO(decoded_data))

            # elif 'xls' in name:
            #     df = pd.read_excel(io.BytesIO(decoded_data))

            else:
                return pd.DataFrame()

        except Exception as e:
            print(e)
            return pd.DataFrame()

    def _is_valid_csv(self, df: pd.DataFrame) -> pd.DataFrame:
        is_valid = set(['Trajectory', 'Frame', 'x', 'y']).issubset(df.columns)
        if is_valid:
            return df.iloc[:, :4]
        else:
            return pd.DataFrame()

    def _summarize(self, full_data: pd.DataFrame) -> pd.DataFrame:

        grouped_data = full_data.groupby(
            ['File', 'Trajectory'], as_index=False).count()[
                ['File', 'Trajectory', 'Frame']]

        trajectories_per_file = grouped_data.groupby(
            ['File'], as_index=False).count()[
                ['File', 'Trajectory']]

        summary_valid = grouped_data[
            grouped_data['Frame'] > self.config.frames_to_valid].groupby(
                ['File'], as_index=False).count()[
                    ['File', 'Trajectory']].rename(
                        columns={'Trajectory': 'Valid'})

        summary = trajectories_per_file.merge(
            summary_valid, how='left').fillna(0)

        summary[['Trajectory', 'Valid']] = summary[
            ['Trajectory', 'Valid']].astype(int)

        if self.use_DB:
            db.update_table('summary', summary,
                            ['file_name', 'trajectories', 'valid'],
                            True)

        return summary

    def _summary_total(self, summary_data: pd.DataFrame) -> pd.Series:

        summary_total = summary_data.sum()
        summary_total['File'] = 'Total'

        return summary_total

    def _remove_trajectories(self, report: str) -> bool:
        trajectories = self._load_trajectories()

        # trajectories = trajectories[trajectories['File'] != report.values[0]]
        trajectories = trajectories[trajectories['File'] != report]

        if self.use_DB:
            db.update_table(
                'trajectories', trajectories,
                ['file_name', 'trajectories', 'frame', 'x', 'y'], True)

            return True
        else:
            # ----------------------------------------------------------- No DB
            self.trajectories = self.trajectories[
                self.trajectories['File'] != report]

            return True

    def _clear_trajectories(self) -> bool:
        trajectories = self._load_trajectories()
        trajectories.drop(trajectories.index, inplace=True)
        if self.use_DB:
            db.update_table(
                'trajectories', trajectories,
                ['file_name', 'trajectories', 'frame', 'x', 'y'], True)

            return True
        else:
            # ----------------------------------------------------------- No DB
            self.trajectories.drop(self.trajectories.index, inplace=True)

            return True

    def _load_trajectories(self) -> pd.DataFrame:

        if self.use_DB:
            return pd.read_sql_table('trajectories', db.connect())
        else:
            # ----------------------------------------------------------- No DB
            return self.trajectories

    def _sanitize_trajectories(self) -> None:
        # def __sanitize_trajectories(self) -> pd.DataFrame:

        trajectories = self._load_trajectories()
        grouped = trajectories.groupby(
            ['File', 'Trajectory'],
            as_index=False).count()[['File', 'Trajectory', 'Frame']]

        valid_trajectories = grouped[
            grouped['Frame'] > self.config.frames_to_valid].groupby(
            ['File', 'Trajectory'], as_index=False).count()

        valid_per_file_lst = list(zip(valid_trajectories['File'],
                                      valid_trajectories['Trajectory']))

        self.trajectories = trajectories[
            [x in valid_per_file_lst for x in list(
                zip(trajectories['File'], trajectories['Trajectory']))]]

        if self.use_DB:
            db.update_table('trajectories', self.trajectories,
                            ['file_name', 'trajectories', 'frame', 'x', 'y'],
                            True)

        # return full_valid_data
