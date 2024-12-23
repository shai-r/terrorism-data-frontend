import folium
import os
from typing import List

from app.utils.num_util import convert_to_float

maps_directory = os.path.join(os.getcwd(),'static', 'maps')


def get_marker_color(paint: float, min_val: float = 0, max_val: float = 10) -> str:
    scale_size = (max_val - min_val) / 10
    scale_index = int((paint - min_val) / scale_size)

    scale_index = min(max(scale_index, 0), 9)

    colors = [
        "green", "lightgreen", "yellowgreen", "yellow", "lightyellow",
        "orange", "darkorange", "red", "darkred", "black"
    ]

    return colors[scale_index]


def default_map():
    map = folium.Map(location=[31.7769, 35.2345], zoom_start=17)
    home_path = os.path.join(maps_directory, 'home.html')
    map.save(home_path)

def map_of_average_casualties(res: List[dict]):
    main_map = folium.Map(location=[0, 0], zoom_start=2)
    for loc in res['avg_casualties_by_area']:
        marker_color = get_marker_color(convert_to_float(loc["victims"]), 0, 25)
        tooltip_text = (
            f"Region: {loc['region']}<br>"
            f"Average Casualties: {loc['victims']:.2f}"
        )
        folium.Marker(
            location=[loc['latitude'], loc['longitude']],
            tooltip=tooltip_text,
            icon=folium.Icon(color=marker_color),
        ).add_to(main_map)
    file_path = os.path.join(maps_directory, 'mean_casualties_by_area.html')
    os.remove(file_path)
    main_map.save(file_path)


def map_of_percent_change(res: List[dict]):
    main_map = folium.Map(location=[0, 0], zoom_start=2)

    for loc in res['percent change']:
        change_text = ""
        for year_change in loc['percent_change']:
            change_text += (
                f"Year: {year_change}<br>"
                f"Percent Change: {loc['percent_change'][year_change]}<br><br>"
            )

        tooltip_text = f"Region: {loc['region']}<br>{change_text}"

        folium.Marker(
            location=[loc['latitude'], loc['longitude']],
            tooltip=tooltip_text,
            icon=folium.Icon(color='yellow'),
        ).add_to(main_map)

    file_path = os.path.join(maps_directory, 'calculate_percent_change.html')
    if os.path.exists(file_path):
        os.remove(file_path)
    main_map.save(file_path)


import folium
import os
from typing import List


def map_of_event_victim_correlation(res: List[dict]):
    main_map = folium.Map(location=[0, 0], zoom_start=2)

    for loc in res:
        region = loc['region']
        latitude = loc['coordinates']['latitude']
        longitude = loc['coordinates']['longitude']
        correlation = loc['correlation']

        marker_color = get_marker_color(abs(correlation), 0, 1)  # נניח שהקורלציה היא בין 0 ל-1

        tooltip_text = (
            f"Region: {region}<br>"
            f"Correlation: {correlation:.2f}"
        )

        folium.Marker(
            location=[latitude, longitude],
            tooltip=tooltip_text,
            icon=folium.Icon(color=marker_color),
        ).add_to(main_map)

    file_path = os.path.join(maps_directory, 'calculate_event_victim_correlation.html')
    if os.path.exists(file_path):
        os.remove(file_path)
    main_map.save(file_path)
