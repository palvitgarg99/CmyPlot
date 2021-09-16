# package imports
from dash import dcc, html
import dash_bootstrap_components as dbc

# local imports

# set constants
# collapse functionality
toggler = 'id-options-toggler'
collapse = 'id-options-collapse'

# option inputs
x_att = 'id-options-x-att'
y_att = 'id-options-y-att'
color = 'id-options-color'
size = 'id-options-size'

title = 'id-options-title'
x_lab = 'id-options-x-lab'
y_lab = 'id-options-y-lab'
caption = 'id-options-caption'

graph_type = 'id-options-graph-type'

# body
card = dbc.Card(
    [
        dbc.CardHeader(
            html.H3(
                dbc.Button(
                    'Graph Options',
                    color='link',
                    id=toggler
                )
            )
        ),
        dbc.Collapse(
            dbc.CardBody(
                [
                    html.H4('Attributes'),
                    html.H6('X-Axis:'),
                    dcc.Dropdown(id=x_att),
                    html.H6('Y-Axis:'),
                    dcc.Dropdown(id=y_att),
                    html.H6('Color:'),
                    dcc.Dropdown(id=color),
                    html.H6('Size:'),
                    dcc.Dropdown(id=size),
                    html.Hr(),
                    html.H4('Labels'),
                    dcc.Markdown(
                        """
                        How to edit graph labels:

                        1. Click on the label you wish to edit.
                        1. Type the label contents.
                        1. Click enter.
                        """
                    ),
                    # It appears that all the labels are editable
                    # using the graph.config.editable flag.
                    # Leaving this code here incase we need more
                    # strict edit power.
                    #
                    # html.H6('Title:'),
                    # dcc.Input(
                    #     id=title,
                    #     type='text'
                    # ),
                    # html.H6('X Label:'),
                    # dcc.Input(
                    #     id=x_lab,
                    #     type='text'
                    # ),
                    # html.H6('Y Label:'),
                    # dcc.Input(
                    #     id=y_lab,
                    #     type='text'
                    # ),
                    # html.H6('Caption:'),
                    # dcc.Input(
                    #     id=caption,
                    #     type='text'
                    # ),
                    html.Hr(),
                    html.H4('Other'),
                    html.H6('Graph Type:'),
                    dcc.Dropdown(
                        id=graph_type
                    )
                ]
            ),
            id=collapse
        )
    ]
)
