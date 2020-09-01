import EPACode

def test_triangle_area():
    base = 10
    height = 10
    area = EPACode.simple_triangle_area(base, height)
    assert area == 50

def test_triangle_area_float():
    base = 10.5
    height = 10.5
    area = EPACode.simple_triangle_area(base, height)
    assert area == 55.125

def test_triangle_area_negative():
    base = -10.5
    height = 10.5
    area = EPACode.simple_triangle_area(base, height)
    assert area == 'NaN'

def test_triangle_hypotenuse():
    base = 10
    height = 10
    area = EPACode.simple_triangle_hypotenuse(base, height)
    assert area == 14.142135623730951

def test_triangle_hypotenuse_float():
    base = 10.5
    height = 10.5
    area = EPACode.simple_triangle_hypotenuse(base, height)
    assert area == 14.849242404917497

def test_triangle_hypotenuse_negative():
    base = 10.5
    height = -10.5
    area = EPACode.simple_triangle_hypotenuse(base, height)
    assert area == 'NaN'

def test_time_seconds():
    hours = 1
    minutes = 10
    area = EPACode.calc_seconds(hours, minutes)
    assert area == 4200

def test_time_seconds_nagative():
    hours = 1
    minutes = -10
    area = EPACode.calc_seconds(hours, minutes)
    assert area == 'NaN'

def test_recursive_string():
    label = 'jf'
    count = 4
    area = EPACode.recursive_string(label, count)
    assert area == 'jfjfjfjf'
