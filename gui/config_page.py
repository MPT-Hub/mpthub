import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from mpt import analysis as mpta
from gui.navbar import Navbar
from gui.footer import Footer
from gui.sidebar import Sidebar

nav = Navbar('Configurations')
sidebar = Sidebar("/config")
footer = Footer()


def Config_page():

    analysis_input_list = dbc.Form(children=[
        dbc.FormGroup(children=[
            dbc.Label(
                input_item["label"],
                html_for=input_item["html_for"],
                width=6),
            dbc.Col(
                dbc.Input(type=input_item["input_type"],
                          id=input_item["input_id"],
                          value=input_item["input_value"],
                          placeholder=input_item["tip"]),
                width=6)],
            row=True) for input_item in mpta.config.analysis.values()])

    analysis_card = dbc.Card(children=[
        dbc.CardHeader(children=[
            html.H5("Analysis and video properties",
                    className="card-title"),
            html.Span("Configurations that affect the analysis.")]),
        dbc.CardBody(analysis_input_list)])

    diffusivity_input_list = dbc.Form(children=[
        dbc.FormGroup(children=[
            dbc.Label(mpta.config.diffusivity[1]["label"],
                      html_for=mpta.config.diffusivity[1]["html_for"],
                      width=5),
            dbc.Col(
                dcc.Slider(
                    id=mpta.config.diffusivity[1]["input_id"],
                    min=mpta.config.diffusivity[1]["min"],
                    max=mpta.config.diffusivity[1]["max"],
                    step=mpta.config.diffusivity[1]["step"],
                    marks=mpta.config.slider_marks,
                    value=mpta.config.diffusivity[1]["range_value"],
                    tooltip={"always_visible": True, "placement": "top"},
                    disabled=mpta.config.diffusivity[1]["disabled"]),
                width=7)],
            row=True),
        dbc.FormGroup(children=[
            dbc.Label(
                mpta.config.diffusivity[2]["label"],
                html_for=mpta.config.diffusivity[2]["html_for"],
                width=5),
            dbc.Col(
                dcc.RangeSlider(
                    id=mpta.config.diffusivity[2]["input_id"],
                    min=mpta.config.diffusivity[2]["min"],
                    max=mpta.config.diffusivity[2]["max"],
                    step=mpta.config.diffusivity[2]["step"],
                    marks=mpta.config.slider_marks,
                    value=mpta.config.diffusivity[2]["range_value"],
                    tooltip={"always_visible": True, "placement": "top"},
                    disabled=mpta.config.diffusivity[2]["disabled"]),
                width=7)],
            row=True),
        dbc.FormGroup(children=[
            dbc.Label(
                mpta.config.diffusivity[3]["label"],
                html_for=mpta.config.diffusivity[3]["html_for"],
                width=5),
            dbc.Col(
                dcc.RangeSlider(
                    id=mpta.config.diffusivity[3]["input_id"],
                    min=mpta.config.diffusivity[3]["min"],
                    max=mpta.config.diffusivity[3]["max"],
                    step=mpta.config.diffusivity[3]["step"],
                    marks=mpta.config.slider_marks,
                    value=mpta.config.diffusivity[3]["range_value"],
                    tooltip={"always_visible": True, "placement": "top"},
                    disabled=mpta.config.diffusivity[3]["disabled"]),
                width=7)],
            row=True),
        dbc.FormGroup(children=[
            dbc.Label(
                mpta.config.diffusivity[4]["label"],
                html_for=mpta.config.diffusivity[4]["html_for"],
                width=5),
            dbc.Col(
                dcc.Slider(
                    id=mpta.config.diffusivity[4]["input_id"],
                    min=mpta.config.diffusivity[4]["min"],
                    max=mpta.config.diffusivity[4]["max"],
                    step=mpta.config.diffusivity[4]["step"],
                    marks=mpta.config.slider_marks,
                    value=mpta.config.diffusivity[4]["range_value"],
                    tooltip={"always_visible": True, "placement": "top"},
                    disabled=mpta.config.diffusivity[4]["disabled"]),
                width=7)],
            row=True)])

    diffusivity_card = dbc.Card(children=[
        dbc.CardHeader(children=[
            html.H5("Diffusivity ranges",
                                className="card-title"),
            html.Span("Set the desired diffusivity ranges.")]),
        dbc.CardBody(diffusivity_input_list)])

    cards = dbc.CardDeck(children=[
        analysis_card,
        diffusivity_card],
        className="container m-0 p-0")

    output_div = html.Div(id="hidden-div", style={"display": "none"})

    body_content = html.Div(children=[
        dcc.Interval(id="status-interval",
                     interval=3000,
                     disabled=False,
                     n_intervals=0,
                     max_intervals=1),
        dcc.Loading(
            html.Div(cards, id="config_div"),
            # color='primary',
            # type="cube",
            style={"marginTop": '21vh', "width": "7rem", "height": "7rem"}),
        html.Div(
            dbc.Button("Save", id="save_config",
                       color="primary", className="text-right"),
            id="save_config_div",
            className="m-3 text-right")])

    body = html.Div(
        dbc.Row(children=[
            dbc.Col(
                dbc.Row(sidebar, className="m-0"),
                id="sidebar", width=3),
            dbc.Col(children=[output_div, body_content], width=9)]),
        className="container mt-3")

    layout = html.Div([
        nav,
        body,
        footer])

    return layout
