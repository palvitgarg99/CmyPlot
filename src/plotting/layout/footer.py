# package imports
from dash import html
import dash_bootstrap_components as dbc

# connstants
footer = html.Footer(
    dbc.Container(
        [
            html.A(
                [html.I(className="fab fa-github pr-1"), "Github"],
                href="https://github.com/ShreeSub/CmyPlot",
                target="_blank",
            ),
            html.Br(),
            html.A(
                [html.I(className="fas fa-at pr-1"), "Citation information"],
                href="https://zenodo.org/record/5634725",
                target="_blank",
            ),
        ]
    )
)
