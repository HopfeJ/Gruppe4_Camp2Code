from flask import Flask, Response
from dash import Dash, html
import dash_bootstrap_components as dbc
import cv2

# Finding the path of basisklassen_cam.py in repo camp2code
import os
import pathlib
import sys
path_to_this_file = os.path.realpath(__file__)
path_to_modules = pathlib.Path(path_to_this_file).resolve().parents[1].joinpath('Software')
sys.path.append(str(path_to_modules))
print("_Choosen path to basisklassen_cam.py", path_to_modules)

from basisklassen_cam import Camera

# Expliztes Anlegen eines Flask-Servers
server = Flask(__name__)
# Erzeugen des Dash-Objektes unter Verwendung des Flask-Servers
app = Dash(__name__, server=server)

my_camera = Camera(flip=False)

# Folgender Generator gibt beim Aufruf den Byte des Bildes in JPG zurück
# Es wird die Klasse Camera aus basisklassen_cam.py verwendet.
def generate_camera_image(camera):
    while True:
        # Kamera-Objekt liefert aktuelles Bild als Numpy-Array
        frame = camera.get_frame()
        # Einige beipielhafte Manipulationen des Bildes
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # canny = cv2.Canny(gray, 100, 200)
        frame = gray
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
    dbc.Row([html.H1("Simple example videostreams with Flask and Dash", style={"textAlign": "center"})]),
    dbc.Row([
        # Einbinden eines Bildes, welches auf den Videofeed verweist.
        # Entsprechend wird das Bild kontinuierlich aktualisiert.
        html.Div([html.Img(src="/video_feed")])
    ], style={'textAlign': 'center'}),
])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=False, port=8080)