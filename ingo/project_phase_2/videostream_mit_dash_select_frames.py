from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from flask import Flask, Response

import plotly.express as px
import cv2
import numpy as np

# Finding the path of basisklassen_cam.py in repo camp2code
import os
import pathlib
import sys
# path_to_this_file = os.path.realpath(__file__)
# path_to_modules = pathlib.Path(path_to_this_file).resolve().parents[1].joinpath('Software')
# sys.path.append(str(path_to_modules))
# print("_Choosen path to basisklassen_cam.py", path_to_modules)

# Erstellen eines Kameraobjektes
# Das Objekt muss die Methoden ...
#   get_frame,
#   get_available_transformers und 
#   select_transformer bereitstellen,
# da diese verwendet werden.
from experimentalCameraClasses import MyCam , MyCam2

# MyCam
# stellt bereit Transformer bereit
# my_camera = MyCam(flip=False)

# MyCam2
# Transformer müssen angelegt werden.
my_camera2 = MyCam2(flip=True)

@my_camera2.register_transformer('black_white')
def black_white(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

@my_camera2.register_transformer('canny')
def canny(frame):
    return cv2.Canny(frame, 100, 150)

@my_camera2.register_transformer('original + canny')
def canny2(frame):
    h, _, _ = frame.shape     
    mask = cv2.Canny(frame, 100, 200)
    mask_inv = cv2.bitwise_not(mask)
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    frame2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    frame3 = cv2.addWeighted(frame2, 1, mask_bgr, 1, 0)
    ih = int(.1*h)
    frame3[:ih] = (frame3[:ih]/3)
    frame3[-ih:] = (frame3[-ih:]/3)
    return frame3

# Auswahl des Kameraobjektes
my_camera = my_camera2
list_of_transformers = my_camera.get_available_transformer()

# APPLIKATION
# Siehe auch Minimalbeispiel
server = Flask(__name__)
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

def generate_camera_image(camera):
    while True:
        # Kamera-Objekt liefert aktuelles Bild als Numpy-Array
        # Es benötigt die Methode get_frame()
        frame = camera.get_frame()
        # Erstellen des Bytecode für das Bild/Videostream aus dem aktuellen Frame als NumPy-Array
        _, x = cv2.imencode(".jpeg", frame)
        x_bytes = x.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + x_bytes + b'\r\n\r\n')

@server.route("/video_feed")
def video_feed():
    return Response(generate_camera_image(my_camera), mimetype='multipart/x-mixed-replace; boundary=frame')

# Layout
# Das Layout enthält ein Dropdownmenu, welches zur Auswahl des Transformers dient.
headline = [
    dbc.Row([html.H1("Example videostream with Dash and Flask", style={"textAlign": "left"})])
]

right_column = html.Div([html.Img(src="/video_feed", style={'width': '70%', "border": "2px black solid", "padding-left": "10%"})])

left_column = html.Div(dcc.Dropdown(list_of_transformers, list_of_transformers[0], clearable=False, 
                                    id='dropdown',
                                    style={'width': '90%', "border": "1px gray solid", "padding-left": "10%" }))

app.layout = html.Div([
    dbc.Row(headline),
    dbc.Row([
        dbc.Col(left_column, width=3, style={'width': '30%', "border": "1px gray dotted"}),
        dbc.Col(right_column, width=9, style={'width': '70%', "border": "1px gray dotted"})
    ]),
    dbc.Row(f"Example class: {my_camera.__class__}"),
    html.P(id='placeholder') # Ein leeres Element im Layout für Output des Callbacks siehe unten -> TODO
],style={"padding-left": "10%", "padding-right": "10%", "padding-top": "1%", "padding-bottom": "50%" })

# Der Callback für das Dropdownmenu verwendet die Methode select_transformer der Kamera
# Ein Callback benötigt zwingend einen Outout.
@callback(Output('placeholder', 'children'), Input('dropdown', 'value'))
def select_transformation(value):
    my_camera.select_transformer(value)
    return ''


if __name__ == "__main__":
    # IP-Adresse eventuell anpassen.
    app.run_server(host="0.0.0.0", debug=False, port=8080)