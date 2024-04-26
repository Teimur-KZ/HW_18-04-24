'''Собственная команда для создания пользователя'''
from django.core.management.base import BaseCommand
from myapp.models import Client, Order, Product


class Command(BaseCommand):
    help = 'Изменить количество товара в заказе и заменить товар новый товар'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID заказа')
        parser.add_argument('quantity', type=int, help='Количество товара')
        parser.add_argument('product', type=int, help='ID товара')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk') # ID заказа
        quantity = kwargs.get('quantity') # Количество товара
        product = kwargs.get('product') # ID товара
        order = Order.objects.filter(pk=pk).first() # Получаем заказ по ID
        product = Product.objects.filter(pk=product).first() # Получаем товар по ID
        if order is not None and product is not None: # Если заказ и товар найдены
            order.quantity = quantity # Изменяем количество товара в заказе
            order.total_price = product.price * quantity
            order.save()
            order.product.clear()
            order.product.add(product)
            self.stdout.write(f'Заказ {pk} изменен!')
        else:
            self.stdout.write('Заказ или товар не найден')

# id заказа, количество товара, id товара
# запуск команды: py manage.py get_change_order 5 2 4
# заказ до:
# ID заказа: 5 - ID клиента: 1 Имя клиента: Имя_клиента1 - ID товара: 5 - Количество: 10 - Сумма заказа: 550.00
# ID заказа: 5 - Название товар_5 - 10 - 550.00

# py manage.py get_change_order 5 2 4
# Заказ 5 изменен!

# заказ после:
# ID заказа: 5 - ID клиента: 1 Имя клиента: Имя_клиента1 - ID товара: 4 - Количество: 2 - Сумма заказа: 88.00
# ID заказа: 5 - Название товар_4 - 2 - 88.00

