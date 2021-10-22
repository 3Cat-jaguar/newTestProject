from django.core.management.base import BaseCommand, CommandError
from openapi.models import api_table
import os
from django.shortcuts import render
from openapi.models import api_table
import requests
import datetime
from datetime import datetime, date, timezone
from django.db.models import Q
from Tables.views import create_db


class Command(BaseCommand):
    def handle(self, *args, **options):
        # urldate = datetime.now().date()
        urldate = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day - 1)
        print(urldate)
        create_db(urldate, 1)
            # i = 1
            # while i < 5:
            #     create_db(urldate, i)
            #     i += 1

