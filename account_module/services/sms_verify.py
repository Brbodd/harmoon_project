import random
import requests

from django.conf import settings

from account_module.models import PhoneVerification


def send_otp(phone_number):

    code = str(random.randint(10000, 99999))

    PhoneVerification.objects.create(
        phone_number=phone_number,
        code=code
    )

    url = "https://api.sms.ir/v1/send/verify"

    headers = {
        "X-API-KEY": settings.SMSIR_API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = {
        "Mobile": phone_number,
        "TemplateId": settings.SMSIR_TEMPLATE_ID,
        "Parameters": [
            {
                "Name": "Code",
                "Value": code
            }
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=10
    )

    # print("SMS STATUS:", response.status_code)
    # print("SMS RESPONSE:", response.text)

    return response