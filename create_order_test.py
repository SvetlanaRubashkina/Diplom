import configuration
import requests
import data

#Функция создает новый заказ и возвращает его трек номер
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body).json()['track']

#Функция выполняет запрос на получение заказа по трек номеру
def get_order_by_track_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track_number),
                         json={},
                         headers=data.order_headers)


def test_create_order():
    track_number = post_new_order()
    status_code = get_order_by_track_number(track_number).status_code
    assert status_code == 200


