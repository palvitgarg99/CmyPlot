# package imports
from dash import dcc, html
import dash_bootstrap_components as dbc

# set constants
path = '/upload'
title = 'Upload'
upload_id = 'id-upload-data'
info_id = 'id-upload-info'

layout = dbc.Container(
    [
        html.H1('Upload file'),
        html.Div(id=info_id),
        dcc.Upload(
            [
                'Drag and Drop or ',
                html.A('Select a File')
            ],
            # TODO move style to css component
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center'
            },
            id=upload_id
        )
    ]
)
