import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

df = pd.read_csv('C:/Users/lga/OneDrive/Pessoal/Acadêmico/FEUP/2019-2020-PDISS_DISS/_research/Results/20200218/ImageJ/561_H2O_200ul/561_D2_H2O_200ul_Series001_RAW_ch00.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)

# if __name__ == "__main__":

#     mpt_app = wx.App()
#     frame = mainWindow(parent=None)
#     frame.Show(True)
#     mpt_app.MainLoop()
