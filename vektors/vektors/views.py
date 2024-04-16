from django.shortcuts import redirect, render
from random import randint
from vektors.payments import generate_payment_link, \
    result_payment, check_success_payment
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def base_pay_view(request):

    user_id = request.user.id
    cost = 1.00
    number = randint(1, 550000)
    description = 'Оплата базового курса'
    link = generate_payment_link(cost, number, description, user_id)
    return redirect(link)


def standart_pay_view(request):

    user_id = request.user.id
    cost = 1.50
    number = randint(1, 550000)
    description = 'Оплата стандартного курса'
    link = generate_payment_link(cost, number, description, user_id)
    return redirect(link)


def full_pay_view(request):

    user_id = request.user.id
    cost = 2.00
    number = randint(1, 550000)
    description = 'Оплата расширенного курса'
    link = generate_payment_link(cost, number, description, user_id)
    return redirect(link)


@csrf_exempt
def result_view(request):
    result = result_payment(request)
    return result


@csrf_exempt
def success_payment_view(request):
    if check_success_payment(request):
        return render(request, 'success_payment.html')
    else:
        return HttpResponse("bad sign")
