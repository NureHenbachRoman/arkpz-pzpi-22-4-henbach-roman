from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

from LaundroMate_backend.enums import UserRole


class Command(BaseCommand):
    help = 'Create user groups'

    def handle(self, *args, **kwargs):
        roles = [role.value for role in UserRole]
        print(roles)
        for role in roles:
            Group.objects.get_or_create(name=role)
        self.stdout.write(self.style.SUCCESS('Successfully created user groups'))
