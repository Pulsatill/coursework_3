import requests

url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676460344497&signature=TzPLFJCuiEgqfgVr7Mk8MjqrA9hxjfI9L0d4dXOjjB4&downloadName=operations.json"


def get_url():
    """
    Получает данные из удалённой базы
    :return: полученные данные
    """
    response = requests.get(url)
    data = response.json()
    return data


def get_data(data):
    """
    Приводит данные в удобоваримый вид
    :param data: данные
    :return: список словарей
    """
    new_data = []
    for transaction in data:
        try:
            # отсекаем отменённые транзакции
            if transaction["state"] == "CANCELED":
                continue
            # если есть параметр "отправитель"
            elif "from" in transaction:
                transaction = dict(
                              trans_id=transaction["id"],
                              trans_state=transaction["state"],
                              trans_date=transaction["date"],
                              trans_amount=transaction["operationAmount"]["amount"],
                              trans_currency_name=transaction["operationAmount"]["currency"]["name"],
                              trans_currency_code=transaction["operationAmount"]["currency"]["code"],
                              trans_descript=transaction["description"],
                              trans_from=transaction["from"],
                              trans_to=transaction["to"]
                              )
                new_data.append(transaction)
            # если параметра "отправитель" нет, то просто отсекаем его для словаря
            elif "from" not in transaction:
                transaction = dict(
                              trans_id=transaction["id"],
                              trans_state=transaction["state"],
                              trans_date=transaction["date"],
                              trans_amount=transaction["operationAmount"]["amount"],
                              trans_currency_name=transaction["operationAmount"]["currency"]["name"],
                              trans_currency_code=transaction["operationAmount"]["currency"]["code"],
                              trans_descript=transaction["description"],
                              trans_to=transaction["to"]
                              )
                new_data.append(transaction)
        # тут ругался на разные ключи, которых нет(или не такие как нужно), пришлось заигнорить
        except KeyError:
            continue
    return new_data


def sort_by_date(new_data):
    """
    Сортирует данные по дате, сначала последние
    :param new_data: список словарей
    :return: отсортированный список словарей
    """
    sorted_data = sorted(new_data, key=lambda x: x["trans_date"], reverse=True)
    return sorted_data


def get_latest(sorted_data):
    """
    Отсекает устаревшие транзакции в списке
    :param sorted_data: отсортированный список словарей
    :return: список словарей с последними пятью транзакциями
    """
    latest_transactions = []
    latest_count = 0
    for i in sorted_data:
        if latest_count < 5:
            latest_transactions.append(i)
            latest_count += 1
        else:
            continue
    return latest_transactions


def correct_date(i):
    """
    Приводит дату в удобоваримый вид
    :param i: выбранный словарь из списка
    :return: дата в удобоваримом виде
    """
    correcting_date = i.get("trans_date")
    date_obj = correcting_date.split("T")[0].split("-")
    trans_date = f'{date_obj[2]}.{date_obj[1]}.{date_obj[0]}'
    return trans_date


def hide_sender_numbers(i):
    """
    Скрывает цифры счёта или карты отправителя,если отправитель есть
    :param i: выбранный словарь из списка
    :return: закодированную строку с названием и номером счёта/карты
    """
    if "trans_from" in i:
        full_string = i.get("trans_from")
        sender_resourses = ""
        sender_numbers = ""
        # цикл для скрытия номера карты
        for s in full_string:
            if s.isdigit():
                sender_numbers += s
            else:
                sender_resourses += s
        # если транзакция выполнена со счёта отправителя, скрывает номер счета
        if "Счет" in full_string:
            hide_send_numbers = f"**" + f"{sender_numbers[-4:]}"
        else:
            hide_send_numbers = f"{sender_numbers[:4]}" + f"{sender_numbers[4:6]}" + "** **** " + f"{sender_numbers[-4:]}"
        return f"{sender_resourses}" + f"{hide_send_numbers}"
    else:
        return None


def hide_recipient_numbers(i):
    """
    Скрывает цифры счета или карты получателя
    :param i: выбранный словарь из списка
    :return: закодированную строку с названием и номером счёта/карты
    """
    full_string_2 = i.get("trans_to")
    recip_resourses = ""
    recip_numbers = ""
    # цикл для скрытия номера карты получателя
    for s in full_string_2:
        if s.isdigit():
            recip_numbers += s
        else:
            recip_resourses += s
    # алгоритм, если транзакция на счет получателя
    if "Счет" in full_string_2:
        hide_recip_numbers = f"**" + f"{recip_numbers[-4:]}"
    else:
        hide_recip_numbers = f"{recip_numbers[:4]}" + f"{recip_numbers[4:6]}" + "** **** " + f"{recip_numbers[-4:]}"
    return f"{recip_resourses}" + f"{hide_recip_numbers}"


def show_result(latest_transactions):
    """
    Показывает результат для последних пяти транзакций
    :param latest_transactions: список с пятью последними транзакциями
    :return: ничего не возвращает, сразу выводит результат
    """
    for i in latest_transactions:
        # дата в удобном формате
        trans_date = correct_date(i)
        # назначение перевода
        description = i.get("trans_descript")
        # скрытые данные отправителя
        sender = hide_sender_numbers(i)
        # скрытые данные получателя
        recip = hide_recipient_numbers(i)
        # сумма перевода
        amount = i.get("trans_amount")
        # название денежной единицы
        currency = i.get("trans_currency_name")
        # показывает результат, если отправителя нет
        if sender is None:
            print(f"{trans_date} {description}\n"
                  f"{recip}\n"
                  f"{amount} {currency}\n")
        # показывает результат если есть отправитель
        else:
            print(f"{trans_date} {description}\n"
                  f"{sender} -> {recip}\n"
                  f"{amount} {currency}\n")
