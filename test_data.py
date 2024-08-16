CREATE_COURIER = 'http://qa-scooter.praktikum-services.ru/api/v1/courier'
LOGIN_COURIER = 'http://qa-scooter.praktikum-services.ru/api/v1/courier/login'
CREATE_ORDER = 'http://qa-scooter.praktikum-services.ru/api/v1/orders'
GET_ORDERS = 'http://qa-scooter.praktikum-services.ru/api/v1/orders'

login_valid = 'john_snow'
password_valid = '111111!'

order_data_black = {
    "firstName": "John",
    "lastName": "Snow",
    "address": "the Wall",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-08-06",
    "comment": "I don't know nothing",
    "color": [
        "BLACK"
    ]
}

order_data_grey = {
    "firstName": "Daenerys",
    "lastName": "Targaryen",
    "address": "Antient Valyria",
    "metroStation": 4,
    "phone": "+7 800 355 35 00",
    "rentTime": 5,
    "deliveryDate": "2024-08-06",
    "comment": "Drakaris",
    "color": [
        "GREY"
    ]
}

order_data_multicolor = {
    "firstName": "Tyrion",
    "lastName": "Lannister",
    "address": "Caterly Rock",
    "metroStation": 3,
    "phone": "+7 800 355 0988",
    "rentTime": 1,
    "deliveryDate": "2024-08-06",
    "comment": "I talk too much",
    "color": [
        "GREY", "BLACK"
    ]
}

order_data_no_color = {
    "firstName": "Sansa",
    "lastName": "Stark",
    "address": "Winterfell",
    "metroStation": 3,
    "phone": "+7 800 445 0988",
    "rentTime": 4,
    "deliveryDate": "2024-08-06",
    "comment": "I like dogs",
    "color": []
}
