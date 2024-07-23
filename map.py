from pymongo import MongoClient
import folium


def fetch_coordinates():
    conn = MongoClient("localhost", 27017)
    db = conn.pothole_detection
    collection = db.potholes
    coordinates = [
        {"latitude": 28.6139, "longitude": 77.2090},
        {"latitude": 28.4595, "longitude": 77.0266},
        {"latitude": 28.5355, "longitude": 77.3910},
        {"latitude": 28.6692, "longitude": 77.4538},
        {"latitude": 28.4089, "longitude": 77.3178},
        {"latitude": 28.9845, "longitude": 77.7064},
        {"latitude": 28.9288, "longitude": 77.0917},
        {"latitude": 28.8955, "longitude": 76.6066},
        {"latitude": 27.8974, "longitude": 78.0880},
        {"latitude": 29.3909, "longitude": 76.9635},
        {"latitude": 28.4675, "longitude": 77.0916},
        {"latitude": 28.4719, "longitude": 77.0801},
        {"latitude": 28.4736, "longitude": 77.0504},
        {"latitude": 28.4614, "longitude": 77.0519},
        {"latitude": 28.4956, "longitude": 77.0480},
        {"latitude": 28.4968, "longitude": 77.0375},
        {"latitude": 28.5083, "longitude": 77.0614},
        {"latitude": 28.4921, "longitude": 77.0328},
        {"latitude": 28.4791, "longitude": 77.0153},
        {"latitude": 28.4634, "longitude": 77.0379}
    ]
    for document in collection.find():
        coordinates.append(
            {"latitude": document["latitude"], "longitude": document["longitude"]}
        )
    return coordinates


def pothole_scatter_mapbox(coordinates):
    map = folium.Map(
        location=[28.6439, 77.1090], tiles="Cartodb dark_matter", zoom_start=10
    )

    for coordinate in coordinates:
        folium.Marker(
            location=[coordinate["latitude"], coordinate["longitude"]],
            icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(map)

    map.save("map_templates/map.html")


if __name__ == "__main__":
    coordinates = fetch_coordinates()
    pothole_scatter_mapbox(coordinates)
