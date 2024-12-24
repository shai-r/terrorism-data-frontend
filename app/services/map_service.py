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

def error_map(file_path, error):
    map = folium.Map(location=[32.093698, 34.825500], zoom_start=17)

    folium.Marker(
        location=[32.093698, 34.825500],
        popup=f'<b style="font-size: 30px; color: red;">ERROR</br>'
              f'<b style="font-size: 20px; color: red;">{error}</br>'
    ).add_to(map)
    map.save(file_path)

def map_of_average_casualties(res: List[dict]):
    main_map = folium.Map(location=[0, 0], zoom_start=2)
    for loc in res:
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

    for loc in res:
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


def map_of_shared_attack_strategies(res, region_type):
    file_path = os.path.join(maps_directory, 'identify_shared_attack_strategies.html')

    if not os.path.exists(maps_directory):
        os.makedirs(maps_directory)
    if region_type == '':
        error_map(file_path, "You did not enter an area type...")
        return

    main_map = folium.Map(location=[20, 0], zoom_start=2)

    for loc in res:
        attack_type = loc['attack_type']
        region = loc[region_type]
        groups = loc['groups']
        latitude = loc['latitude']
        longitude = loc['longitude']

        marker_color = get_marker_color(len(groups), 10,500) \
            if region_type == 'region' \
            else get_marker_color(len(groups), 0,120)

        tooltip_text = (
            f"<b>Attack Type:</b> {attack_type}<br>"
            f"<b>Region:</b> {region}<br>"
            f"<b>Groups Number:</b> {len(groups)}<br>"
            f"<b>Groups Involved:</b> {', '.join(groups[:5])}..."
        )

        folium.Marker(
            location=[latitude, longitude],
            tooltip=tooltip_text,
            icon=folium.Icon(color=marker_color),
        ).add_to(main_map)

    if os.path.exists(file_path):
        os.remove(file_path)
    main_map.save(file_path)

def map_of_high_activity_regions(res, region_type):
    file_path = os.path.join(maps_directory, 'identify_high_activity_regions.html')

    if not os.path.exists(maps_directory):
        os.makedirs(maps_directory)
    if region_type == '':
        error_map(file_path, "You did not enter an area type...")
        return

    main_map = folium.Map(location=[20, 0], zoom_start=2)
    for loc in res:
        region = loc[region_type]
        groups = loc['groups']
        latitude = loc['latitude']
        longitude = loc['longitude']

        marker_color = get_marker_color(len(groups), 50,850) \
            if region_type == 'region' \
            else get_marker_color(len(groups), 0,300)

        tooltip_text = (
            f"<b>Region:</b> {region}<br>"
            f"<b>Groups Number:</b> {len(groups)}<br>"
            f"<b>Groups Involved:</b> {', '.join(groups[:5])}..."
        )

        folium.Marker(
            location=[latitude, longitude],
            tooltip=tooltip_text,
            icon=folium.Icon(color=marker_color),
        ).add_to(main_map)

    if os.path.exists(file_path):
        os.remove(file_path)
    main_map.save(file_path)

def map_of_influential_groups(res, region_type):
    file_path = os.path.join(maps_directory, 'identify_influential_groups.html')

    if not os.path.exists(maps_directory):
        os.makedirs(maps_directory)
    if region_type == '':
        error_map(file_path, "You did not enter an area type...")
        return

    main_map = folium.Map(location=[20, 0], zoom_start=2)
    for loc in res:
        region = loc[region_type]
        group = loc['group']
        latitude = loc['latitude']
        longitude = loc['longitude']
        total_influence = loc['total_influence']

        tooltip_text = (
            f"<b>Region:</b> {region}<br>"
            f"<b>Total Influence:</b> {total_influence}<br>"
            f"<b>Influential Group:</b> {group}"
        )

        folium.Marker(
            location=[latitude, longitude],
            tooltip=tooltip_text,
            icon=folium.Icon(color='yellow'),
        ).add_to(main_map)

    if os.path.exists(file_path):
        os.remove(file_path)
    main_map.save(file_path)
