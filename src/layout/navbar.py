# package imports
import dash_bootstrap_components as dbc

# local imports
from pages.home import home

# set contansts
toggler = 'id-navbar-toggler'
collapse = 'id-navbar-collapse'
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand(
                'Example',
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
                        # TODO remove the following NavItem
                        dbc.NavItem(
                            dbc.NavLink(
                                'About',
                                href='/about'
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
    sticky='fixed',
    color='primary',
    dark=True
)
