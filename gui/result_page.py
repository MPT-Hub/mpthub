import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from gui.navbar import Navbar
from gui.footer import Footer
from gui.sidebar import Sidebar

nav = Navbar('Results')
sidebar = Sidebar("/result")
footer = Footer()

body_content = html.Div(children=[
    dbc.Row(children=[
        dbc.Col(
            dbc.Button("Export all reports",
                       id={'page': 'results', 'type': 'all'},
                       color="primary", className="text-center"))],
            id="all-reports-div",
            className="mb-3 text-right"),
    dbc.Row(children=[
        dbc.Col(
            dcc.Tabs(children=[
                dcc.Tab(label='Individual analysis', children=[

                    dbc.Row(dbc.Col(
                        dcc.Graph(
                            figure={'data': [
                                {'x': [1, 2, 3], 'y': [4, 1, 2],
                                    'type': 'bar', 'name': 'SF'},
                                {'x': [1, 2, 3], 'y': [2, 4, 5],
                                    'type': 'bar', 'name': u'Montréal'}]}),
                    )),

                    dbc.Row(
                        dbc.Col(
                            dbc.Button("Export 1",
                                       id={'page': 'results',
                                           'type': 'individual'},
                                       color="primary",
                                       className="text-center")),
                        className="text-right",
                        style={'margin-top': '-115px'})]),

                dcc.Tab(label='Transport Mode', children=[

                    dbc.Row(dbc.Col(
                        dcc.Graph(
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [1, 4, 1],
                                     'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [1, 2, 3],
                                     'type': 'bar', 'name': u'Montréal'}]}),
                    )),

                    dbc.Row(
                        dbc.Col(
                            dbc.Button("Export 2",
                                       id={'page': 'results',
                                           'type': 'transport-mode'},
                                       color="primary",
                                       className="text-center")),
                        className="text-right",
                        style={'margin-top': '-115px'})]),

                dcc.Tab(label='Einstein-Stokes', children=[

                    dbc.Row(dbc.Col(
                        dcc.Graph(
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [2, 4, 3],
                                     'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [5, 4, 3],
                                     'type': 'bar', 'name': u'Montréal'}]}),
                    )),

                    dbc.Row(
                        dbc.Col(
                            dbc.Button("Export 3",
                                       id={'page': 'results',
                                           'type': 'einstein-stokes'},
                                       color="primary",
                                       className="text-center")),
                        className="text-right",
                        style={'margin-top': '-115px'})]), ]))])])

body = html.Div(
    dbc.Row(children=[
        dbc.Col(sidebar, id="sidebar", width=3),
        dbc.Col(body_content, width=9)]),
    className="container mt-3")


def Result_page():
    layout = html.Div([
        nav,
        body,
        footer])

    return layout
