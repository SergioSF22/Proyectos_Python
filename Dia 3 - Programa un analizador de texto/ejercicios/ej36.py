"""Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

"difícil" --> "fácil"

"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas."""
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase = frase.replace("difícil","fácil")
frase = frase.replace("mala","buena")
print("Nueva frase: ", frase)