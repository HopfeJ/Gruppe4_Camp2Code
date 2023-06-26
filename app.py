from dash import Dash, html, dcc
import numpy as np
import pandas as pd
import plotly.express as px
import datetime

"""
    Daten aus CSV Datei in DataFrame holen
"""

df = pd.read_csv('fahrdaten.txt')

"""
    Berechnung der Gesamtfahrzeit
"""
df['Zeitstempel'] = pd.to_datetime(df['Zeitstempel'])
stamp_begin = df['Zeitstempel'][0]
stamp_end = df['Zeitstempel'][-1:]
print(type(stamp_end))
print(stamp_end)

travel_time = stamp_end - stamp_begin


print(travel_time)
print(type(travel_time))
"""
    Webseite erstellen
"""
app = Dash()
fig = px.line(df, x=df['Zeitstempel'], y=df['Geschwindigkeit'])

app.layout = html.Div(
    children=[
    html.H1(children='Fahrparcours_Gruppe4',
    style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40}), 
    html.P(children='Maximale Geschwindigkeit: ' + str(df['Geschwindigkeit'].max())),
    html.P(children='Minimale Geschwindigkeit: ' + str(df['Geschwindigkeit'].min())),
    html.P(children='Durchschnittsgeschwindigkeit: ' + str(df['Geschwindigkeit'].mean())),
    dcc.Graph(figure=fig)])













if __name__ == '__main__':
    app.run_server(host = '192.168.178.66', port=8080, debug=False)