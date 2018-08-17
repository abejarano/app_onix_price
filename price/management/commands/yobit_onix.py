#!/usr/bin/env python
from django.core.management.base import BaseCommand
from decimal import Decimal
from price.models import Yobit
import os
import requests

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))) + '/commands/'


class Command(BaseCommand):
    help = "Comando para registar los valores de onx en yobit"

    def handle(self, *args, **options):
        headers = {'Content-Type': 'application/json'}
        url = 'https://yobit.net/api/2/onx_btc/ticker'
        r = requests.get(url, headers=headers)
        resp = r.json()

        btc_onx = resp['ticker']['sell']
        print(btc_onx)

        url = 'https://yobit.net/api/2/btc_usd/ticker'
        r = requests.get(url, headers=headers)
        resp = r.json()

        usd_btc = resp['ticker']['sell']
        print(usd_btc)

        Yobit(
            btc_onx=Decimal(btc_onx),
            usd_btc=Decimal(usd_btc),
        ).save()
