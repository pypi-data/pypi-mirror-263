from cron_parser.constants import  FIELD_NAMES

def get_range_values(range_str):
        """
        get range values for specified range
        parameters: range_str
        return: list of values
        """
        
        start, end = map(int, range_str.split("-"))
        print("list", list(range(start, end + 1)))
        print(list(range(start, end + 1)))
        return list(range(start, end + 1))


def get_step_values(step_str, min_value, max_value):
    values = []
    step = int(step_str)
    for value in range(min_value, max_value + 1):
        if (value - min_value) % step == 0:
            values.append(value)
    return values

def get_min(field_name):
    mins = [0, 0, 1, 1, 0]
    return mins[FIELD_NAMES.index(field_name)]

def get_max(field_name):
    maxes = [59, 23, 31, 12, 6]
    return maxes[FIELD_NAMES.index(field_name)]

