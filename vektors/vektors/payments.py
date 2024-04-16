import decimal
import hashlib
from urllib import parse
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
from django.http import HttpResponse
from django.contrib.auth.models import Group
from users.models import User

load_dotenv()
MERCHANT_LOGIN = os.getenv('MERCHANT_LOGIN')
MERCHANT_PASSWORD_TEST_1 = os.getenv('MERCHANT_PASSWORD_TEST_1')
MERCHANT_PASSWORD_TEST_2 = os.getenv('MERCHANT_PASSWORD_TEST_2')


def calculate_signature(*args) -> str:
    """Create signature MD5."""
    return hashlib.md5(':'.join(str(arg) for arg in args).encode()).hexdigest()


def parse_response(request: str) -> dict:
    """
    :param request: Link.
    :return: Dictionary.
    """
    params = {}

    for item in urlparse(request.build_absolute_uri()).query.split('&'):
        key, value = item.split('=')
        params[key] = value
    return params


def check_signature_result(
    order_number: int,  # invoice number
    received_sum: decimal,  # cost of goods, RU
    received_signature: hex,  # SignatureValue
    password: str,  # Merchant password
) -> bool:
    signature = calculate_signature(received_sum, order_number, password)
    if signature.lower() == received_signature.lower():
        return True
    return False


# Формирование URL переадресации пользователя на оплату.

def generate_payment_link(
    cost: decimal,  # Cost of goods, RU
    number: int,  # Invoice number
    description: str,  # Description of the purchase
    user_id: int,
    is_test=1,
    robokassa_payment_url='https://auth.robokassa.ru/Merchant/Index.aspx',
) -> str:

    merchant_login = MERCHANT_LOGIN
    merchant_password_1 = MERCHANT_PASSWORD_TEST_1
    user_id_for_sign = f'Shp_id={user_id}'
    signature = calculate_signature(
        merchant_login,
        cost,
        number,
        merchant_password_1,
        user_id_for_sign
    )

    data = {
        'MerchantLogin': merchant_login,
        'OutSum': cost,
        'InvId': number,
        'Description': description,
        'SignatureValue': signature,
        'IsTest': is_test,
        'Shp_id': user_id,
    }
    return f'{robokassa_payment_url}?{parse.urlencode(data)}'

# Проверка параметров в скрипте завершения операции (SuccessURL).


def check_success_payment(request) -> bool:
    """ Verification of operation parameters
    ("cashier check") in SuccessURL script.
    :param request: HTTP parameters
    """
    merchant_password_1 = MERCHANT_PASSWORD_TEST_1
    param_request = parse_response(request)
    cost = param_request['OutSum']
    number = param_request['InvId']
    signature = param_request['SignatureValue']

    if check_signature_result(number, cost, signature, merchant_password_1):
        return HttpResponse("Thank you for using our service")
    return HttpResponse('bad sign')


def result_payment(request) -> str:
    """Verification of notification (ResultURL).
    :param request: HTTP parameters.
    """
    if not request.method == 'POST':
        return HttpResponse('error')
    if request.method == 'POST':
        merchant_password_2 = MERCHANT_PASSWORD_TEST_2
        data = request.POST
        cost = int(data['OutSum'])
        number = data['InvId']
        signature = data['SignatureValue']
        user_id = data['Shp_id']
        user = User.objects.get(id=user_id)
        base_group = Group.objects.get(name="base")
        standart_group = Group.objects.get(name="standart")
        full_group = Group.objects.get(name="full")
        if cost == 1.00:
            user.groups.add(base_group)
        elif cost == 1.50:
            user.groups.add(standart_group)
        elif cost == 2.00:
            user.groups.add(full_group)
        else:
            print('hello')
        if check_signature_result(number, cost, signature,
                                  merchant_password_2):
            return HttpResponse(f'OK{data["InvId"]}')
        return HttpResponse('bad sign')
