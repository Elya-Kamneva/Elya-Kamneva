import requests


def get_auth_token():
    url = "https://test.altyn-i.kz/auth/oauth/token?grant_type=Password&user_type=customer&username=OQOaV9g47BOt5U62544p1v8TaxUQzsZuKl0UbPH4kYhvrXERq8+KKeToSj173qY1x4DeMceBI0ab3YIER2KDZ/RBIbzJQsMLYHVWaPH0Xq52ZLf9uOLhd/O4aaoCXBbfcwikpu8tWv1EgMYTvlUhBwDsIv6M8frM+Z2PPbQsgso=&password=dJTKULnTKWHUpt/bUUUud1xdlZ0znTVYbMZiF9iwJ7QwgSOXZrcMuXz26on9iSZ9LQ7yCOXIJsb+nT+ViroqlXjNPqhH/ka+nwlGwSwc6qum47slMNI+yVDIFZIkfdY7R3ylGPnJFyFdFTGhysO6fL16KdEJVqtaI579fVthoSQ=&verificationCode=111111"  # URL для авторизации
    headers = {"Content-Type": "application/json", "Authorization": "Basic V0VCOg=="}


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
