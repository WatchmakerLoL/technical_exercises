from datetime import datetime

from flask import Flask, request, Response

import json

from itertools import groupby

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/check-order-status', methods=['POST', 'GET'])
def custom_order_status():
    order_status = []
    data = json.loads(request.data)

    for key, value in groupby(data, __key_func):
        order_status.append({
            'order_number': key,
            'status': __check_for_status(value)
        })

    return Response(json.dumps(order_status), status=200)


def __key_func(k):
    return k['order_number']


def __check_for_status(list):
    list_values = [value for value in list]
    list_all_values = [value for elem in list_values for value in elem.values()]
    if 'PENDING' in list_all_values:
        return 'PENDING'
    elif 'SHIPPED' in list_all_values:
        return 'SHIPPED'
    else:
        return 'CANCELLED'


@app.route('/check-season-delivered', methods=['POST', 'GET'])
def seasons_problem():
    data = json.loads(request.data)
    response = []

    for order in data:
        response.append(
            {
                "ORD_ID": order['ORD_ID'],
                "SEASON": __get_season(order['ORD_DT'])
              }
        )

    return Response(json.dumps(response), status=200)


def __get_season(date_str):
    doy = datetime.strptime(date_str, '%m/%d/%y').timetuple().tm_yday

    if doy in range(80, 172):
        return 'SPRING'
    elif doy in range(172, 264):
        return 'SUMMER'
    elif doy in range(264, 355):
        return 'FALL'
    else:
        return 'WINTER'

@app.route('/detect-changes', methods=['POST', 'GET'])
def detecting_change():
    data = json.loads(request.data)
    changes = [i for i in range(1,len(data)) if data[i]['was_rainy']!=data[i-1]['was_rainy'] and data[i]['was_rainy'] == True]
    response = [value for count, value in enumerate(data) if count in changes]
    return Response(json.dumps(response), status=200)


if __name__ == '__main__':
    app.run()
