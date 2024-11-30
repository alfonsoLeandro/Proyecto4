from criptosistema import CriptoSistema


class CriptoSistema1(CriptoSistema):

    def __init__(self):
        self.a = 4
        self.b = 11

    def encriptar_texto(self, texto):
        vector = self.traducir_a_numeros(texto)
        vector = self.encriptar_numeros(vector)
        return self.traducir_a_texto(vector)

    def traducir_a_numeros(self, texto):
        res = []
        for c in texto:
            caracter = c.upper()
            if caracter not in CriptoSistema1.equivalentes:
                print(f"El caracter {c} no esta en el diccionario")
                continue
            res.append(CriptoSistema1.equivalentes[caracter])
        return res

    def traducir_a_texto(self, vector):
        res = []
        for n in vector:
            if n > 29:
                print(f"El numero {n} es mayor a 29")
                continue
            res.append(CriptoSistema1.equivalentes_inverso[n])
        return res

    def encriptar_numeros(self, vector):
        res = []
        for number in vector:
            res.append(self.encriptar_numero(number))
        return res

    def encriptar_numero(self, number: int):
        return (self.a * number + self.b) % 29

    # Desencriptación

    # Encuentra un numero x entre 0 y 28, para el cual se da que (a*x)%29 = 1
    def a_inverso(self):
        for x in range(29):
            if (self.a * x) % 29 == 1:
                return x
        return None

    # Desencriptación
    def desencriptar_texto(self, mensaje_encriptado):
        a_inv = self.a_inverso()
        if a_inv is None:
            raise ValueError("No se encontró el inverso multiplicativo")

        # Convertir caracteres a índices, aplicar fórmula de desencriptación, obtener original a partir de indice
        original = []
        for char in mensaje_encriptado:
            y = CriptoSistema.equivalentes[char]
            x = (a_inv * (y - self.b)) % 29
            original.append(CriptoSistema.equivalentes_inverso[x])

        return "".join(original)