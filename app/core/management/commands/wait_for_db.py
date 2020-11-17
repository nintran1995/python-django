import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for db ...')
        db_conn = None
        while not db_conn:
            try:
                # get the database with keyword 'default' from settings.py
                db_conn = connections['default']
                # prints success message in green
                self.stdout.write(self.style.SUCCESS('db_available'))
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second ...')
                time.sleep(1)

        
