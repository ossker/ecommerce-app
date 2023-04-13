from io import BytesIO
from celery import task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@task
def payment_completed(order_id):
    """
    Zadanie wysyła e-mailem powiadomienie po pomyślnym utworzeniu zamówienia
    """
    order = Order.objects.get(id=order_id)

    subject = f'Mój sklep - rachunek nr {order.id}'
    message = 'W załączniku przesyłamy rachunek dla ostatniego zakupu.'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])

    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    email.send()