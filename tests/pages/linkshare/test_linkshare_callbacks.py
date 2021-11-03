import plotly
from src.plotting.pages.linkShare import figure_generator as fg


# Case when user tried to access some incorrect shared link
def test_incorrect_link_handling():
    # Throw error if no or wrong object type returned
    assert isinstance(fg.make_graph(), plotly.graph_objs._figure.Figure)


def test_fake_file_access_handling():
    fg.filename = "fake_file"
    assert isinstance(fg.make_graph(), plotly.graph_objs._figure.Figure)
