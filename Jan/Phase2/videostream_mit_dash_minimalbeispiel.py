from flask import Flask, Response
from dash import Dash, html, Input, Output, ctx, callback
import dash_bootstrap_components as dbc
import cv2
import os
import pathlib
import sys

path_to_this_file = os.path.realpath(__file__)
path_to_modules = pathlib.Path(path_to_this_file).resolve().parents[1].joinpath('Software')
sys.path.append(str(path_to_modules))
print("_Choosen path to basisklassen_cam.py", path_to_modules)

from basisklassen_cam import Camera
#from deepcar import DeepCar
#car= DeepCar()

# Expliztes Anlegen eines Flask-Servers
server = Flask(__name__)
# Erzeugen des Dash-Objektes unter Verwendung des Flask-Servers
app = Dash(__name__, server=server)

my_camera = Camera(flip=True)

# Folgender Generator gibt beim Aufruf den Byte des Bildes in JPG zurück
# Es wird die Klasse Camera aus basisklassen_cam.py verwendet.
def generate_camera_image(camera):
    while True:
        # Kamera-Objekt liefert aktuelles Bild als Numpy-Array
        frame = camera.get_frame()
        # Einige beipielhafte Manipulationen des Bildes
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # canny = cv2.Canny(gray, 100, 200)
        #frame = gray
        # Erstellen des Bytecode für das Bild/Videostream aus dem aktuellen Frame als NumPy-Array
        _, x = cv2.imencode(".jpeg", frame)
        x_bytes = x.tobytes()

        yield (b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + x_bytes + b'\r\n\r\n')

# Anlegen eines Endpunkte für einen Videostream /video_feed
# Dieser Endpunkt ist in der App ebenfalls erreichbar.
@server.route("/video_feed")
def video_feed():

    return Response(generate_camera_image(my_camera), mimetype='multipart/x-mixed-replace; boundary=frame')

# Layout der App
app.layout = html.Div(children=[
                dbc.Row([html.H1("Gruppe 4", style={"textAlign": "center"})]),
                dbc.Row([html.Div([html.Img(src="/video_feed")]),
                         
                html.Button('Start', id='Start', n_clicks=0),
                #html.Button('Button 2', id='btn-nclicks-2', n_clicks=0),
                #html.Button('Button 3', id='btn-nclicks-3', n_clicks=0),
                html.Div(id='container-button-timestamp')
                ], style={'textAlign': 'center'}),
])



@callback(
    Output('container-button-timestamp', 'children'),
    Input('Start', 'n_clicks'),
    #Input('btn-nclicks-2', 'n_clicks'),
    #Input('btn-nclicks-3', 'n_clicks')
)
def displayClick(btn1):#, btn2, btn3):
    msg = "Noch kein Befehl ausgeführt"
    if "Start" == ctx.triggered_id:
        msg = 'Das Programm wird gestartet'
        #car.run()
    #elif "btn-nclicks-2" == ctx.triggered_id:
    #    msg = "Button 2 was most recently clicked"
    #elif "btn-nclicks-3" == ctx.triggered_id:
    #    msg = "Button 3 was most recently clicked"
    return html.Div(msg)



if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=False, port=8080)