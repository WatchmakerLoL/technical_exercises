from datetime import datetime

from flask import Flask, request, Response

import json

from itertools import groupby

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


"""
    API - Exercise 1 Customer Order Status
"""


@app.route('/check-order-status', methods=['POST', 'GET'])
def custom_order_status():
    data = json.loads(request.data)

    order_status = [{
        'order_number': key,
        # Call function to check for status.
        'status': __check_for_status(value)
        # Make use of groupby from itertools to group by order_number
    } for key, value in groupby(data, __key_func)]

    return Response(json.dumps(order_status), status=200)


# Itertools keyfunc
def __key_func(k):
    return k['order_number']


def __check_for_status(list):
    list_values = [value for value in list]
    list_all_values = [value for elem in list_values for value in elem.values()]
    # Conditionals to know which status the overall order is in.
    if 'PENDING' in list_all_values:
        return 'PENDING'
    elif 'SHIPPED' in list_all_values:
        return 'SHIPPED'
    else:
        return 'CANCELLED'


"""
    API - Exercise 2 Seasons Problem
"""


@app.route('/check-season-delivered', methods=['POST', 'GET'])
def seasons_problem():
    data = json.loads(request.data)
    response = [{
        "ORD_ID": order['ORD_ID'],
        # Call function that helps determine the Season
        "SEASON": __get_season(order['ORD_DT'])
    } for order in data]

    return Response(json.dumps(response), status=200)


def __get_season(date_str):
    # Convert Date String to 'Day of the Year'
    doy = datetime.strptime(date_str, '%m/%d/%y').timetuple().tm_yday

    # Conditionals to know which season 'doy' corresponds.
    if doy in range(80, 172):
        return 'SPRING'
    elif doy in range(172, 264):
        return 'SUMMER'
    elif doy in range(264, 355):
        return 'FALL'
    else:
        return 'WINTER'


"""
    API - Exercise 3 Detect Changes
"""


@app.route('/detect-changes', methods=['POST', 'GET'])
def detecting_change():
    data = json.loads(request.data)

    # Make use of list comprehensions to detect where changes were made
    # Then, make a new list with the values that changed.
    changes = [i for i in range(1, len(data)) if
               data[i]['was_rainy'] != data[i - 1]['was_rainy'] and data[i]['was_rainy'] == True]
    response = [value for count, value in enumerate(data) if count in changes]
    return Response(json.dumps(response), status=200)


if __name__ == '__main__':
    app.run()
