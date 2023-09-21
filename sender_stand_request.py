import requests
import configuration
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)


def get_order_by_track(track_number):
    params = {'t': track_number}
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                            params=params,
                            headers=data.headers)
    return response
    print(response.status_code)
    print(response.headers)
    print(response.json)