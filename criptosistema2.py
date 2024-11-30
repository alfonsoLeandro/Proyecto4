from criptosistema import CriptoSistema
import numpy as np


class CriptoSistema2(CriptoSistema):

    def __init__(self):
        # self.A = generar_matriz()
        self.A = np.array([
            [8, 13, 1],
            [3, 10, 6],
            [13, 26, 7]
        ])
        # Vector Arbitrario
        self.b = [4, 5, 6]

    # Generar una matriz A aleatoria con determinante 1
    # def generar_matriz():
    #     while True:
    #         A = np.random.randint(0, 29, (3, 3))  # Generar matriz con coeficientes entre 0 y 28
    #         if round(np.linalg.det(A)) == 1:      # Verificar que det(A) = 1
    #             return A
    # Ejecuto y dejo el resultado en una variable A para que sea siempre la misma
    # De lo contrario A cambiaria en cada ejecucion, lo que significa que si encripto algo y corto el programa, ya no se podra desencriptar mas

    def encriptar_texto(self, texto):
        vector = self.vectorizar(texto)
        texto_cript = self.encriptar_todos_los_bloques(vector)
        texto_cript = self.convertir_a_caracteres(texto_cript)
        return ''.join(texto_cript)

    # Utilidad
    def convertir_a_caracteres(self, encrypted_list):
        return [CriptoSistema.equivalentes_inverso[num] for num in encrypted_list if num in CriptoSistema.equivalentes_inverso]

    # Utilidad
    def convertir_a_numeros(self, char_list):
        return [CriptoSistema.equivalentes[char] for char in char_list if char in CriptoSistema.equivalentes]

    # Vectorizar
    def dividir_en_bloques(self, texto, tamaño=3):
        bloques = [texto[i:i + tamaño] for i in range(0, len(texto), tamaño)]
        if len(bloques[-1]) < tamaño:
            bloques[-1] = bloques[-1].ljust(tamaño, ' ')
        return bloques

    # Vectorizar
    def convertir_a_vector(self, bloques):
        vector = []
        for bloque in bloques:
            for char in bloque:
                # Convertir cada carácter usando el mapeo
                vector.append(CriptoSistema.equivalentes.get(char.upper(), -1))  # Valor -1 si el carácter no está en el mapeo
        return vector

    # Vectorizar
    def dividir_vector_en_bloques(self, vector, tamano=3):
        return [vector[i:i + tamano] for i in range(0, len(vector), tamano)]

    # Funcion Principal: Vectorizar
    def vectorizar(self, texto):
        result = self.dividir_en_bloques(texto)
        result = self.convertir_a_vector(result)
        result = self.dividir_vector_en_bloques(result, tamano=3)
        return result

    # Encriptación
    def encriptar_bloque(self, x, mod=29):
        x = np.array(x).reshape(-1, 1)  # Asegurar que x sea un vector columna
        b = np.array(self.b).reshape(-1, 1)
        resultado = (np.dot(self.A, x) + b) % mod  # Aplicar transformación lineal y módulo
        return resultado.flatten()

    # Encriptación
    def encriptar_todos_los_bloques(self, vector, mod=29):
        resultados = []
        for bloque in vector:
            resultado = self.encriptar_bloque(bloque, mod)
            resultados.extend(int(x) for x in resultado)
        return resultados

    # Desencriptar
    def mod_inverse(self, matrix, mod=29):
        """
        Returns the modular inverse of a matrix modulo `mod`.
        Uses the Extended Euclidean Algorithm for matrix inversion.
        """
        det = int(np.round(np.linalg.det(matrix)))  # Determinant of the matrix
        det_inv = pow(det, -1, mod)  # Modular inverse of the determinant

        # Inverse of a 3x3 matrix in mod `mod`
        adjugate_matrix = np.round(np.linalg.inv(matrix) * det).astype(int) % mod
        inverse_matrix = (adjugate_matrix * det_inv) % mod
        return inverse_matrix

    # Desencriptar
    def desencriptar(self, encriptado, mod=29):
        encriptado = np.array(encriptado, dtype=int)
        A = np.array(self.A, dtype=int)
        b = np.array(self.b, dtype=int).reshape(-1, 1)

        tamano_bloques = A.shape[0]
        if len(encriptado) % tamano_bloques != 0:
            raise ValueError(f"El largo del vector encriptado debe ser un multiplo del tamaño de bloques ({tamano_bloques}).")

        bloques_encriptados = [encriptado[i:i + tamano_bloques] for i in range(0, len(encriptado), tamano_bloques)]
        A_inv = self.mod_inverse(A, mod)
        original = []

        # Desencriptar cada bloque
        for bloque in bloques_encriptados:
            bloque = np.array(bloque).reshape(-1, 1)
            y = (bloque - b) % mod
            x = np.dot(A_inv, y) % mod
            original.extend(x.flatten())

        return original

    # Funcion Principal: Desencriptar
    def desencriptar_texto(self, char_list, mod=29):
        encrypted_numbers = self.convertir_a_numeros(char_list)
        decrypted_numbers = self.desencriptar(encrypted_numbers, mod)
        original_chars = self.convertir_a_caracteres(decrypted_numbers)
        return ''.join(original_chars)
