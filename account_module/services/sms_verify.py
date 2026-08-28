import random

from smsiran import SmsIR

from django.conf import settings

from account_module.models import PhoneVerification

def send_otp(phone_number):

    code = str(random.randint(10000, 99999))

    PhoneVerification.objects.create(
        phone_number=phone_number,
        code=code
    )

    sms_ir = SmsIR(
        settings.SMSIR_API_KEY,
        settings.SMSIR_LINE_NUMBER
    )

    sms_ir.send_verify_code(
        number=phone_number,
        template_id=settings.SMSIR_TEMPLATE_ID,
        parameters=[
            {
                "name": "code",
                "value": code
            }
        ]
    )

    return code

