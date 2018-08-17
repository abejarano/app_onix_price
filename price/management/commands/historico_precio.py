#!/usr/bin/env python
from django.core.management.base import BaseCommand

import os

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))) + '/commands/'


class Command(BaseCommand):
    help = "Comando para recabar un historico de precios"

    def handle(self, *args, **options):
        pass
