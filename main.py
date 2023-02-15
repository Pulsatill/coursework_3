# импорт функций
from utils import funcs
from utils.funcs import get_url, get_data, sort_by_date, get_latest, show_result

# начало программы
data = get_url()
new_data = get_data(data)
sorted_data = sort_by_date(new_data)
latest_transactions = get_latest(sorted_data)
show_result(latest_transactions)
