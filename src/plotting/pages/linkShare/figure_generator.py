import pickle
import pandas as pd
import plotly.express as px
from dash import exceptions

xaxis = ""
yaxis = ""
filename = ""


def make_graph():
    if filename != "":
        try:
            a_file = open(filename, "rb")
            output = pickle.load(a_file)
            # prep data

            if output == None:
                return px.scatter()
            df = pd.DataFrame(output['df'])

            if xaxis != "" and yaxis != "":
                figure = px.scatter(x=df[xaxis], y=df[yaxis])
            a_file.close()
            return figure
        except Exception as e:
            return px.scatter()
    else:
        return px.scatter()
