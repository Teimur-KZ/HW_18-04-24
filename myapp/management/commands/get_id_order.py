'''Собственная команда для создания пользователя'''
from django.core.management.base import BaseCommand
from myapp.models import Client, Order, Product


class Command(BaseCommand):
    help = 'Найти заказ по ID заказа'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID заказа')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            client = order.client
            product = order.product.first()
            self.stdout.write(f'ID заказа: {pk} - ID клиента: {client.pk} Имя клиента: {client.name} - ID товара: {product.pk} - Количество: {order.quantity} - Сумма заказа: {order.total_price}')
            self.stdout.write(f'ID заказа: {pk} - {product.name} - {order.quantity} - {order.total_price}')
        else:
            self.stdout.write('Заказ не найден')

# запуск команды: py manage.py get_id_order 1 -h или py manage.py get_id_order 5
# ID заказа: 5 - ID клиента: 1 Имя клиента: Имя_клиента1 - ID товара: 5 - Количество: 10 - Сумма заказа: 550.00