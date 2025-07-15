import os
import requests

def get_campaigns():
    token = os.getenv("y0__xCu0-CTARiy6zggm5Dg4RMwpc6l_AcX_bBfhELlTEbmfBC9huROFbh4mA")
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Login": os.getenv("smart.business.technologies@yandex.ru"),
        "Accept-Language": "ru",
        "Content-Type": "application/json"
    }
    body = {
        "method": "get",
        "params": {
            "SelectionCriteria": {}
        }
    }
    response = requests.post("https://api.direct.yandex.com/json/v5/campaigns", json=body, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return f"Ошибка при получении данных: {e}"
