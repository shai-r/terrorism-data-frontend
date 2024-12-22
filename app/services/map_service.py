import folium
import os
from typing import List

from app.utils.num_util import convert_to_float

current_directory = os.getcwd()
htmls_directory = os.path.join(current_directory,  'htmls')
file_path = os.path.join(htmls_directory, 'average_by_region.html')

def get_marker_color(fatal_avg: float) -> str:
    if fatal_avg < 1:
        return "green"
    elif 1 <= fatal_avg < 2:
        return "lightgreen"
    elif 2 <= fatal_avg < 4:
        return "orange"
    elif 4 <= fatal_avg < 6:
        return "darkorange"
    elif 6 <= fatal_avg <= 8:
        return "red"
    else:
        return "black"

def map_of_average_casualties(res: List[dict]) -> folium.Map:
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

    return main_map