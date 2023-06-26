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
stamp_begin = df['Zeitstempel'].iloc[0] # iloc = indexlocation, greift auf das erste Element der Spalte zu
stamp_end = df['Zeitstempel'].iloc[-1]
travel_time = stamp_end - stamp_begin
total_drive_time = travel_time.total_seconds() # Datentyp float


"""
    Berechnen der einzelnen Fahrzeiten
"""
df['Zeitdifferenzen'] = df['Zeitstempel'].diff().dt.total_seconds().shift(-1)

"""
    Berechnen der Fahrstrecke
"""
df['Strecke'] = df['Zeitdifferenzen'] * df['Geschwindigkeit']

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
    html.P(children='Gesamtfahrzeit: ' + str(total_drive_time)),
    html.P(children='Gesamtstrecke: ' + str(df['Strecke'].sum())),
    html.P(children='Durchschnittsgeschwindigkeit: ' + str(df['Strecke'].sum())), # Hier fehlt noch was !!!
    dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run_server(host = '192.168.178.66', port=8080, debug=False)