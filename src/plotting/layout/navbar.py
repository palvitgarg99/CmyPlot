# package imports
from dash import html
import dash_bootstrap_components as dbc

# local imports
from src.plotting.pages.home import home
from src.plotting.pages.upload import upload
from src.plotting.pages.table import table
from src.plotting.pages.graph import graph

# set constants
toggler = "id-navbar-toggler"
collapse = "id-navbar-collapse"
LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("CmyPlot", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id=toggler),
            dbc.Col(
                dbc.Nav(
                    dbc.Container(dbc.NavItem(dbc.NavLink(home.title, href=home.path))),
                    navbar=True,
                ),
                width="auto",
            ),
            dbc.Col(
                dbc.Nav(
                    dbc.Container(
                        dbc.NavItem(dbc.NavLink(upload.title, href=upload.path))
                    ),
                    navbar=True,
                ),
                width="auto",
            ),
            dbc.Col(
                dbc.Nav(
                    dbc.Container(
                        dbc.NavItem(dbc.NavLink(table.title, href=table.path))
                    ),
                    navbar=True,
                ),
                width="auto",
            ),
            dbc.Col(
                dbc.Nav(
                    dbc.Container(
                        dbc.NavItem(dbc.NavLink(graph.title, href=graph.path))
                    ),
                    navbar=True,
                ),
                width="auto",
            ),
        ]
    ),
    color="dark",
    dark=True,
    sticky="fixed",
)
