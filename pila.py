class nodoPila(object):
    def __init__(self ):
        self.info = None
        self.sig = None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(pila, dato): #self=pila de estadica a dinamino
        """Apila el dato sobre la cima  de la pila"""
        nodo= nodoPila() #crear nodo
        nodo.info = dato # dato almacenado en la info del nodo
        nodo.sig = pila.cima #sig de nodo es la cima de la pila
        pila.cima = nodo # que a su vez es un nuevo nodo con  info y sig
        pila.tamanio += 1 # el tamanio de la pila se aumenta 1

    def desapilar(pila): #solo es necesario la pila porque el dato es pila.cima.info
        """ Desapilar el elemento en la cima de la pila y lo devuelve"""

        dato = pila.cima.info #el dato almacenado en la info de nodo de la pila
        pila.cima = pila.cima.sig # el cima de la pila es el sig de nodo (el dato anterior  de la pila)
        pila.tamanio -= 1  #al desapilar la pila el tamanio de disminuye 1
        return dato #devuelve le dato almacena en la info de la cima de la pila

    def pila_vacia(pila): #solo comprobar de la cima de la pila es vacia o no
        """Devuelve true si la pila esta vacia"""

        return pila.cima is None # si la cima de la pila devulve el true sino no devuelve nada

    def en_cima(pila): #ver el dato que esta situado en la cima de la pila
        """Devulve el valor almacenado en la cima de la pila"""
        if pila.cima is not None: # si la cima de la pila no es vacia muestra la cima de la pila
            return pila.cima.info # devuelve el info de la cima de la pila
        else:
            return None # si es vacia devuelve vacia

    def tamanio(pila):
        return pila.tamanio

    def barrido(pila):
        """Muestra e contenidod de una pila sin perder datos"""
        paux = Pila() # crea una nueva pila paux= pila auxiliar

        while(not Pila.pila_vacia(pila)): # mientras la pila no es vacia
            dato = Pila.desapilar(pila) # desapilar 
            print(dato) # mostar el dato
            Pila.apilar(paux , dato) #almacena los datos de en paux una nueva pila temporal

        while (not Pila.pila_vacia(paux)): # mientras no es pila vacia paux
            dato = Pila.desapilar(paux) #desapilar la pila "paux"
            Pila.apilar(pila,dato) # almacenar de nuevo a la pila original

def numero():
    pdatos = Pila() # pila datos la principal
    ppar = Pila() # pila para número pares
    pimpar = Pila() # pila para número impares
    dato = int(input("Ingrese un número - 0 para salir "))
    while (dato!=0): # para salir del procesar el algoritmo
        Pila.apilar(pdatos,dato)
        dato = int(input("Ingrese un número - 0 para salir "))
    while (not Pila.pila_vacia(pdatos)): #ver la pila proncipal esta vacia o no
        dato = Pila.desapilar(pdatos) #desapilar el pdato para despues almacena de otro pila
        if (dato %2 ==0):
            Pila.apilar(ppar,dato) #par apilar el dato en la pila par
        else:
            Pila.apilar(pimpar,dato) #impar apilar el dato en la pila impar
    while (not Pila.pila_vacia(ppar)):
        lista =[]
        dato= Pila.desapilar(ppar)# mostrar los datos almacena en la pila de par o impar
        lista.append(dato)
        print(lista)
    while not Pila.pila_vacia(pimpar):
        lista = []
        dato = Pila.desapilar(pimpar)
        lista.append(dato)
        print(lista)


numero()
