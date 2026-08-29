import requests
from django.conf import settings


def send_otp(phone_number, template_id, code):
    url = "https://api.sms.ir/v1/send/verify"

    headers = {
        "X-API-KEY": settings.SMSIR_API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = {
        "Mobile": phone_number,
        "TemplateId": template_id,
        "Parameters": [
            {
                "Name": "Code",
                "Value": str(code),
            }
        ],
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=10
    )

    return response