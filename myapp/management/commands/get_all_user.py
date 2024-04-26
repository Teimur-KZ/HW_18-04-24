'''Собственная команда для создания пользователя'''
from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Список всех клиентов'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(f'ID №{client.pk} >>> {client.name} - {client.email} - {client.phone} - {client.address}')

# запуск команды: py manage.py get_all_user -h или py manage.py get_all_user
# py manage.py get_all_user
# ID №1 >>> Имя_клиента1 - email_client1_1714030681.532518@test.ru - +7(999)999-99-2 - Адрес_1
# ID №2 >>> Имя_клиента2 - email_client2_1714030681.6908042@test.ru - +7(999)999-99-4 - Адрес_2
# ID №3 >>> Имя_клиента3 - email_client3_1714030681.8641467@test.ru - +7(999)999-99-6 - Адрес_3
# ID №4 >>> Имя_клиента4 - email_client4_1714030682.0385628@test.ru - +7(999)999-99-8 - Адрес_4
# ID №5 >>> Имя_клиента5 - email_client5_1714030682.2115014@test.ru - +7(999)999-99-10 - Адрес_5
# ID №6 >>> Имя_клиента6 - email_client6_1714030682.4012036@test.ru - +7(999)999-99-12 - Адрес_6
# ID №7 >>> Имя_клиента7 - email_client7_1714030682.5774276@test.ru - +7(999)999-99-14 - Адрес_7
# ID №8 >>> Имя_клиента8 - email_client8_1714030682.738411@test.ru - +7(999)999-99-16 - Адрес_8
# ID №9 >>> Имя_клиента9 - email_client9_1714030682.9476714@test.ru - +7(999)999-99-18 - Адрес_9
# ID №10 >>> Имя_клиента10 - email_client10_1714030683.1211154@test.ru - +7(999)999-99-20 - Адрес_10
