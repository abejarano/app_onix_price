from django.db import models
from django.utils import timezone


# Create your models here.


class PorcentajesIntercambio(models.Model):
    procentaje_ganacia_venta = models.DecimalField(
        max_digits=16, decimal_places=8, null=False, blank=False
    )

    class Meta:
        db_table = 'onx_porcentaje_ganancia'


class PrecioBtcLocalbitcoin(models.Model):
    precio_btc_usd_avg_1h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    precio_btc_usd_avg_6h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    precio_btc_usd_avg_12h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    precio_btc_usd_avg_24h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    precio_btc_bs_avg_1h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    precio_btc_bs_avg_6h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    precio_btc_bs_avg_12h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    precio_btc_bs_avg_24h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'onx_precio_btc'


class PrecioOnix(models.Model):
    btc_onx_venta = models.DecimalField(
        max_digits=16, decimal_places=8, null=False, blank=False
    )
    onx_bs_venta = models.DecimalField(
        max_digits=16, decimal_places=8, null=False, blank=False
    )
    usd_onx_venta = models.DecimalField(
        max_digits=16, decimal_places=8, null=False, blank=False
    )
    btc_onx_compra = models.DecimalField(
        max_digits=16, decimal_places=8, null=False, blank=False
    )
    onx_bs_compra = models.DecimalField(
        max_digits=16, decimal_places=8, null=False, blank=False
    )
    usd_onx_compra = models.DecimalField(
        max_digits=16, decimal_places=8, null=False, blank=False
    )
    procentaje_intercambio = models.ForeignKey(
        PorcentajesIntercambio,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'onx_historico_precio'


class Yobit(models.Model):
    btc_onx = models.DecimalField(
        max_digits=16, decimal_places=8, null=False, blank=False)
    usd_btc = models.DecimalField(
        max_digits=16, decimal_places=8, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'onx_yobit'
