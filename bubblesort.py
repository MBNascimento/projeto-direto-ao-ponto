#-*-coding:utf8;-*-
#qpy:console
#bubblesort.py
def espaco():
    print(" ")
espaco()

valores = [2, 3, 7, 4, 1]

desordenado = True

while desordenado :
    # assumindo que não encontremos mais pares fora de ordem
    desordenado = False
    # buscando elementos fora de ordem
    for i in range (len(valores)-1):
        if valores[i] > valores[i+1]:
            # invertendo os elementos se ordem 
            valores [i], valores[i+1] = valores[i+1], valores[i]
            desordenado = True
            print (valores)
