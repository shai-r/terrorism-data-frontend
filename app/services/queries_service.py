from app.services.map_service import map_of_average_casualties, default_map, map_of_percent_change, \
    map_of_event_victim_correlation, map_of_shared_attack_strategies, map_of_high_activity_regions, \
    map_of_influential_groups
from app.services.statistics_service import get_statistics


def select_query(query: str = 'home', region = None):
    data = get_statistics(f"{query}/{region}") if region else get_statistics(query)
    match query:
        case "mean_casualties_by_area":
            map_of_average_casualties(data)
        case "calculate_percent_change":
            map_of_percent_change(data)
        case "calculate_event_victim_correlation":
            map_of_event_victim_correlation(data)
        case "identify_shared_attack_strategies":
            map_of_shared_attack_strategies(data, region)
        case "identify_high_activity_regions":
            map_of_high_activity_regions(data, region)
        case "identify_influential_groups":
            map_of_influential_groups(data, region)
        case _:
            default_map()