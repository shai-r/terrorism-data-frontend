from app.services.map_service import map_of_average_casualties, default_map
from app.services.statistics_service import get_statistics


def select_query(region, query: str = 'home'):
    match query:
        case "mean_casualties_by_area":
            data = get_statistics(query)
            map_of_average_casualties(data)
        case _:
            default_map()