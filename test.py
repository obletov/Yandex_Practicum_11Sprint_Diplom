# Дмитрий Облетов, 8а когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_create_and_get_order():
    response = sender_stand_request.post_new_order()
    track = response.json()["track"]

    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200

response = sender_stand_request.post_new_order()

print(response.status_code)
print(response.headers)
print(response.json)