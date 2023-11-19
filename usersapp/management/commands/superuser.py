from django.core.management import BaseCommand

from usersapp.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@yandex.ru',
            first_name='Admin',
            last_name='#',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('1234')
        user.save()

