import dash_html_components as html
import dash_bootstrap_components as dbc


def Footer():

    footer = dbc.Navbar(
        html.Div(
            html.P(id="status-bar",
                   className="m-0",
                   style={"height": 25}),
            className="container"),
        id="footer",
        color="primary",
        className="fixed-bottom text-white")

    return footer
