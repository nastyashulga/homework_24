from typing import Iterator, Any, Optional, Callable
import re

def filter_query(param: str, data: list[str]) -> Iterator[str]:
    return list(filter(lambda row: param in row, data))

def map_query(param: int, data: list[str]) -> Iterator[str]:
    int_number = int(param)
    return list(map(lambda row: row.split(' ')[int_number], data))

def unique_query(data: list[str], *args: Any, **kwargs: Any) -> Iterator[str]:
    result: list[str] = []
    seen = set()
    for row in data:
        if row in seen:
            continue
        else:
            result.append(row)
            seen.add(row)
    return result

def sort_query(param: str, data: list[str]) -> Iterator[str]:
    reverse: Optional[bool] = False if param == 'asc' else True
    return sorted(data, reverse=reverse)

def limit_query(param: int, data: list[str]) -> Iterator[str]:
    limit = int(param)
    return data[:limit]

def regex_query(param: str, generator: Iterator[str]) -> Iterator[str]:
    pattern: re.Pattern = re.compile(param)
    return filter(lambda x: re.search(pattern, x), generator)

dict_of_utils: dict[str, Callable[..., Iterator[str]]] = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': regex_query,
}


def build_query(cmd: str, filename: str, data: list[str] = None) -> Iterator[str]:
    if not data:
        with open(f'data/{filename}') as file:
            data = list(map(lambda row: row.strip(), file))
    return dict_of_utils[cmd](param=filename, data=data)



