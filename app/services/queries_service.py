from app.services.map_service import map_of_average_casualties, default_map, map_of_percent_change, \
    map_of_event_victim_correlation
from app.services.statistics_service import get_statistics


def select_query(query: str = 'home', region = None):
    match query:
        case "mean_casualties_by_area":
            data = get_statistics(query)
            map_of_average_casualties(data)
        case "calculate_percent_change":
            data = get_statistics(query)
            map_of_percent_change(data)
        case "calculate_event_victim_correlation":
            data = get_statistics(query)
            map_of_event_victim_correlation(data)
        case _:
            default_map()