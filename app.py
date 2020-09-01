import EPACode

from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/triangle/area/height/<height>/base/<base>', methods=['GET'])
def area_of_a_triangle(base=0.0, height=0.0):
    response_object = {'status': 'success'}
    if EPACode.is_positive_number(float(base)) and EPACode.is_positive_number(float(height)):
        response_object['message'] = ''
        response_object['area'] = EPACode.simple_triangle_area(float(base), float(height))
    else:
        response_object['message'] = 'This function requires positive numbers'
        response_object['area'] = 0
    return jsonify(response_object)

@app.route('/triangle/hypotenuse/height/<height>/base/<base>', methods=['GET'])
def triangle_hypotenuse(base=0.0, height=0.0):
    response_object = {'status': 'success'}
    
    if EPACode.is_positive_number(float(base)) and EPACode.is_positive_number(float(height)):
        response_object['message'] = ''
        response_object['hypotenuse'] = EPACode.simple_triangle_hypotenuse(float(base), float(height))
    else:
        response_object['message'] = 'This function requires positive numbers'
        response_object['hypotenuse'] = 0
    return jsonify(response_object)

@app.route('/time/seconds/hours/<hours>/minutes/<minutes>', methods=['GET'])
def calculate_seconds(hours=0, minutes=0):
    response_object = {'status': 'success'}
    if EPACode.is_positive_number(int(hours)) and EPACode.is_positive_number(int(minutes)):
        response_object['message'] = ''
        response_object['seconds'] = EPACode.calc_seconds(int(hours), int(minutes))
    else:
        response_object['message'] = 'This function requires positive numbers'
        response_object['seconds'] = 0
    return jsonify(response_object)

@app.route('/recursion/label/<label>/count/<count>', methods=['GET'])
def recusion(label="", count=0):
    response_object = {'status': 'success'}
    if EPACode.is_positive_number(int(count)):
        response_object['message'] = ''
        response_object['result'] = EPACode.recursive_string(label, int(count))
    else:
        response_object['message'] = 'This function requires a positive number for count'
        response_object['result'] = 0
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()