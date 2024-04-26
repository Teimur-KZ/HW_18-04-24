'''Собственная команда для создания пользователя'''
from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Delete user'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email of user')

    def handle(self, *args, **kwargs):
        email = kwargs.get('email')
        client = Client.objects.filter(email=email).first()
        if client:
            if input(f'Вы уверены, что хотите удалить клиента с email: {email}? (y/n) ') == 'y':
                client.delete()
                self.stdout.write(f'Клиент с email: {email} удален!')
            else:
                self.stdout.write(f'Клиент с email: {email} не удален!')
        else:
            self.stdout.write(f'Клиент с email: {email} не найден!')


# запуск команды: py manage.py delete_user -h или py manage.py delete_user viktor@test.ru
