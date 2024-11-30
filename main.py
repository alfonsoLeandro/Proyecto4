from criptosistema1 import CriptoSistema1
from criptosistema2 import CriptoSistema2

TEXTO = ("En el principio creo Dios los cielos y la tierra Y la tierra estaba desordenada y vacia y las tinieblas"
         " estaban sobre la faz del abismo y el Espiritu de Dios se movia sobre la faz de las aguas")

# Funciones utilitarias
def repeticiones_caracteres(texto):
    letras_instancias = {}
    for c in texto:
        if c not in letras_instancias:
            letras_instancias[c] = 0
        letras_instancias[c] = letras_instancias[c] + 1
    return dict(sorted(letras_instancias.items(), key=lambda item: item[1], reverse=True))


def posiciones(caracter, texto):
    res = []
    for i in range(len(texto)):
        if texto[i] == caracter:
            res.append(i)
    return res


# Ejecución del programa, logs en consola

print(f"Texto original: {TEXTO}")
print()

cs1 = CriptoSistema1()
encriptado1 = cs1.encriptar_texto(TEXTO)
print("========================== CS1 ==========================")
print(f"Texto encriptado: {encriptado1}")
caracter_mas_repetido = list(repeticiones_caracteres(TEXTO).keys())[0]
caracter_mas_repetido_encriptado = list(repeticiones_caracteres(encriptado1).keys())[0]
print(f"Caracter más repetido \"{caracter_mas_repetido}\", posiciones: {posiciones(caracter_mas_repetido, TEXTO)}")
print(f"Caracter más repetido de texto encriptado: \"{caracter_mas_repetido_encriptado}\","
      f" posiciones: {posiciones(caracter_mas_repetido_encriptado, encriptado1)}")
print(f"Podemos asumir que el caracter \"{caracter_mas_repetido}\" encriptado,"
      f" es \"{caracter_mas_repetido_encriptado}\"")
desencriptado1 = cs1.desencriptar_texto(encriptado1)
print(f"Desencriptado: {desencriptado1}")


print()

print("========================== CS2 ==========================")
cs2 = CriptoSistema2()
encriptado2 = cs2.encriptar_texto(TEXTO)
print(f"CS2 - Texto encriptado: {encriptado2}")
caracter_mas_repetido_encriptado_2 = list(repeticiones_caracteres(encriptado1).keys())[0]
print(f"Caracter más repetido \"{caracter_mas_repetido}\", posiciones: {posiciones(caracter_mas_repetido, TEXTO)}")
print(f"Caracter más repetido de texto encriptado: \"{caracter_mas_repetido_encriptado_2}\","
      f" posiciones: {posiciones(caracter_mas_repetido_encriptado_2, encriptado2)}")
print(f"No podemos asumir que el caracter \"{caracter_mas_repetido}\" encriptado, es "
      f"\"{caracter_mas_repetido_encriptado_2}\", ya que por mas que sean ambos los mas repetidos, "
      f"no se encuentran en las mismas posiciones")
desencriptado2 = cs2.desencriptar_texto(encriptado2)
print(f"Desencriptado: {desencriptado2}")

