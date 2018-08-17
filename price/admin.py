from django.contrib import admin
from .models import Yobit, PrecioBtcLocalbitcoin
# Register your models here.


@admin.register(Yobit)
class AdminLocalBitcoin(admin.ModelAdmin):
    list_display = ('btc_onx', 'usd_btc',)


@admin.register(
    PrecioBtcLocalbitcoin
)
class AdminLocalBitcoin(admin.ModelAdmin):
    list_display = ('precio_btc_usd_avg_1h', 'precio_btc_usd_avg_6h',
                    'precio_btc_usd_avg_12h', 'precio_btc_usd_avg_24h',
                    'precio_btc_bs_avg_1h', 'precio_btc_bs_avg_6h',
                    'precio_btc_bs_avg_12h', 'precio_btc_bs_avg_24h',)
