# import sqlite3
from sqlalchemy import create_engine
import pandas as pd
from mpt.settings import Settings
from pathlib import Path

settings = Settings()


def resolve_paths() -> None:
    if not Path(settings.BASE_PATH).exists():
        Path.mkdir(Path(settings.BASE_PATH))

    if not Path(settings.EXPORT_PATH).exists():
        Path.mkdir(Path(settings.EXPORT_PATH))


def connect():
    return create_engine(f"sqlite:///{settings.DB_PATH}")


def persist() -> str:
    """
    Perform table creation for the app, based on default data.
    If tables already exists, nothing is done.
    """
    resolve_paths()

    config_df = pd.DataFrame({
        'p_size': [settings.DEFAULT_P_SIZE],
        'min_frames': [settings.DEFAULT_MIN_FRAMES],
        'fps': [settings.DEFAULT_FPS],
        'total_frames': [settings.DEFAULT_TOTAL_FRAMES],
        'width_px': [settings.DEFAULT_WIDTH_PX],
        'width_si': [settings.DEFAULT_WIDTH_SI],
        'temperature_C': [settings.DEFAULT_TEMPERATURE_C],
        'time': [settings.DEFAULT_TIME],
        'immobile_max': [settings.DEFAULT_IMMOBILE_MAX],
        'diffusive_min': [settings.DEFAULT_DIFFUSIVE_MIN],
        'diffusive_max': [settings.DEFAULT_DIFFUSIVE_MAX],
        'open_folder': [settings.DEFAULT_OPEN_FOLDER],
        'save_folder': [settings.DEFAULT_SAVE_FOLDER]})

    trajectories_df = pd.DataFrame(
        columns=['file_name', 'trajectory', 'frame', 'x', 'y'])

    summary_df = pd.DataFrame(
        columns=['file_name', 'trajectories', 'valid'])

    msg = f"\n{create_table('config', config_df)}"
    msg += f"\n{create_table('trajectories', trajectories_df)}"
    msg += f"\n{create_table('summary', summary_df)}"
    msg += f"\n{update_table('summary', summary_df)}"
    msg += f"\n{update_table('config', config_df)}"
    return msg


def clear_table(table_name: str):
    pass


def update_table(table_name: str, data: pd.DataFrame,
                 column_names: list = None, replace_data: bool = False) -> str:
    """Updates a table based on received DataFrame. Ignores update if pandas \
        detect that the table is already updated.

    Arguments:
        table_name {str} -- Name of the table to be updated.
        data {pd.DataFrame} -- Data to be inserted.
    """

    conn = connect()
    table_df = None
    table_df = pd.read_sql_table(table_name, con=conn)
    msg = ""
    try:
        if column_names:
            data.rename(dict(zip(data.columns, column_names)), axis='columns')

        if replace_data or (table_df.columns.size != data.columns.size):
            for (column_name, column_data) in data.iteritems():
                if data[column_name].any() and table_df[column_name].any():
                    data[column_name] = column_data

            data.to_sql(table_name, con=conn,
                        index=False, if_exists='replace')

            msg = f"Table '{table_name}' updated."
    except KeyError:
        data.to_sql(table_name, con=conn,
                    index=False, if_exists='replace')
        msg = f"Table '{table_name}' updated."
    except Exception:
        msg = "Exception."
    finally:
        table_df = None
        return msg


def create_table(table_name: str, data: pd.DataFrame) -> str:
    """Creates table based on received DataFrame. Forces fail if pandas \
        detect that the table already exists.

    Arguments:
        table_name {str} -- Name of the table to be created.
        data {pd.DataFrame} -- Data to be inserted.
    """
    conn = connect()
    try:
        data.to_sql(table_name, con=conn, index=False, if_exists='fail')
        msg = f"Table '{table_name}' created."
    except ValueError:
        msg = f"Table '{table_name}' already exists. Aborting."
    except Exception:
        msg = "Exception."
    finally:
        return msg
