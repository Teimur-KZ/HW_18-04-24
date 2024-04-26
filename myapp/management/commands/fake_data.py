'''Собственная команда для создания пользователя'''
from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order
import time

class Command(BaseCommand):
    help = 'Заполнение базы данных тестовыми данными'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество клиентов')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        products = []  # список для хранения товаров
        for j in range(1, count + 1):
            product = Product(
                name=f'Название товар_{j}',
                description=f'Описание товара_{j}',
                price=j*11,
                quantity=j*10
            )
            product.save()
            products.append(product)  # добавляем товар в список

        for i in range(1, count + 1):
            client = Client(
                name=f'Имя_клиента{i}',
                email=f'email_client{i}_{time.time()}@test.ru',
                phone=f'+7(999)999-99-{i*2}',
                address=f'Адрес_{i}'
            )
            client.save()
            for product in products:  # для каждого товара в списке
                order = Order(client=client, quantity=j, total_price=product.price * j)
                order.save()
                order.product.add(product)

        self.stdout.write(f'База данных заполнена тестовыми данными!')


'''
class Command(BaseCommand):
    help = 'Заполнение базы данных тестовыми данными'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество клиентов')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(
                name=f'Имя_клиента{i}',
                email=f'email_client{i}_{time.time()}@test.ru',
                phone=f'+7(999)999-99-{i*2}',
                address=f'Адрес_{i}'
            )
            client.save()
        for j in range(1, count + 1):
            product = Product(
                name=f'Название товар_{j}',
                description=f'Описание товара_{j}',
                price=j*11,
                quantity=j*10
            )
            product.save()
            order = Order(client=client, quantity=j, total_price=product.price * j) # если товаров больше одного, то общая сумма заказа увеличивается
            order.save()
            order.product.add(product)

        self.stdout.write(f'База данных заполнена тестовыми данными!')
'''
        # запуск команды: py manage.py fake_data 10