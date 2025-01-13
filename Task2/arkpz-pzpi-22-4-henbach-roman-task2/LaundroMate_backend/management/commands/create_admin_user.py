from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
import getpass

from LaundroMate_backend.enums import UserRole


class Command(BaseCommand):
    help = 'Create an admin user'

    def handle(self, *args, **kwargs):
        username = input('Enter username: ')

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING('User with this username already exists'))
            user = User.objects.get(username=username)
            update = input(f'Do you want to update {username}? (y/N): ')
            if update.lower() == 'y':
                self.update_admin(user)
            return

        password = getpass.getpass('Enter password: ')
        email = input('Enter email: ')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.groups.add(Group.objects.get(name=UserRole.ADMIN.value))
        self.stdout.write(self.style.SUCCESS('Successfully created admin user'))

    def update_admin(self, user):
        password = getpass.getpass('Enter password (leave empty to keep previous password): ')
        if password.strip() != '':
            user.set_password(password)

        email = input('Enter email (leave empty to keep previous email): ')
        if email.strip() != '':
            user.email = email

        user.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated admin user'))
