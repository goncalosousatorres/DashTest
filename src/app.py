from dash import Dash, dcc
import dash_bootstrap_components as dbc


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
mytext = dcc.Markdown(children="# Hello Ines")
app.layout = dbc.Container([mytext])
app.title = "Test Title"
app.run()
