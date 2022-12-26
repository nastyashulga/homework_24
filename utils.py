def filter_query(param, data):
    return list(filter(lambda row: param in row, data))

def map_query(param, data):
    int_number = int(param)
    return list(map(lambda row: row.split(' ')[int_number], data))

def unique_query(data: list[str], *args, **kwargs):
    result = []
    seen = set()
    for row in data:
        if row in seen:
            continue
        else:
            result.append(row)
            seen.add(row)
    return result

def sort_query(param, data: list[str]):
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)

def limit_query(param, data):
    limit = int(param)
    return data[:limit]

dict_of_utils = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query
}


def build_query(cmd, filename, data=None):
    if not data:
        with open(f'data/{filename}') as file:
            data = list(map(lambda row: row.strip(), file))
    return dict_of_utils[cmd](param=param, data=data)



