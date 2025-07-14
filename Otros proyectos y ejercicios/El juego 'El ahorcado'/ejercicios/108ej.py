"""Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio"""
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for rasgo,valor in kwargs.items():
        print(f"- {rasgo}: {valor}")

describir_persona("Sergio",edad=22,color_ojos="Marrón",altura=1.71)