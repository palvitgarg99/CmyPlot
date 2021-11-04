import plotly
import pickle
from src.plotting.pages.linkShare import figure_generator as fg


# Case when user tried to access some incorrect shared link
def test_incorrect_link_handling():
    # Throw error if no or wrong object type returned
    assert isinstance(fg.make_graph(), plotly.graph_objs._figure.Figure)


def test_fake_file_access_handling():
    fg.filename = "fake_file"
    assert isinstance(fg.make_graph(), plotly.graph_objs._figure.Figure)


def test_dummy_file_access_handling():
    a_file = open("test.pkl", "wb+")
    data = {
        "df": [
            {
                "X0": 0.105462161,
                "X1": 0.025386467,
            },
            {
                "X0": -0.323946043,
                "X1": -0.180540713,
            },
            {
                "X0": -0.177804072,
                "X1": 0.041125761,
            },
            {
                "X0": -0.265325854,
                "X1": 0.199801246,
            },
            {
                "X0": -0.014840754,
                "X1": 0.126975545,
            },
            {
                "X0": -0.217654183,
                "X1": 0.313129246,
            },
        ]
    }
    pickle.dump(data, a_file)
    a_file.close()
    fg.filename = "test.pkl"
    assert isinstance(fg.make_graph(), plotly.graph_objs._figure.Figure)
