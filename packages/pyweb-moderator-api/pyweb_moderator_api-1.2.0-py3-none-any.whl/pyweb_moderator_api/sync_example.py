import pyweb_moderator_api

text = "Пример текста"

with pyweb_moderator_api.SyncAPI(token="your_api_token") as client:
    result = client.getClass(text=text, model="bert")

text_class = result.text_class
time_taken = result.time_taken
confidence = result.confidence
unique_id = result.unique_id
balance = result.balance
label = result.label

print(f"Класс текста: {text_class}\nМетка: {label}\nБыло потрачено времени: {time_taken}\nТочность: {confidence}\nИдентификатор: {unique_id}\nОставшийся баланс: {balance}")