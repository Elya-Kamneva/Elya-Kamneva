import requests
import time
from IBUL.AuthIBUL.authIBUL import get_auth_token
from IBUL.Files.file_storage_IBUL import save_data, load_data
from datetime import datetime, timedelta

# Адрес API и Bearer токен
api_url1 = "https://legal-test.altyn-i.kz/api/payment/domestic-transfer/new"  # URL создания
api_url2 = "https://legal-test.altyn-i.kz/api/workflow/documentAction"  # URL отправку на подписание
api_url3 = "https://legal-test.altyn-i.kz/api/signing/checkSMS"  # URL подписания
api_url_sms_request = "https://legal-test.altyn-i.kz/api/signing/sms-request"
bearer_token = get_auth_token()
# текущий день
# val_date = datetime.now().strftime("%d.%m.%Y")

# следующий день
val_date = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")

# Заголовки
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

# Начальные значения для `amount` и `number`
data = load_data("../../Files/init_data.json")
start_amount = data.get("start_amount")
start_number = data.get("start_number")

# Количество итераций
iterations = 500

# Выполнение запросов
for i in range(iterations):
    start_amount += 1
    start_number += 1
    data = {
    "account": {
        "id": 34053,
        "number": "KZ559491100003471026",
        "cardNumber": None,
        "currency": "KZT",
        "currencyDigital": None,
        "balance": 44460566.57,
        "plannedBalance": -3590511319.28,
        "alias": "XXX",
        "externalCustomerId": None,
        "type": None,
        "accountType": "Current",
        "expirationDate": None,
        "status": {
            "id": None,
            "code": "1",
            "label": "Открыт",
            "subCode": "1",
            "subLabel": "Открыт"
        }
    },
    "amount": start_amount,
    "valueDate": val_date,
    "purpose": "testISO19112024",
    "purposeCode": "911",
    "purposeText": "testISO19112024 Hалог на имущество физических лиц Комиссионное вознаграждение АО «ЕНПФ», ДНПФ от суммы пенс-ых активов, АО «ГФСС» от суммы его активов",
    "priority": False,
    "number": start_number,
    "isTemplate": False,
    "director": {
        "id": 2426,
        "fullName": "Четинелли М.К.",
        "position": None,
        "sign_level": "A"
    },
    "accountant": {
        "id": -1,
        "value": {
            "id": -1
        },
        "label": "Не предусмотрен",
        "fullName": "Не предусмотрен"
    },
    "benefName": "РГУ УГД ПО МЕД Р ДГД ПО АЛМАТЫ КГД МФ РК",
    "benefTaxCode": "910740000123",
    "benefAccount": "KZ24070105KSN0000000",
    "benefBankCode": "KKMFKZ2A",
    "benefResidencyCode": "11",
    "vat": None,
    "budgetCode": "104102",
    "vinCode": "",
    "domesticTransferType": "PaymentOrder",
    "isNotNeedUnc": False,
    "isNotLinkTerrorism": True,
    "isPermitGiveInformation": False,
    "isLoanPay": False,
    "isSubsidiaryOrganization": False,
    "numberOfAdministrativeAffairs": None,
    "isRaw": False,
    "kvo": None,
    "benefCountryCode": None,
    "serverhubLinkMetadataDtoList": []
}


    try:
        # Создание платежа
        response = requests.post(api_url1, headers=headers, json=data)
        if response.status_code == 200:
            response_data = response.json()
            document_id = response_data.get("value")  # Извлекаем id платежа
            print(f"Итерация {i + 1}: Платеж создан. ID: {document_id}")

            # Отправка на подписание
            sent_to_sign_response = requests.post(api_url2, headers=headers,
                                                  json={"action": "submit", "documentId": document_id})
            if sent_to_sign_response.status_code == 200:
                print(f"Итерация {i + 1}: Платеж отправлен на подписание. ID: {document_id}.")
            else:
                print(
                    f"Ошибка отправки на подписание: {sent_to_sign_response.status_code}, {sent_to_sign_response.text}")

            requests.post(api_url_sms_request, headers=headers, data='{}')

            # Подписание
            sign_response = requests.post(api_url3, headers=headers,
                                          json={"code": "111111", "ids": [document_id], "signAndSend": True})
            if sign_response.status_code == 200:
                print(f"Итерация {i + 1}: Платеж подписан и отправлен. ID: {document_id}.")
            else:
                print(f"Ошибка подписания: {sign_response.status_code}, {sign_response.text}")

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

save_data({"start_amount": start_amount, "start_number": start_number})
