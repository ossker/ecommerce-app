from myshop.celery import app
from django.core.mail import send_mail
from .models import Order

@app.task
def order_created(order_id):
    """
        Zadanie wysyłające powiadomienie za pomocą wiadomości e-mail
        po zakończonym powodzeniem utworzeniu obiektu zamówienia.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Zamówienie nr {order.id}'
    message = f'Witaj, {order.first_name}!\n\nZłożyłeś zamówienie w naszym sklepie. Identyfikator zamówienia to {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent