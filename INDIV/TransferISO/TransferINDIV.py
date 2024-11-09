import requests
import time
from INDIV.filesINDIV.fileStorageINDIV import save_data, load_data

# Адрес API и Bearer токен
api_url1 = "https://test.altyn-i.kz/api/transfers/external-account-transfer/create"  # URL создания
api_url2 = "https://test.altyn-i.kz/api/transfers/confirm"  # URL отправки
bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzZWRfYXV0aF9mYWN0b3JzIjpbIlBhc3N3b3JkIl0sImN1c3RvbWVyX2V4dGVybmFsX2lkIjoiMDcwMC4wMzY4NzAiLCJjaGFpbl90eXBlIjoiU1VDQ0VTUyIsInJvbGUiOiJwZXJzIiwidXNlcl9uYW1lIjoiZnBXSDhYR0dYTS9hamd1MjdGMjA0L0xBUlhWdlVkRG9lekhMTC9jNzBIaEZPVGhTSk1QS3JSMW5EWnVhdUZUMjlzcWR6QnVYYXh3TWVDdjY0amUwVjR4VzhjZVhzVE5oZi9FTFdoVDJNZWxYZ3FrOVZDNDEgUUV2QTVYUHNDNWxINzlWU2tlIGFIRzJrUGhETHdOZ3piWTlMeXIgWFA5WXh4N2ZHN1Z0QndjPSIsImNyZWF0ZWQiOiIyMDI0LTExLTA4VDE4OjIwOjMxLjY0OCIsInJvbGVfdmVyc2lvbiI6MCwiaXNfcGFzc3dvcmRfY2hhbmdlIjpmYWxzZSwiYXV0aG9yaXRpZXMiOlsiY3VzdG9tZXIiXSwiY2xpZW50X2lkIjoiV0VCIiwicm9sZXNfYXV0aF9mYWN0b3JzIjpbeyJhdXRoX2ZhY3Rvcl9jaGFpbiI6WyJQYXNzd29yZCJdLCJyb2xlIjp7ImlkIjo0LCJjb2RlIjoicGVycyJ9fV0sInVzZXJfdHlwZSI6ImN1c3RvbWVyIiwidG9rZW5faWQiOiJiYWU5MWY5NTkzMzQ0ZDAwYjE0NmM1MTY3ZmY4YWM4YyIsInVzZXJfaWQiOjEwMTM5NTIyLCJyb2xlX2lkIjo0LCJzY29wZSI6WyJBTEwiXSwiY2FuX3NraXAiOmZhbHNlLCJwb3NzaWJsZV9jaGFpbnMiOltdLCJjdXN0b21lcl91c2VyX2lkIjoxMDEzOTUxMywiY3VzdG9tZXJzIjpbeyJuYW1lIjoiWFhYIC0g0JDQodCV0KLQntCS0J3QkCIsImlkIjoxMDEzOTUxM31dLCJleHAiOjE4NTEwNzIwMzEsImN1c3RvbWVyX2lkIjoxMDEzOTU0MiwianRpIjoiZTc0NjJhZTktZTQ5NS00MjY4LWE2NjktNWQyNjc3MGY2Y2VmIn0.EHtGHe67ght9Qo7RxhuPvn5mNwOoN_Vq3GpVixQvJXZEJmQa9XUPBJFnPzWR2IC2Dc1pgJovFeoD0Hck-9Gd5WQ7ffEMwzXeb6Dn00FbHcsmhDFYIeq2YZv7pq1osqyI7jiRnXQ2kNZ0fFq_UZ14KqPzrZ-SLVr6HQP0ZknNIkfI1sZsq6YU3hw-piH2f53brfUDHR8IBLLjeuy7j-DqseKAjttcZWgYWEs-9kIBtjYRU-dFACxqVwEkAi-rxKTz5DPi94g61xVW5Qfr6iORW3S4z73MaC-9qHpjtz-vDOFXNkQsX3jFeOAdhH81pwMQsOrFKi99v29xMbJ_y5dcCw"

# Заголовки
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

# Начальные значения для `amount` и `number`
data = load_data("../../INDIV/filesINDIV/init_data.json")
start_amount = data.get("start_amount")

# Количество итераций
iterations = 1

# Выполнение запросов
for i in range(iterations):
    start_amount += 1
    data = {
        "fromAccountId": 10259010,
        "beneficiaryIban": "KZ96722C000018790336",
        "beneficiaryBankCode": "CASPKZKA",
        "beneficiaryName": "ИГЕМБЕКОВА ТОГЖАН АСЕТОВНА",
        "beneficiaryTaxCode": "981027401225",
        "beneficiaryCountry": "KZ",
        "knp": "343",
        "kbe": "19",
        "amount": start_amount,
        "agreement": False,
        "document": {}
}

    try:
        # Создание платежа
        response = requests.post(api_url1, headers=headers, json=data)
        if response.status_code == 200:
            response_data = response.json()
            document_id = response_data.get("transferId")  # Извлекаем id платежа
            print(f"Итерация {i + 1}: Платеж создан. ID: {document_id}")

            # Подписание
            sent_to_sign_response = requests.post(api_url2, headers=headers,
                                                  json={"verificationCode": "111111", "transferId": document_id})
            if sent_to_sign_response.status_code == 200:
                print(f"Итерация {i + 1}: Платеж отправлен на подписание. ID: {document_id}.")
            else:
                print(
                    f"Ошибка отправки на подписание: {sent_to_sign_response.status_code}, {sent_to_sign_response.text}")

        else:
            # Обработка ошибок
            error_details = response.json()
            error_message = error_details.get("message") or "Ошибка"
            print(f"Итерация {i + 1}, : Ошибка {response.status_code}: {error_message}")

        # Задержка
        time.sleep(1)
    except requests.exceptions.RequestException as e:
        print(f"Итерация {i + 1}: Произошла ошибка: {e}")

print("Все итерации завершены.")

save_data({"start_amount": start_amount})