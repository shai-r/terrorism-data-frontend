def convert_to_number(func, value):
    try:
        return func(value)
    except ValueError:
        return func(0)

def convert_to_int(value):
    return convert_to_number(int, value)

def convert_to_float(value):
    return convert_to_number(float, value)