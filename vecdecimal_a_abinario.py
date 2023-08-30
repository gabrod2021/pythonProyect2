
import random
n = int(input("Ingrese la longitud del vector: "))
# Genero un vector con números aleatorios entre 1 y 20
VecDec = [random.randint(1, 20) for _ in range(n)]
print("Vector decimal:",VecDec)
print("Vector binario:",end=" ")
VecBin = []
for decimal in VecDec:
    temp_bin = []  # Crea una lista temporal para el número binario
    while decimal >= 1:
        temp_bin.insert(0, decimal % 2)
        decimal = decimal // 2
    VecBin.extend(temp_bin)  # Agrega los dígitos binarios al resultado fina
    print(" ".join(map(str, temp_bin)),end=" - ")

"""He realizado las siguientes modificaciones en el código:
He cambiado binario = VecBin a VecBin.extend(temp_bin) para agregar correctamente los dígitos binarios al resultado final.
He agregado la creación de una lista temp_bin para almacenar temporalmente los dígitos binarios de cada número decimal.
Con estas correcciones, el código debería imprimir la lista original de números decimales VecDec y 
luego la representación binaria correspondiente en el mismo orden. Asimismo se puede mostrar en el bucle while,
cada numero binario en la lista temporal."""


#OTRA FORMA DE HACERLO
"""VecBin = []
VecDec = [1, 3, 5, 8, 10, 20, 17, 15, 13, 9, 11, 4, 2, 18, 7, 6, 19, 12, 14, 16]
binario = 0
i = 0
for decimal in VecDec:
   while decimal >= 1:
        digito = decimal % 2
        decimal = decimal // 2
        binario += digito * (10 ** i)
        i += 1
print(binario)"""









