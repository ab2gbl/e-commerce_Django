from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Flushes the database and loads data from data.json'

    def handle(self, *args, **kwargs):
        self.stdout.write("Flushing database...")
        call_command('flush', '--noinput')
        self.stdout.write("Loading data from data.json...")
        call_command('loaddata', 'data.json')
        self.stdout.write(self.style.SUCCESS("Database reset complete."))