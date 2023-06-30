from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import datetime
import dash_bootstrap_components as dbc
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
    Berechnen der Durschnittsgeschwindigkeit
"""
average_speed = df['Strecke'].sum() / total_drive_time

"""
Grafische Aufbereitung der Strecke
"""
df['Strecke_Grafik'] = df['Strecke'].shift(1).cumsum()
df['Strecke_Grafik'].iloc[0] = 0
print(df)


"""
    Webseite erstellen
"""
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    children=[
    html.H1(children='Fahrparcours_Gruppe4',
    style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40}), 
    html.P(children='Maximale Geschwindigkeit: ' + str(df['Geschwindigkeit'].max())),
    html.P(children='Minimale Geschwindigkeit: ' + str(df['Geschwindigkeit'].min())),
    html.P(children='Gesamtfahrzeit: ' + str(total_drive_time)),
    html.P(children='Gesamtstrecke: ' + str(df['Strecke'].sum())),
    html.P(children='Durchschnittsgeschwindigkeit: ' + str(average_speed)),
    dcc.Dropdown(id='dropdown', options=[
        {'label': 'Geschwindigkeit', 'value': 'Geschwindigkeit'},
        {'label': 'Fahrtrichtung', 'value': 'Fahrtrichtung'},
        {'label': 'Lenkwinkel', 'value': 'Lenkwinkel'},
        {'label': 'Abstand', 'value': 'Abstand'},
        {'label': 'Strecke', 'value': 'Strecke_Grafik'},
    ], value = 'Geschwindigkeit' ),
    dcc.Graph(id='line_plot')])

@app.callback(
    Output(component_id='line_plot', component_property='figure'),
    Input(component_id='dropdown', component_property='value'))
def graph_update(value_of_input_component):
    print(value_of_input_component)
    fig = px.line(df, x=df['Zeitstempel'], y=df[value_of_input_component])
    return fig


if __name__ == '__main__':
    app.run_server(host = '127.0.0.1', port=8080, debug=False)