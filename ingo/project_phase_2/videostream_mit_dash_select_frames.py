from dash import Dash, html, dcc, Input, Output, callback, no_update
import dash_bootstrap_components as dbc
from flask import Flask, Response

import plotly.express as px
import cv2
import numpy as np
from camcar import CamCar
from steering_controller_classic import SteeringController

my_car = CamCar(SteeringController(np.array([90, 0, 0]), np.array([150, 255, 255])))
# APPLIKATION
# Siehe auch Minimalbeispiel
server = Flask(__name__)
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

def get_jpeg_generator(camcar):
    while True:
        # Objekt liefert aktuelles Bild als Numpy-Array
        # Es benötigt die Methode get_last_frame()
        frame = camcar.get_last_frame()
        # Erstellen des Bytecode für das Bild/Videostream aus dem aktuellen Frame als NumPy-Array
        _, x = cv2.imencode(".jpeg", frame)
        x_bytes = x.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + x_bytes + b'\r\n\r\n')

@server.route("/video_feed")
def video_feed():
    return Response(get_jpeg_generator(my_car), mimetype='multipart/x-mixed-replace; boundary=frame')

# Layout
# Das Layout enthält ein Dropdownmenu, welches zur Auswahl der Car - Klasse dient.
headline = [
    dbc.Row([html.H1("Group4success", style={"textAlign": "left"})])
]

right_column = html.Div([html.Img(src="/video_feed", style={'width': '70%', "border": "2px black solid", "padding-left": "10%"})])


left_column = html.Div(dcc.Dropdown([1,2,3], 1, clearable=False, 
                                    id='dropdown',
                                    style={'width': '90%', "border": "1px gray solid", "padding-left": "10%" }))

app.layout = html.Div([
    dbc.Row(headline),
    dbc.Row([
        dbc.Col(left_column, width=3, style={'width': '30%', "border": "1px gray dotted"}),
        dbc.Col(right_column, width=9, style={'width': '70%', "border": "1px gray dotted"})
    ]),
    dbc.Row(f"Example class: {my_car.__class__}"),
    dbc.Button("Start", color="success", id="start"),
    dbc.Button("Stop", color="danger", id="stop", style={'margin-left': '10px'}),
    html.P(id='placeholder', style={}) # Ein leeres Element im Layout für Output des Callbacks siehe unten -> TODO

],style={"padding-left": "10%", "padding-right": "10%", "padding-top": "1%", "padding-bottom": "50%" })

# Ein Callback benötigt zwingend einen Outout.
@app.callback(Output('placeholder', 'children', allow_duplicate=True), Input('dropdown', 'value'), prevent_initial_call=True) # allow_duplicate=True: Platzhalter mehrfach einsetzbar
def select_transformation(value):
    
    return value

@app.callback(Output("placeholder", "children", allow_duplicate=True), Input("start", "n_clicks"), prevent_initial_call=True) # Verhindert den Aufruf beim Seitenaufbau
def start(n):
    if n:
        my_car.run()
    return no_update

@app.callback(Output("placeholder", "children", allow_duplicate=True), Input("stop", "n_clicks"), prevent_initial_call=True) # Verhindert den Aufruf beim Seitenaufbau
def stop(n):
    if n:
        my_car.stop_run()
    return no_update

if __name__ == "__main__":
    # IP-Adresse eventuell anpassen.
    app.run_server(host="0.0.0.0", debug=False, port=8080)