import requests


def get_auth_token():
    url = "https://legal-test.altyn-i.kz/auth/custom/oauth/token"  # URL для авторизации
    headers = {"Content-Type": "application/json", "Authorization": "Basic V0VCOg=="}
    payload = {
        "grant_type": "Password",
        "user_type": "customer",
        "username": "Fi5rLnnaylAchiwmvEFhCNh7XSU0cD5SsJVHFNQ91U/Ea/ClnyPXmPbIbPh5+gGT+Z3Q97PebI01wyf/bxipTuYxV3frOjwdjkF+0lEk0sXUJlKJnmlX/KwHNtgLg1YO0CxoI3DOFsgR43PYWm+zuYiuPwJQi3XwTJCmbdvtIAU=",
        "password": "BMlkirnS+jmW31K+IoSqka5MVHvxc9CHKdid7wnWexSj/VIbRE1wEqCfXbKZeiPWDb/PMF20XuCvWxNYY8QSfX7+TKm/maJG7i2Xo7lbaAkRHPpUrc9X2JVqmFglpjsAkPLj9B8o66THdl7wga/C4TCKcsbvLGjDiZVRueuOn2E=",
        "id": 2426
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        token = response.json().get("access_token")
        return token
    else:
        raise Exception("Ошибка авторизации: " + response.text)


# Вызов функции
try:
    token = get_auth_token()
    print("Полученный токен:", token)
except Exception as e:
    print(e)
