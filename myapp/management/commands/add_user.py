'''Собственная команда для создания пользователя'''
from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Добавление нового пользователя в базу данных'

    def handle(self, *args, **options):
        client = Client(
            name='Виктор',
            email='viktor@test.ru',
            phone='+7(999)999-99-96',
            address='Moscow'
        )
        if Client.objects.filter(email=client.email).exists(): # проверка на существование клиента, #.exists() - возвращает True, если объект существует
            self.stdout.write(f'Клиент с email: {client.email} уже существует!')
            return
        client.save()
        self.stdout.write(f'Клиент: {client.name} - {client.email} создан!')

# запуск команды: py manage.py add_user -h или py manage.py add_user

# py manage.py add_user
# Клиент: Виктор - viktor@test.ru создан!
