# Onix prices buy.

Es una aplicación python que calcular el precio de venta de onix en bolivares y dolares. La aplicación esta dirigida
para el país de venzuela, sin emnbargo puede ser adaptada para otros paises.

# Librerias.

django==2.1

python3.6

# Instalar la aplicación

pip install django-price-onixcoin

Posteriormente podrá crear unos crontad que ejecuete los siguientes comandos dentro de tu proyecto django

python3 manager.py price_btc_localbitcoin (cada 20 min)

python3 manager.py yobit_onix (cada 1 min)

python3 manager.py price_onix (cada 1 min)