import dash_html_components as html
import dash_bootstrap_components as dbc
from gui.navbar import Navbar
from gui.footer import Footer
from gui.sidebar import Sidebar

nav = Navbar('Results')
sidebar = Sidebar("/result")
footer = Footer()

body_content = html.Div(children=[
    dbc.Row(
        dbc.Button("Export all reports",
                   id={'page': 'results', 'type': 'all'},
                   color="primary", className="text-center"),
        id="all-reports-div",
        className="mb-3"),
    dbc.Row(children=[
        dbc.Col(
            dbc.Button("Export Individual analysis report",
                       id={'page': 'results', 'type': 'individual'},
                       color="primary", className="text-center"),
            id="individual-div", className="text-left", width=4),
        dbc.Col(
            dbc.Button("Export Transport Mode report",
                       id={'page': 'results', 'type': 'transport-mode'},
                       color="primary", className="text-center"),
            id="transport-mode-div", className="text-center", width=4),
        dbc.Col(
            dbc.Button("Export Einstein-Stokes report",
                       id={'page': 'results', 'type': 'einstein-stokes'},
                       color="primary", className="text-center"),
            id="einstein-stokes-div", className="text-right", width=4)]),
    # html.P("Testing..."),
    # html.P(f"micro (mu): {chr(956)}"),
    # html.I(className="far fa-trash-alt"), html.Br(),
    # html.I(className="fas fa-trash-alt"), html.Br(),
    # html.I(className="fas fa-minus"), html.Br(),
    # html.I(className="fas fa-times"), html.Br(),
    # html.I(className="far fa-times-circle"), html.Br(),
    # html.I(className="fas fa-ban"), html.Br(),
    # html.I(className="fas fa-list-alt"), html.Br(),
    # html.I(className="fas fa-eye"), html.Br(),
    # html.I(className="far fa-chart-bar")
])

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
