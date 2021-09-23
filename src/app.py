# package imports
import dash
import dash_bootstrap_components as dbc
from flask_caching import Cache

# local imports
from layout.layout import layout

# create app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True,
    title='CmyPlot'
)

# set up cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

# set initial layout
app.layout = layout
