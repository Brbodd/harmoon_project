import requests

from django.conf import settings


def send_booking_sms(full_name, phone_number, reserv_date, reserv_time):

    url = "https://api.sms.ir/v1/send/bulk"

    message_text = (
        f"رزرو جدیدی ثبت شد.\n"
        f"نام و نام خانوادگی: {full_name}\n"
        f"شماره تماس: {phone_number}\n"
        f"تاریخ: {reserv_date}\n"
        f"زمان: {reserv_time.strftime('%H:%M')}"
    )

    headers = {
        "X-API-KEY": settings.SMSIR_API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = {
        "lineNumber": settings.SMSIR_LINE_NUMBER,
        "messageText":  message_text,
        "mobiles": [
            "09382660324"
        ],
        
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=10
    )

    return response
