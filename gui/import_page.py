import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from gui.navbar import Navbar
from gui.footer import Footer
from gui.sidebar import Sidebar
from mpt import analysis as mpta

nav = Navbar('ImageJ reports (import and summary)')
sidebar = Sidebar("/import")
footer = Footer()


def update_output(summary, total):
    table_content = ""
    summary['Remove'] = ""
    total['Remove'] = ""

    if len(summary) > 0:
        table_content = dbc.Table([
            html.Thead(
                html.Tr([
                    html.Th(
                        col if col != 'Remove' else '',
                        className="text-center")
                    for col in summary.columns]),
                className="text-white bg-primary"),
            html.Tbody([
                html.Tr([
                    html.Td(
                        (html.A(
                            href="#",
                            id={'type': 'report', 'index': index},
                            # id=f"trajectory-{i}",
                            className="text-danger far fa-trash-alt"))
                        if col == "Remove" else summary.iloc[index][col],
                        className="" if col == "File" else "text-center")
                    for col in summary.columns])
                for index in range(len(summary))]),
            html.Tfoot([
                html.Tr([
                    html.Th(
                        col,
                        className="text-right"
                        if col == ["Total"] else "text-center")
                    for col in total])],
                className="bg-light")],
            className="table-hover")

    return table_content


def Import_page():
    summary, total = mpta.load_summary()
    summary['Remove'] = ""
    total['Remove'] = ""

    button_style = {"display": "none"}
    table_content = ""
    if len(summary) > 0:
        button_style = {"display": "block"}

        table_content = update_output(summary, total)

        # table_content = dbc.Table([
        #     html.Thead(
        #         html.Tr([
        #             html.Th(
        #                 col if col != 'Remove' else '',
        #                 className="text-center")
        #             for col in summary.columns]),
        #         className="text-white bg-primary"),
        #     html.Tbody([
        #         html.Tr([
        #             html.Td(
        #                 (html.A(
        #                     href="#",
        #                     id={'type': 'report', 'index': index},
        #                     # id=f"trajectory-{i}",
        #                     className="text-danger far fa-trash-alt"))
        #                 if col == "Remove" else summary.iloc[index][col],
        #                 className="" if col == "File" else "text-center")
        #             for col in summary.columns])
        #         for index in range(len(summary))]),
        #     html.Tfoot([
        #         html.Tr([
        #             html.Th(
        #                 col,
        #                 className="text-right"
        #                 if col == ["Total"] else "text-center")
        #             for col in total])],
        #         className="bg-light")],
        #     className="table-hover")

    output_div = html.Div(id="analysis-progress", style={"display": "none"})

    body_content = html.Div(children=[
        dcc.Loading(children=[
            output_div,
            html.Div(table_content, id="output-data-upload"),
            dbc.Row(children=[
                dbc.Col(
                    dbc.Button("Clear summary",
                               id={'page': 'import', 'type': 'clear'},
                               color="danger", className="text-left"),
                    id="clear_summary_div",
                    className="text-left",
                    style=button_style),
                dbc.Col(
                    dbc.Button("Start analysis",
                               id={'page': 'import', 'type': 'analysis'},
                               color="primary", className="text-right"),
                    id="start_analysis_div",
                    className="text-right",
                    style=button_style)
            ], id="import-button-div")
        ], id="", style={"marginTop": '21vh', "width": "7rem", "height": "7rem"})])

    upload_area = html.Div(
        dcc.Upload(
            id='upload-data',
            className='m-0 row align-items-center',
            children=html.Div(['Drag and Drop or ',
                               html.Br(),
                               html.A('Select Files')],
                              className='container-fluid'),
            style={
                # 'width': '100%',
                'height': '240px',
                #    'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center'},
            multiple=True,
            accept=".csv"),
        className='p-0 container-fluid')

    body = html.Div(
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Row(sidebar, className="m-0"),
                dbc.Row(upload_area, className='m-0 mt-3')],
                id="sidebar", width=3),
            dbc.Col(body_content, width=9)]),
        className="container mt-3")

    layout = html.Div(children=[
        nav,
        body,
        footer])

    return layout
