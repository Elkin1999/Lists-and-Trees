# -*- coding: cp1252 -*-
#Autor: Elkin Camilo Osorio Martinez 
#Programa: Lists and Trees.py
#Descripción: Este programa crea una lista de nodos, en la cual cada nodo solo conoce al siguente nodo
#Fecha: 19/06/2017 3:37 pm
class Nodo:
    """ Esta clase representa cada uno de los Nodos de la lista
   """
   
    # Atributos
    valor = None # el valor del nodo
    siguiente = None # se dirige al siguiente nodo
    anterior = None # se dirige al nodo anterior
 
    # Constructor
    def __init__(self, valor, siguiente, anterior):
        self.valor = valor
        self.siguiente = siguiente
        self.anterior = anterior
 
 
class ListaSimple:
    """ Se crea una clase de una lista simple, en donde los nodos
    solo conocen al nodo siguiente
       
   """
   
    # Atributos
    raiz = None # el nodo raiz de la lista
    ultimo = None #el nodo final de la lista
    anterior = None 
   
    def getVacio(self):
        if self.raiz==None:
            return True

    # Constructor
    def __init__(self, nodo):
        self.raiz = nodo
        self.ultimo = nodo
 
    # Metodos
    def insertar(self, valor):
        """ Inserta un nodo nuevo con valor en la lista
       """
        nuevo = Nodo(valor, None, None)
        # Caso 1= que la lista este vacia 
        if self.raiz == None:
            self.raiz = nuevo
            self.siguiente = nuevo
            self.anterior = nuevo
        # Caso 2: que el nuevo nodo vaya antes del nodo raiz
        elif nuevo.valor < self.raiz.valor:
            nuevo.siguiente = self.raiz
            nuevo.siguiente.anterior=nuevo
            self.raiz = nuevo
            self.anterior= nuevo
        else:
            insertado = False
            actual = self.raiz
            siguiente=actual.siguiente
            anterior = actual;
            # Caso 3: que el nuevo nodo vaya entre los dos nodos existentes
            while actual != None:
                if nuevo.valor < actual.valor:
                    anterior.siguiente = nuevo
                    siguiente.anterior= nuevo
                    nuevo.siguiente = siguiente
                    insertado = True
                    break
                anterior = actual
                actual = actual.siguiente
            # Caso 4: que el nuevo nodo vaya al final
            if not insertado:
                nuevo.anterior=anterior
                anterior.siguiente = nuevo;
 
    def borrarPrimero(self):
        """ Borra un nodo existente con valor de la lista
       """
        #si la lista esta vacia, no hay nada para eliminar
        if self.getVacio()==True:
            print ("No hay nodos en esta lista")
            #Cuando solo hay un nodo creado en la lista
        elif self.raiz == self.siguiente:
            self.raiz=None
            self.siguiente=None
        else:
            temp=self.raiz
            self.raiz=self.raiz.siguiente
            temp=None
            print ("Se eliminó el primer y unico")
        pass
 
    def imprimir(self):
        """ Imprime todo los elementos de la lista
       """
        nodo = self.raiz
        while nodo != None:
            print(nodo.valor)
            nodo = nodo.siguiente
 
 
# Programa Principal
 
ls = ListaSimple(None)
ls.insertar("juan")
ls.insertar("teresa")
ls.insertar("maria")
ls.insertar("lucia")
ls.insertar("andres")
ls.insertar("sara")
ls.insertar("julio")
ls.insertar("diana")
ls.imprimir()
