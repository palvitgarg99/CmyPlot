# package imports
from dash import html
import dash_bootstrap_components as dbc

# local imports
from pages.home import home
from pages.upload import upload
from pages.table import table
from pages.graph import graph

# set contansts
toggler = 'id-navbar-toggler'
collapse = 'id-navbar-collapse'
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand(
                [
                    html.I(className='far fa-chart-bar pr-1'),
                    'CmyPlot'
                ],
                href='/'
            ),
            dbc.NavbarToggler(id=toggler),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                home.title,
                                href=home.path
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                upload.title,
                                href=upload.path
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                table.title,
                                href=table.path
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                graph.title,
                                href=graph.path
                            )
                        )
                    ],
                    navbar=True
                ),
                id=collapse,
                navbar=True
            )
        ]
    ),
    sticky='fixed'
)
