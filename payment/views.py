from django.shortcuts import render, get_object_or_404

from orders.models import Order


def payment_process(request):
    # Get Order ID From Session
    order_id = request.session.get('order_id')

    # Get The Order object
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

