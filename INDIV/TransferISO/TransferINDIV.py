import requests
import time
from INDIV.filesINDIV.fileStorageINDIV import save_data, load_data

# Адрес API и Bearer токен
api_url1 = "https://test.altyn-i.kz/api/transfers/external-account-transfer/create"  # URL создания
api_url2 = "https://test.altyn-i.kz/api/transfers/confirm"  # URL отправки
bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzZWRfYXV0aF9mYWN0b3JzIjpbIlBhc3N3b3JkIl0sImN1c3RvbWVyX2V4dGVybmFsX2lkIjoiMDcwMC4wMzY4NzAiLCJjaGFpbl90eXBlIjoiU1VDQ0VTUyIsInJvbGUiOiJwZXJzIiwidXNlcl9uYW1lIjoiT2FsbWVSM29aYnE3YjZpZEVMTVdYTVJhRFg3IHRudWNUR1dTclNZbEZQQXFLWW1DTWFOaGpyVzdrUzFiWSAzTzRZZTZsVmwzREt4R1JPWDJONDdyZ3AgcDJKUC9vN1hOaDdNZUxrYThtSEkwMjhUWW0gRDBOTU52cS9tR0E5aEZyRFQwMTU4Q213akV1a0VoIHhKVE1ydXl0VmhBbmFiRWtzTSBHM1ZHZHNBPSIsImNyZWF0ZWQiOiIyMDI0LTExLTEwVDEyOjIwOjAzLjY1OCIsInJvbGVfdmVyc2lvbiI6MCwiaXNfcGFzc3dvcmRfY2hhbmdlIjpmYWxzZSwiYXV0aG9yaXRpZXMiOlsiY3VzdG9tZXIiXSwiY2xpZW50X2lkIjoiV0VCIiwicm9sZXNfYXV0aF9mYWN0b3JzIjpbeyJhdXRoX2ZhY3Rvcl9jaGFpbiI6WyJQYXNzd29yZCJdLCJyb2xlIjp7ImlkIjo0LCJjb2RlIjoicGVycyJ9fV0sInVzZXJfdHlwZSI6ImN1c3RvbWVyIiwidG9rZW5faWQiOiJiYmY4NDMzY2RjODY0ZTUwYTVhYTU5YWQ1OWYwZmVjNyIsInVzZXJfaWQiOjEwMTM5NTIyLCJyb2xlX2lkIjo0LCJzY29wZSI6WyJBTEwiXSwiY2FuX3NraXAiOmZhbHNlLCJwb3NzaWJsZV9jaGFpbnMiOltdLCJjdXN0b21lcl91c2VyX2lkIjoxMDEzOTUxMywiY3VzdG9tZXJzIjpbeyJuYW1lIjoiWFhYIC0g0JDQodCV0KLQntCS0J3QkCIsImlkIjoxMDEzOTUxM31dLCJleHAiOjE4NTEyMjMyMDMsImN1c3RvbWVyX2lkIjoxMDEzOTU0MiwianRpIjoiYjQ3NjU3YzAtZWE1OC00ODRkLWJhZmMtN2ZkNDJkNzE1ZjQwIn0.CKroIGX3cklGohplW1mJ1iznW9XpK-8m5JiYAJKIe2PbayH83qX8ngeWFYhgF5uw0fckB9Gk8HQSy75jtWnMTelKlhQTx3vMhwBN2y-l0b8IV_DWt3jsfmjDrBM0ddQIx8_vc1lzrNEsaypDr3XW1h_VnQnLM3rBfXrraCrnOAZ9hGjlw3fP9sToov09P9OYJn1bpsnMSQBZlPUvCpLFqPtS_T5IkP-eY-XO7tTPvJIX3qTiLPDE2HeSrm9kdUfgJp6gSeLAfjpM7KMG8ZQ9qlXRGSaftu4bFYzhWCiYu9LROUDFnDUHdwAgiRI-P4lDTh2d1ESR7W47BW4NLSJFhg",

# Заголовки
headers = {
    "Authorization": "{bearer_token}",
    "Content-Type": "application/json"
}

# Начальные значения для `amount` и `number`
data = load_data("../../INDIV/filesINDIV/init_data.json")
start_amount = data.get("start_amount")

# Количество итераций
iterations = 1

# Выполнение запросов
for i in range(iterations):
    start_amount += 10
    data = {
  "fromAccountId": 10259010,
  "beneficiaryIban": "KZ92722C000027167716",
  "beneficiaryBankCode": "CASPKZKA",
  "beneficiaryName": "ГИЛЬМАНОВА КАРИНА РУСЛАНОВНА",
  "beneficiaryTaxCode": "880728400402",
  "beneficiaryCountry": "KZ",
  "knp": "111",
  "kbe": "19",
  "amount": start_amount,
  "agreement": False,
  "document": {

  }
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