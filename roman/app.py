from dash import Dash, html
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



# Min, Max, Avg-Speed
max_speed = df["Speed"].max()
min_speed = df[df["Speed"] > 0]["Speed"].min()
#avg_speed = df[df["Direction"] > 0]["Speed"].mean()
avg_speed = df["Speed"].mean()

# Gesamtfahrzeit:
start_stop_df = df[df["Reason"].isin(["start_driving", "car_stop"])]["Zeitstempel"].reset_index(drop=False)
start_stop_df["Zeitstempel"] = pd.to_datetime(start_stop_df["Zeitstempel"])
start_stop_df['Zeitintervall'] = start_stop_df["Zeitstempel"].diff()
summe_zeitintervall = start_stop_df['Zeitintervall'].sum()
print("Gesamtfahrzeit:", summe_zeitintervall.total_seconds())

# Gesamte zurückgelegte Strecke:
# s = v * t
print(start_stop_df)


print("start_stop:",type(start_stop_df))
print("Max Speed:", max_speed)
print("Min Speed:", min_speed)
print("Avg Speed:", avg_speed)

# Inizialisierung der Dash-App
app = Dash()

# Beipiel für das Erstellen eines Layouts der App ... 
# ... durch das Zusammenfügen verschiedener HTML-Komponenten
app.layout = html.Div(
    children=[
        html.H1(children='Fahrparcour Gruppe 4',
                style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40}),
        html.H2(children='Wissenswertes'),    
        html.Div(children='Beispieltext. Dash ist ein tolles Ding!'),
    ]
)

# Starten der Dash-App
if __name__ == '__main__':
    print('**')
    app.run_server(debug=True) # Startet Server im Debug-Modus
