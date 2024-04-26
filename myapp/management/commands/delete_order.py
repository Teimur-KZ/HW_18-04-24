'''Собственная команда для создания пользователя'''
from django.core.management.base import BaseCommand
from myapp.models import Client, Order, Product


class Command(BaseCommand):
    help = 'Удаление заказа из базы данных'

    def add_arguments(self,parser):
        parser.add_argument('pk', type=int, help='ID заказа который нужно удалить')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        product = order.product.first()
        if order is not None:
            if input(f'Заказ №{order.pk} - {product} - Сумма заказа: {order.total_price} \nВы уверены, что хотите удалить заказ с ID: {pk}? (y/n) ') == 'y':
                order.delete()
                self.stdout.write(f'Заказ {pk} удален!')
            else:
                self.stdout.write(f'Заказ {pk} не удален!')
        else:
            self.stdout.write(f'Заказ {pk} не найден')

# запуск команды: py manage.py delete_order -h или py manage.py delete_order 10

# py manage.py delete_order 100
# Заказ №100 - Название товара: Название товар_10, Цена товара: 110.00 - Сумма заказа: 1100.00
# Вы уверены, что хотите удалить заказ с ID: 100? (y/n) y
# Заказ 100 удален!
