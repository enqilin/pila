# pila

Una pila es una colección de elementos que se agregan y se eliminan siguiendo el principio de último en entrar-primero en salir (LIFO, Last In-First Out), es decir, el último elemento insertado en la pila es el primero en ser eliminado. Un elemento puede ser agregado en cualquier momento a una pila, pero solo se puede acceder o eliminar el elemento que esté en la cima o tope de la misma

existen dos actividades o eventos que administran los elementos de una pila, esto también implica que en realidad el valor del dato almacenado no influye en el funcionamiento de la estructura. Estos eventos son: apilar cuando se agrega un nuevo elemento en la cima y desapilar cuando se saca el elemento que está en la cima.

Esto implica que solo se puede acceder al elemento que está en la cima de la pila. La forma de acce- der a los demás elementos de la colección es desapilar cada uno de estos, de a uno a la vez.

una pila puede definirse de la siguiente manera: si consideramos su estructura y funcio- namiento, es una estructura lineal dinámica de datos que no están ordenados y cuyas actividades de inserción y eliminación se realizan a través de un índice llamado cima o tope. Es importante remarcar que el orden de complejidad de las operaciones sobre la pila son de tiempo constante O(1) dado que solo se pueden agregar y quitar elementos desde la parte superior de la misma, por lo que no importa la cantidad de elementos que tenga.

1.	apilar(pila, elemento). Agrega el elemento sobre la cima de la pila;

2.	desapilar(pila). Elimina y devuelve el elemento almacenado en la cima de la pila;

3.	pila_vacia(pila). Devuelve verdadero (true) si la pila no contiene elementos;

4.	cima(pila). Devuelve el valor del elemento que está almacenado en la cima de la pila pero sin eliminarlo;

5.	tamaño(pila). Devuelve la cantidad de elementos en la pila.
definimos nodo y pila:
clase nodoPila

```bash
class nodoPila(obejct):
    info , sig = None, None
```

clase Pila

```bash

```

definir las funciones mencionadas previamente.

```bash
#continuación de la clse de la pila
    def apilar(pila, dato): #self=pila de estadica a dinamino
        """Apila el dato sobre la cima  de la pila"""
        nodo= nodoPila() #crear nodo
        nodo.info = dato # dato almacenado en la info del nodo
        nodo.sig = pila.cima #sig de nodo es la cima de la pila
        nodo.cima = nodoPila()# que a su vez es un nuevo nodo con  info y sig
        pila.tamanio += 1 # el tamanio de la pila se aumenta 1
        

    def desapilar(pila): #solo es necesario la pila porque el dato es pila.cima.info
        """ Desapilar el elemento en la cima de la pila y lo devuelve"""
        x= pila.cima.info #el dato almacenado en la info de nodo de la pila
        pila.cima = pila.cima.sig # el cima de la pila es el sig de nodo (el dato anterior  de la pila)
        pila.tamanio -= 1  #al desapilar la pila el tamanio de disminuye 1
        return x #devuelve le dato almacena en la info de la cima de la pila

    def pila_vacia(pila): #solo comprobar de la cima de la pila es vacia o no
        """Devuelve true si la pila esta vacia"""
        return pila.cima is None # si la cima de la pila devulve el true sino no devuelve nada

    def en_cima(pila): #ver el dato que esta situado en la cima de la pila
        """Devulve el valor almacenado en la cima de la pila"""
        if pila.cima is not None: # si la cima de la pila no es vacia muestra la cima de la pila
            return pila.cima.info # devuelve el info de la cima de la pila
        else:
            return None# si es vacia devuelve vacia
```

barrido de la pila

```bash
def barrido(pila):
        """Muestra e contenidod de una pila sin perder datos"""

        paux = Pila() # crea una nueva pila paux= pila auxiliar
        while(not pila_vacia(pila)): # mientras la pila no es vacia
            dato = desapilar(pila) # desapilar 
            print(dato) # mostar el dato
            apilar(paux , dato) #almacena los datos de en paux una nueva pila temporal

        while (not pila_vacia(paux)): # mientras no es pila vacia paux
            dato = desapilar(paux) #desapilar la pila "paux"
            apilar(pila,dato) # almacenar de nuevo a la pila original

            
```



"""
### EJERMPLOS DE PILA MULTIPLE ###
En este caso se tiene una pila de números enteros 
y se desea dividirla en dos pilas, 
una con los números pares y otra con los impares:
"""
```bash
pdatos = Pila() # pila datos la principal
ppar = Pila() # pila para número pares
pimpar = Pila() # pila para número impares
dato = int(input("Ingrese un número - 0 para salir "))

while (dato!=0): # para salir del procesar el algoritmo
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
    print(dato)

```
explica de las acciones realizadas para la resolucion del ejercicio:

Se crean las variables necesarias de tipo pila. Luego, después de cargar los datos en la pila, se procede a eliminar el elemento en la cima de la pila y se determina si el elemento desapilado es par o impar para apilarlo en la pila correspondiente (par o impar). Y se repite el mismo procedimiento para cada elemento hasta que la pila quede vacía para finalmente mostrar el contenido de ambas pilas.
