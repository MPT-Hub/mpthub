import dash_html_components as html
import dash_bootstrap_components as dbc


def Sidebar(active="/"):

    font_style = {"fontSize": "1.1rem"}
    sidebar = dbc.Nav(children=[
        dbc.NavItem(
            dbc.NavLink(children=[
                html.I(className="pr-2 fas fa-home"), "Home"],
                style=font_style,
                href="/", active=(active == '/' or False))),
        dbc.NavItem(
            dbc.NavLink(children=[
                html.I(className="pr-2 fas fa-sliders-h"), "Configurations"],
                style=font_style,
                href="/config", active=(active == '/config' or False))),
        dbc.NavItem(
            dbc.NavLink(children=[
                html.I(className="pr-2 fas fa-upload"), "Import reports"],
                style=font_style,
                href="/import", active=(active == '/import' or False))),
        dbc.NavItem(
            dbc.NavLink(children=[
                html.I(className="pr-2 far fa-chart-bar"), "Results"],
                style=font_style,
                href="/result", active=(active == '/result' or False)))],
        vertical="md",
        pills=True,
        className="container-fluid pl-0 pr-0",
        id="sidebar")

    return sidebar
