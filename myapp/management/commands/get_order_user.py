'''Собственная команда для создания пользователя'''
from django.core.management.base import BaseCommand
from myapp.models import Client, Order, Product


class Command(BaseCommand):
    help = 'Все заказы клиента'

    def add_arguments(self, parser):
        #parser.add_argument('email', type=str, help='Email клиента')
        parser.add_argument('pk', type=int, help='ID клиента')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        orders = Order.objects.filter(client=client)
        if client is not None and orders.exists(): # Если клиент найден и у него есть заказы
            orders = Order.objects.filter(client=client)
            intro = f'Все заказы клиента {client.name}\n'
            text = '\n'.join(f'ID клиента: {pk} - кол заказов: {order.quantity} - Сумма заказа: {order.total_price}' for order in orders)
            self.stdout.write(f'{intro}{text}')
        elif client is not None and orders.exists() == False:
            self.stdout.write(f'У клиента {client.name} нет заказов')
        else:
            self.stdout.write('Клиент не найден')
# запуск команды: py manage.py get_order_user 1 -h или py manage.py get_order_user 5
# Все заказы клиента Имя_клиента5
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 110.00
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 220.00
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 330.00
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 440.00
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 550.00
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 660.00
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 770.00
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 880.00
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 990.00
# ID клиента: 5 - кол заказов: 10 - Сумма заказа: 1100.00

# py manage.py get_order_user 11
# У клиента Виктор нет заказов

