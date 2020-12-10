import io
import base64
import pandas as pd


def clean_input(self, contents, name) -> pd.DataFrame:

    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in name:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')),
                usecols=[0, 1, 2, 3])

        elif 'xls' in name:
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            return pd.DataFrame()

    except Exception as e:
        print(e)
        return pd.DataFrame()

    return df
