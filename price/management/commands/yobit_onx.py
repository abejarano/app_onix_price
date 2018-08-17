#!/usr/bin/env python
from django.core.management.base import BaseCommand
from apps.onx.models import Yobit
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

        url = 'https://yobit.net/api/2/btc_usd/ticker'
        r = requests.get(url, headers=headers)
        resp = r.json()

        usd_btc = resp['ticker']['sell']

        Yobit(
            btc_onx_buy=btc_onx,
            usd_btc_buy=usd_btc,
        ).save()
