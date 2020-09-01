import math

def is_number(n):
 try:
    float(n)
 except ValueError:
    return False
 return True

def is_positive_number(n):
    if is_number(n):
        if n < 0:
            return False
        else:
            return True
    else:
        return False

def simple_triangle_area(base, height):
    if is_positive_number(base) and is_positive_number(height):
        return float(.5*(base*height))
    else:
        return "NaN"

def simple_triangle_hypotenuse(base, height):
    if is_positive_number(base) and is_positive_number(height):
        c_sqr = float((base*base)+(height*height))
        return math.sqrt(c_sqr)
    else:
        return "NaN"

def rebase_time(i):
    if is_positive_number(i):
        return (int(i) * 60)
    else:
        return "NaN"

def calc_seconds(hours, minutes):
    if is_positive_number(hours) and is_positive_number(minutes):
        hrs_to_secs = rebase_time(rebase_time(hours))
        mins_to_secs = rebase_time(minutes)
        return hrs_to_secs + mins_to_secs;
    else:
        return "NaN"

def recursive_string(label, count):
    if int(count) > 1:
        label += recursive_string(label, int(count) - 1)
    return label