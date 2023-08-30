
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










