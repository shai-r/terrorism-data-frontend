import folium
import os
from typing import List

from app.utils.num_util import convert_to_float

maps_directory = os.path.join(os.getcwd(),'static', 'maps')
file_path = os.path.join(maps_directory, 'mean_casualties_by_area.html')

def get_marker_color(paint: float) -> str:
    match paint:
        case _ if paint > 1:
            return "green"
        case _ if 1 <= paint < 2:
            return "lightgreen"
        case _ if 2 <= paint < 3:
            return "orange"
        case _ if 3 <= paint < 4:
            return "orange"
        case _ if 4 <= paint < 5:
            return "darkorange"
        case _ if 5 <= paint < 6:
            return "red"
        case _:
            return "black"

def default_map():
    map = folium.Map(location=[31.7769, 35.2345], zoom_start=17)
    home_path = os.path.join(maps_directory, 'home.html')
    map.save(home_path)

def map_of_average_casualties(res: List[dict]):
    main_map = folium.Map(location=[0, 0], zoom_start=2)
    for loc in res['avg_casualties_by_area']:
        print(loc)
        marker_color = get_marker_color(convert_to_float(loc["victims"]))
        tooltip_text = (
            f"Region: {loc['region']}<br>"
            f"Average Casualties: {loc['victims']:.2f}"
        )
        folium.Marker(
            location=[loc['latitude'], loc['longitude']],
            tooltip=tooltip_text,
            icon=folium.Icon(color=marker_color),
        ).add_to(main_map)

    os.remove(file_path)
    main_map.save(file_path)