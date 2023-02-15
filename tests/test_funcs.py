import pytest
from utils import funcs


@pytest.fixture
def data():
    return [{
        "id": 518707726,
        "state": "EXECUTED",
        "date": "2018-11-29T07:18:23.941293",
        "operationAmount": {
            "amount": "3348.98",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "MasterCard 3152479541115065",
        "to": "Visa Gold 9447344650495960"
    },
        {
        "id": 649467725,
        "state": "EXECUTED",
        "date": "2018-04-14T19:35:28.978265",
        "operationAmount": {
            "amount": "96995.73",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 27248529432547658655",
        "to": "Счет 97584898735659638967"
    },
        {
        "id": 782295999,
        "state": "EXECUTED",
        "date": "2019-09-11T17:30:34.445824",
        "operationAmount": {
            "amount": "54280.01",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 24763316288121894080",
        "to": "Счет 96291777776753236930"
    },
        {
        "id": 542678139,
        "state": "EXECUTED",
        "date": "2018-10-14T22:27:25.205631",
        "operationAmount": {
            "amount": "90582.51",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 2256483756542539",
        "to": "Счет 78808375133947439319"
    },
        {
        "id": 558167602,
        "state": "EXECUTED",
        "date": "2019-04-12T17:27:27.896421",
        "operationAmount": {
            "amount": "43861.89",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 73654108430135874305",
        "to": "Счет 89685546118890842412"
    }]


@pytest.fixture
def new_data():
    return [{
            'trans_id': 441945886,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-08-26T10:50:58.294041',
            'trans_amount': '31957.58',
            'trans_currency_name': 'руб.',
            'trans_currency_code': 'RUB',
            'trans_descript': 'Перевод организации',
            'trans_from': 'Maestro 1596837868705199',
            'trans_to': 'Счет 64686473678894779589'
            },
            {
            'trans_id': 41428829,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-07-03T18:35:29.512364',
            'trans_amount': '8221.37',
            'trans_currency_name': 'USD',
            'trans_currency_code': 'USD',
            'trans_descript': 'Перевод организации',
            'trans_from': 'MasterCard 7158300734726758',
            'trans_to': 'Счет 35383033474447895560'
            },
            {
            'trans_id': 939719570,
            'trans_state': 'EXECUTED',
            'trans_date': '2018-06-30T02:08:58.425572',
            'trans_amount': '9824.07',
            'trans_currency_name': 'USD',
            'trans_currency_code': 'USD',
            'trans_descript': 'Перевод организации',
            'trans_from': 'Счет 75106830613657916952',
            'trans_to': 'Счет 11776614605963066702'
            },
            {
            'trans_id': 587085106,
            'trans_state': 'EXECUTED',
            'trans_date': '2018-03-23T10:45:06.972075',
            'trans_amount': '48223.05',
            'trans_currency_name': 'руб.',
            'trans_currency_code': 'RUB',
            'trans_descript': 'Открытие вклада',
            'trans_to': 'Счет 41421565395219882431'
            },
            {
            'trans_id': 142264268,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-04-04T23:20:05.206878',
            'trans_amount': '79114.93',
            'trans_currency_name': 'USD',
            'trans_currency_code': 'USD',
            'trans_descript': 'Перевод со счета на счет',
            'trans_from': 'Счет 19708645243227258542',
            'trans_to': 'Счет 75651667383060284188'
            },
            {
            'trans_id': 873106923,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-03-23T01:09:46.296404',
            'trans_amount': '43318.34',
            'trans_currency_name': 'руб.',
            'trans_currency_code': 'RUB',
            'trans_descript': 'Перевод со счета на счет',
            'trans_from': 'Счет 44812258784861134719',
            'trans_to': 'Счет 74489636417521191160'
            }]


@pytest.fixture
def sorted_data():
    return [{
        'trans_id': 863064926,
        'trans_state': 'EXECUTED',
        'trans_date': '2019-12-08T22:46:21.935582',
        'trans_amount': '41096.24',
        'trans_currency_name': 'USD',
        'trans_currency_code': 'USD',
        'trans_descript': 'Открытие вклада',
        'trans_to': 'Счет 90424923579946435907'
    },
        {
            'trans_id': 114832369,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-12-07T06:17:14.634890',
            'trans_amount': '48150.39',
            'trans_currency_name': 'USD',
            'trans_currency_code': 'USD',
            'trans_descript': 'Перевод организации',
            'trans_from': 'Visa Classic 2842878893689012',
            'trans_to': 'Счет 35158586384610753655'
        },
        {
            'trans_id': 154927927,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-11-19T09:22:25.899614',
            'trans_amount': '30153.72',
            'trans_currency_name': 'руб.',
            'trans_currency_code': 'RUB',
            'trans_descript': 'Перевод организации',
            'trans_from': 'Maestro 7810846596785568',
            'trans_to': 'Счет 43241152692663622869'
        }]


@pytest.fixture
def latest_transactions():
    return [{
        'trans_id': 863064926,
        'trans_state': 'EXECUTED',
        'trans_date': '2019-12-08T22:46:21.935582',
        'trans_amount': '41096.24',
        'trans_currency_name': 'USD',
        'trans_currency_code': 'USD',
        'trans_descript': 'Открытие вклада',
        'trans_to': 'Счет 90424923579946435907'
    },
        {
            'trans_id': 114832369,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-12-07T06:17:14.634890',
            'trans_amount': '48150.39',
            'trans_currency_name': 'USD',
            'trans_currency_code': 'USD',
            'trans_descript': 'Перевод организации',
            'trans_from': 'Visa Classic 2842878893689012',
            'trans_to': 'Счет 35158586384610753655'
        },
        {
            'trans_id': 154927927,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-11-19T09:22:25.899614',
            'trans_amount': '30153.72',
            'trans_currency_name': 'руб.',
            'trans_currency_code': 'RUB',
            'trans_descript': 'Перевод организации',
            'trans_from': 'Maestro 7810846596785568',
            'trans_to': 'Счет 43241152692663622869'
        }, {
            'trans_id': 482520625,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-11-13T17:38:04.800051',
            'trans_amount': '62814.53',
            'trans_currency_name': 'руб.',
            'trans_currency_code': 'RUB',
            'trans_descript': 'Перевод со счета на счет',
            'trans_from': 'Счет 38611439522855669794',
            'trans_to': 'Счет 46765464282437878125'
        },
        {
            'trans_id': 801684332,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-11-05T12:04:13.781725',
            'trans_amount': '21344.35',
            'trans_currency_name': 'руб.',
            'trans_currency_code': 'RUB',
            'trans_descript': 'Открытие вклада',
            'trans_to': 'Счет 77613226829885488381'
        }]


@pytest.fixture
def i():
    return {
            'trans_id': 482520625,
            'trans_state': 'EXECUTED',
            'trans_date': '2019-11-13T17:38:04.800051',
            'trans_amount': '62814.53',
            'trans_currency_name': 'руб.',
            'trans_currency_code': 'RUB',
            'trans_descript': 'Перевод со счета на счет',
            'trans_from': 'Счет 38611439522855669794',
            'trans_to': 'Счет 46765464282437878125'
        }


def test_get_url():
    assert funcs.get_url()


def test_get_data(data):
    assert funcs.get_data(data)


def test_sort_by_date(new_data):
    assert funcs.sort_by_date(new_data)


def test_get_latest(sorted_data):
    assert funcs.get_latest(sorted_data)


def test_correct_date(i):
    assert funcs.correct_date(i) == "13.11.2019"


def test_hide_sender_numbers(i):
    assert funcs.hide_sender_numbers(i) == "Счет **9794"


def test_hide_recipient_numbers(i):
    assert funcs.hide_recipient_numbers(i) == "Счет **8125"


def test_show_results(latest_transactions):
    assert funcs.show_result(latest_transactions)
