import dash_html_components as html
import dash_bootstrap_components as dbc

I3S_LOGO = "./assets/i3S_logo_transparent.png"


def Navbar(page_name: str = "Home"):

    navbar = dbc.Navbar(
        html.Div(children=[
            html.A(
                dbc.Row(children=[
                    dbc.Col(html.Img(src=I3S_LOGO, height="40px")),
                    dbc.Col(dbc.NavbarBrand(
                        "Multiple Particle Tracking Analysis",
                        className="ml-3"))],
                        align="center",
                        no_gutters=True),
                href="./"),
            html.Div(
                dbc.Row(
                    dbc.Col(
                        dbc.NavbarBrand(page_name,
                                        className="ml-3")),
                    no_gutters=True,
                    className="ml-auto flex-nowrap mt-3 mt-md-0",
                    align="center"))],
            className="container"),
        color="dark",
        dark=True,
        id="navbar")

    return navbar
