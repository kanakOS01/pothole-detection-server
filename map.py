import folium
import pandas as pd

coordinates = [
    {'latitude': 28.6139, 'longitude': 77.2090},
    {'latitude': 28.4595, 'longitude': 77.0266},
    {'latitude': 28.5355, 'longitude': 77.3910},
    {'latitude': 28.6692, 'longitude': 77.4538},
    {'latitude': 28.4089, 'longitude': 77.3178},
    {'latitude': 28.9845, 'longitude': 77.7064},
    {'latitude': 28.9288, 'longitude': 77.0917},
    {'latitude': 28.8955, 'longitude': 76.6066},
    {'latitude': 27.8974, 'longitude': 78.0880},
    {'latitude': 29.3909, 'longitude': 76.9635}
]

def pothole_scatter_mapbox():
    map = folium.Map(
        location=[28.6139, 77.2090], tiles="Cartodb dark_matter", zoom_start=10
    )

    for coordinate in coordinates:
        folium.Marker(
            location=[coordinate['latitude'], coordinate['longitude']],
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(map)

    map.save("map_templates/map.html")


if __name__ == "__main__":
    pothole_scatter_mapbox()
