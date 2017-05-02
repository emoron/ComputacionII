# coding: utf-8
#!/usr/bin/env python

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila esta vacia levanta excepción"""
        try:
         return self.items.pop()
        except IndexError:
            raise ValueError("LA PILA ESTA VACIA")
     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
