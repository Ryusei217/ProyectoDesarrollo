from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="cristian").exists():
            User.objects.create_superuser("cristian", "cristian@iqsd.co", "Admin.2017")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
