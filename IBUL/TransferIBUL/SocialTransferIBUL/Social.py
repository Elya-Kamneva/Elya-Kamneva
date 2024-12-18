import requests
import time
from IBUL.AuthIBUL.authIBUL import get_auth_token
from IBUL.Files.file_storage_IBUL import save_data, load_data
from datetime import datetime

# Адрес API и Bearer токен
api_url1 = "https://legal-test.altyn-i.kz/api/payment/domestic-transfer/new"  # URL создания
api_url2 = "https://legal-test.altyn-i.kz/api/workflow/documentAction"  # URL отправку на подписание
api_url3 = "https://legal-test.altyn-i.kz/api/signing/checkSMS"  # URL подписания
api_url_sms_request = "https://legal-test.altyn-i.kz/api/signing/sms-request"
bearer_token = get_auth_token()
# текущий день
val_date = datetime.now().strftime("%d.%m.%Y")

# следующий день
#val_date = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")

period = datetime.now().strftime("%m.%Y")

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
iterations = 50

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
            "birthDate": "06.02.1987"
        },
        {
            "firstName": "Роман",
            "lastName": "Акалелов",
            "middleName": "Игоревич",
            "bin": "831217301589",
            "birthDate": "06.02.1987"
        },
        {
            "firstName": "Ақтоты",
            "lastName": "Бекмаганбетова",
            "middleName": "Баймуханқызы",
            "bin": "750708401544",
            "birthDate": "06.02.1987"
        },
        {
            "firstName": "Алия",
            "lastName": "Беркимбаева",
            "middleName": "Муратовна",
            "bin": "860508451050",
            "birthDate": "06.02.1987"
        },
        {
            "firstName": "Данила",
            "lastName": "Бородин",
            "middleName": "Серафимович",
            "bin": "061111500446",
            "birthDate": "06.02.1987"
        },
        {
            "firstName": "Динара",
            "lastName": "Дакенова",
            "middleName": "Салимгереевна",
            "bin": "980720450654",
            "birthDate": "06.02.1987"
        },
        {
            "firstName": "Назерке",
            "lastName": "Даукенова",
            "middleName": "Нұрлыбекқызы",
            "bin": "960628451282",
            "birthDate": "06.02.1987"
        },
        {
            "firstName": "Раушан",
            "lastName": "Есимбекова",
            "middleName": "Канатовна",
            "bin": "910130400648",
            "birthDate": "06.02.1987"
        },
        {
            "firstName": "Олег",
            "lastName": "Ешков",
            "middleName": "Юрьевич",
            "bin": "870412301147",
            "birthDate": "06.02.1987"
        },
        {
            "firstName": "Айнамкөз",
            "lastName": "Қарақұлова",
            "middleName": "Нурланқызы",
            "bin": "911211401193",
            "birthDate": "06.02.1987"
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
            "taxCode": employee["bin"],
            "kbe": "",
            "countryCode": "",
            "birthDate": employee["birthDate"],
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
        "plannedBalance": -3590306881.28,
        "alias": "XXX",
        "externalCustomerId": None,
        "type": None,
        "accountType": "Current",
        "expirationDate": None,
        "status": None
    },
    "amount": start_amount,
    "valueDate": val_date,
    "purpose": "Социальные отчисления",
    "purposeCode": "012",
    "purposeText": "Социальные отчисления",
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
    "benefName": "НАО \"Гос. корпорация \"Правительство для граждан\"",
    "benefTaxCode": "160440007161",
    "benefAccount": "KZ67009SS00368609110",
    "benefBankCode": "GCVPKZ2A",
    "benefResidencyCode": "11",
    "bankName": "НАО \"Государственная корпорация «Правительство для граждан\"",
    "domesticTransferType": "SocialContribution",
    "employees": employees,
    "employeeTransferCategory": "S",
    "employeeTransferPeriod": period,
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
