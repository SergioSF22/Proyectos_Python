"""Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado."""
def usd_eur(usd):
    return usd * 0.9
dolares = 500
print(f"{dolares}$ son al cambio {usd_eur(dolares)}€")
