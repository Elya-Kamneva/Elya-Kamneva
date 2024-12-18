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
#val_date = datetime.now().strftime("%d.%m.%Y")

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
    # Список сотрудников
    employees_data = [
        {
            "firstName": "Жанат",
            "lastName": "Азыкеев",
            "middleName": "Даулбаевич",
            "bin": "870330350942",
            "account": "KZ87722C000030907447",
        },
        {
            "firstName": "Роман",
            "lastName": "Акалелов",
            "middleName": "Игоревич",
            "bin": "831217301589",
            "account": "KZ31722C000020803383",
        },
        {
            "firstName": "Ақтоты",
            "lastName": "Бекмаганбетова",
            "middleName": "Баймуханқызы",
            "bin": "750708401544",
            "account": "KZ67722C000025830245",
        },
        {
            "firstName": "Алия",
            "lastName": "Беркимбаева",
            "middleName": "Муратовна",
            "bin": "860508451050",
            "account": "KZ88722C000024978983",
        },
        {
            "firstName": "Данила",
            "lastName": "Бородин",
            "middleName": "Серафимович",
            "bin": "061111500446",
            "account": "KZ38722C000074939442",
        },
        {
            "firstName": "Динара",
            "lastName": "Дакенова",
            "middleName": "Салимгереевна",
            "bin": "980720450654",
            "account": "KZ42722C000027615204",
        },
        {
            "firstName": "Назерке",
            "lastName": "Даукенова",
            "middleName": "Нұрлыбекқызы",
            "bin": "960628451282",
            "account": "KZ90722C000013276770",
        },
        {
            "firstName": "Раушан",
            "lastName": "Есимбекова",
            "middleName": "Канатовна",
            "bin": "910130400648",
            "account": "KZ04722C000014689086",
        },
        {
            "firstName": "Олег",
            "lastName": "Ешков",
            "middleName": "Юрьевич",
            "bin": "870412301147",
            "account": "KZ55722C000020415145",
        },
        {
            "firstName": "Айнамкөз",
            "lastName": "Қарақұлова",
            "middleName": "Нурланқызы",
            "bin": "911211401193",
            "account": "KZ62722C000023472653",
        }
    ]

    # Распределение общей суммы между сотрудниками
    total_amount = start_amount
    num_employees = len(employees_data)
    base_amount = total_amount // num_employees
    remainder = total_amount % num_employees

    #формирование списка сотрудников
    employees = []
    for index, employee in enumerate(employees_data):
        employee_amount = base_amount + (1 if index < remainder else 0)
        employees.append({
            "id": 137234928 + index,
            "deleted": False,
            "firstName": employee["firstName"],
            "lastName": employee["lastName"],
            "middleName": employee["middleName"],
            "amount": employee_amount,
            "account": employee["account"],
            "taxCode": employee["bin"],
            "kbe": "29",
            "countryCode": "RU",
            "birthDate": None,
            "reason": None,
            "period": None,
            "deductionType": None
        })

    data = {
    "account": {
        "id": 34053,
        "number": "KZ559491100003471026",
        "cardNumber": "KZ559491100003471026",
        "currency": "KZT",
        "currencyDigital": None,
        "balance": 44460566.57,
        "plannedBalance": -3590294150.28,
        "alias": "XXX",
        "externalCustomerId": None,
        "type": None,
        "accountType": "Current",
        "expirationDate": None,
        "status": None
    },
    "amount": start_amount,
    "valueDate": val_date,
    "purpose": "Перечисление юридическим лицом в банк заработной платы, оплаты трудового отпуска для последующего за",
    "purposeCode": "332",
    "purposeText": "Перечисление юридическим лицом в банк заработной платы, оплаты трудового отпуска для последующего за",
    "priority": False,
    "number": start_number,
    "isTemplate": False,
    "templateName": None,
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
    "info": None,
    "benefName": "Акционерное общество «Kaspi Bank»",
    "benefTaxCode": "971240001315",
    "benefAccount": "KZ24722S000000686267",
    "benefBankCode": "CASPKZKA",
    "benefResidencyCode": "14",
    "domesticTransferType": "Payroll",
    "employees": employees,
    "isLoanPay": False,
    "isRaw": False,
    "isSubsidiaryOrganization": False,
    "subsidiaryOrganizationId": None,
    "serverhubLinkMetadataDtoList": [],
    "actualPayer": {
        "name": "Камнева Элина Станиславовна",
        "taxCode": "971228400872",
        "isJuridical": False
    }
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
