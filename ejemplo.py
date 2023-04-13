from pila import Pila
from pila import Pila as apilar
from pila import Pila as desapilar
from pila import Pila as pila_vacia



"""
 EJERMPLOS DE PILA MULTIPLE
En este caso se tiene una pila de números enteros 
y se desea dividirla en dos pilas, 
una con los números pares y otra con los impares:
"""

pdatos = Pila() # pila datos la principal
ppar = Pila() # pila para número pares
pimpar = Pila() # pila para número impares
dato = int(input("Ingrese un número - 0 para salir "))
def numero():
    while (dato==0): # para salir del procesar el algoritmo
        apilar(pdatos,dato)
        dato = int(input("Ingrese un número - 0 para salir "))
    while (not Pila.pila_vacia(pdatos)): #ver la pila proncipal esta vacia o no
        dato = Pila.desapilar(pdatos) #desapilar el pdato para despues almacena de otro pila
        if (dato %2 ==0):
            dato = Pila.apilar(ppar,dato) #par apilar el dato en la pila par
        else:
            dato = Pila.apilar(pimpar,dato) #impar apilar el dato en la pila impar
    while (not Pila.pila_vacia(ppar)):
        dato= Pila.desapilar(ppar)# mostrar los datos almacena en la pila de par o impar
        return print(dato),print(ppar), print(pimpar)
letra=numero(pdatos)