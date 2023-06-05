from typing import Any, Optional
from psycopg2 import OperationalError as Psycopg20Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

import time


class Command(BaseCommand):
    """Django Commant to wait for database"""
    
    def handle(self, *args, **options):
        self.stdout.write('waiting for database...')
        db_up = False
        
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up= True
            except(Psycopg20Error, OperationalError):
                self.stdout.write('Database unvalilable, wait 1 second...')
                time.sleep(1)
                
        self.stdout.write(self.style.SUCCESS('Database available'))