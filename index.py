import dash
import dash_core_components as dcc
import dash_html_components as html
# import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL
from dash.exceptions import PreventUpdate
from gui.home_page import Home_page
from gui.config_page import Config_page
from gui.import_page import Import_page, update_output
from gui.result_page import Result_page
from mpt import analysis as mpta
import json

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')])


# ----------------------------------------------------------------------- Route
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/config':
        return Config_page()
    elif pathname == "/import":
        return Import_page()
    elif pathname == '/result':
        return Result_page()
    else:
        return Home_page()
# -----------------------------------------------------------------------------


###############################################################################
# ------------------------------- Config page ------------------------------- #
###############################################################################
# ---------------------------------------------------------------- Sync sliders


@app.callback([Output("sub_diffusive", "value"),
               Output("active", "value")],
              [Input("immobile", "value"),
               Input("diffusive", "value")],
              [State("sub_diffusive", "value"),
               State("active", "value")])
def update_slider(immobile_value, diffusive_value,
                  sub_diffusive_value, active_value):

    # TODO: Review precision (add/subtract 0.001)
    new_subdiffusive_range = [immobile_value + 0.001,
                              diffusive_value[0] - 0.001]
    new_active_range = diffusive_value[1] + 0.001

    return new_subdiffusive_range, new_active_range
# -----------------------------------------------------------------------------

# ----------------------------------------------------------------- Save config


@app.callback(Output('hidden-div', 'children'),
              [Input('save_config', 'n_clicks')],
              [State('size', 'value'), State('fps', 'value'),
               State('width_px', 'value'), State('filter', 'value'),
               State('frames', 'value'), State('width_si', 'value'),
               State('immobile', 'value'), State('diffusive', 'value'),
               State('time', 'value')],
              prevent_initial_call=True)
def update_analysis_data(n_clicks,
                         size, fps, width_px, min_frames, frames, width_si,
                         immobile, diffusive, time):
    if n_clicks:
        config_list = [
            size, min_frames, fps, frames, width_px, width_si,
            mpta.config.temperature_C, time,
            immobile, diffusive[0], diffusive[1],
            mpta.config.open_folder, mpta.config.save_folder]

        success = mpta.config.update_from_list(config_list)

        if success:
            footer_classes = "fixed-bottom text-white bg-success"
            message = "Success! Configration saved."
        else:
            footer_classes = "fixed-bottom text-white bg-danger"
            message = "Something went wrong! Configration not saved."

        return (footer_classes, message)
# -----------------------------------------------------------------------------


###############################################################################
# ------------------------------- Import page ------------------------------- #
###############################################################################
# ---------------------------------------------------------------------- Upload
@app.callback([Output('output-data-upload', 'children'),
               Output('import-button-div', 'style')],
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')],
              prevent_initial_call=True)
def summarize_reports(list_of_contents, list_of_names):
    button_style = {"display": "none"}
    children = ""
    if list_of_contents is not None:
        summary, total = mpta.summarize(list_of_contents, list_of_names)

        if len(summary) > 0:
            button_style = {"display": "block"}

        children = update_output(summary, total)

    return children, button_style
# -----------------------------------------------------------------------------


# -------------------------------------------------------------- Manage summary
@app.callback(Output('url', 'pathname'),
              [Input({'type': 'report', 'index': ALL}, 'n_clicks'),
               Input({'page': 'import', 'type': ALL}, 'n_clicks')],
              prevent_initial_call=True)
def manage_summary(values, action):
    trigger = get_trigger(dash.callback_context)
    url = ""
    if trigger is not None:
        url = "/import"
    else:
        PreventUpdate
        return

    result = False
    if trigger == 'report' and not all(x is None for x in values):
        result = mpta.remove_report(values.index(1))

    elif trigger == 'clear':
        result = mpta.clear_summary()

    elif trigger == 'analysis':
        result = mpta.analyze()
        url = "/result"  # if result else "/import"

    print(result)
    return url


def get_trigger(context: dash.callback_context):
    trigger = None
    if context.inputs != {}:
        context_json = context.triggered[0]['prop_id'].split('.n_clicks')[0]
        trigger = json.loads(context_json)['type']

    return trigger
# -----------------------------------------------------------------------------


# ------------------------------------------------------------------ Status bar
# @app.callback([Output('footer', 'className'),
#                Output('status-bar', 'children')],
#               [Input('hidden-div', 'children')])
# def update_status(hidden_props):
#     footer_classes = "fixed-bottom text-white bg-primary"
#     message = ""

#     if hidden_props is not None:
#         footer_classes, message = hidden_props
#         if message == "reset":
#             message = ""

#     return footer_classes, message


# @app.callback(Output('status-interval', 'n_intervals'),
#               [Input('footer', 'className')])
# def reset_status_bar(num):
#     if num == 0:
#         raise PreventUpdate
#     else:
#         status_bar_props = None

#     return status_bar_props
# -----------------------------------------------------------------------------


def run_mpt():
    app.run_server(debug=True)


if __name__ == '__main__':
    run_mpt()
