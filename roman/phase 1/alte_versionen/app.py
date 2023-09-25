from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as nd
import os


os.chdir("/home/pi/Gruppe4_Camp2Code/roman")

# Datenauswertung

df = pd.read_csv("roman_fahrdaten.txt")
#print(df)

df = df[~df["Reason"].isin(["supersonic_sensor_error", "Hinderniss"])] # nur Fahrzeiten
df = df[df["Direction"] > 0] # nur Vorwärtsfahrten
print(df)

# Gesamtfahrzeit:
df['Zeitstempel'] = pd.to_datetime(df['Zeitstempel'])
stamp_begin = df['Zeitstempel'].iloc[0] # iloc = indexlocation, greift auf das erste Element der Spalte zu
stamp_end = df['Zeitstempel'].iloc[-1]
travel_time = stamp_end - stamp_begin
total_drive_time = travel_time.total_seconds() # Datentyp float

# Gesamte zurückgelegte Strecke:
df['Zeitdifferenzen'] = df['Zeitstempel'].diff().dt.total_seconds().shift(-1)
df['Strecke'] = df['Zeitdifferenzen'] * df['Speed']
print(df)

# Min, Max Speed
max_speed = df["Speed"].max()
min_speed = df[df["Speed"] > 0]["Speed"].min()
avg_speed = df['Strecke'].sum() / total_drive_time

df['Strecke_Grafik'] = df['Strecke'].shift(1).cumsum()
df['Strecke_Grafik'].iloc[0] = 0 # auf Null setzen, damit es im Ursprung startet

print("Max Speed:", max_speed)
print("Min Speed:", min_speed)
print("Avg Speed:", avg_speed)
print("Gesamtstrecke:", df['Strecke'].sum())
print("Total Traveltime:", total_drive_time)

"""
    Webseite erstellen
"""
app = Dash()

app.layout = html.Div(
    children=[
    html.H1(children='Fahrparcours_Gruppe4',
    style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40}), 
    html.P(children='Maximale Geschwindigkeit: ' + str(df['Speed'].max())),
    html.P(children='Minimale Geschwindigkeit: ' + str(df['Speed'].min())),
    html.P(children='Gesamtfahrzeit: ' + str(total_drive_time)),
    html.P(children='Gesamtstrecke: ' + str(df['Strecke'].sum())),
    html.P(children='Durchschnittsgeschwindigkeit: ' + str(avg_speed)),
    dcc.Dropdown(id='dropdown', options=[
        {'label': 'Geschwindigkeit', 'value': 'Speed'},
        {'label': 'Fahrtrichtung', 'value': 'Direction'},
        {'label': 'Lenkwinkel', 'value': 'Steering_Angle'},
        {'label': 'Abstand', 'value': 'Distance'},
        {'label': 'Strecke', 'value': 'Strecke_Grafik'},
    ], value = 'Speed' ),
    dcc.Graph(id='line_plot')])

@app.callback(
    Output(component_id='line_plot', component_property='figure'),
    Input(component_id='dropdown', component_property='value'))
def graph_update(value_of_input_component):
    print(value_of_input_component)
    fig = px.line(df, x=df['Zeitstempel'], y=df[value_of_input_component])
    return fig

# Starten der Dash-App
if __name__ == '__main__':
    print('**')
    #app.run_server(debug=True) # Startet Server im Debug-Modus
    app.run_server(host = '127.0.0.1', port=8080, debug=False)