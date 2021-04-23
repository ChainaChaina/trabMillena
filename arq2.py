from arq1 import ListNode

class DoublyLinkedListIterator:

  def __init__(self, firstNode=None):
    self.firstNode = firstNode # (guarda o endereço/referência/valor do primeiro Node)
    self.lastNode = None # (guarda o endereço/referência/valor do ultimo Node)
    self.iterator = None # (guarda o endereço/referência do Node sob o iterador)
    if firstNode: # se tiver o primeiro nó
      self.size = 1 #(guarda o número de elementos da Lista)
    else:
      self.size = 0 #se não tiver o primeiro nó da lista, a lista está vazia, portanto self.size = 0


  def getSize(self): 
    return self.size


  def get_firstNode(self):
    return self.firstNode


  def get_lastNode(self):
    return self.lastNode


  def get_iterator(self):
    return self.iterator


  def setSize(self, size):
    self.size = size


  def set_firstNode(self, firstNode=None):
    self.firstNode = firstNode


  def set_lastNode(self, lastNode=None):
    self.lastNode = lastNode


  def set_iterator(self, iterator = None):
    self.iterator = iterator


  def addNode(self, data): #add Node depois do it e it fica neste Node
    newNode = ListNode(data, None)
    #self.lastNode = newNode
    if (self.size == 0):
      self.iterator = newNode
      self.lastNode = newNode
      self.firstNode = newNode
    elif self.iterator == self.lastNode:
      self.lastNode.nextNode = newNode.nextNode #o nó inserido se torna agora o último nó
      self.antNode = self.lastNode 
      self.iterator = newNode #coloca o iterator sobre o novo Nó
      self.lastNode = newNode #coloca o lastNode no último nó (o nó inserido)
    else:
      newNode.nextNode = self.iterator.nextNode # novo Noh aponta para o noh seguinte do iterador
      self.iterator.nextNode = newNode # faz o prox do no sob o iterador apontar para o novo no
      self.iterator = newNode  # por o iterador sob o novo no
    self.size += 1     # incrementa o contador e retorna true pois teve sucesso na adicao
    return True


  def insNode(self, data): #insere Node antes do it e it fica neste Node
    newNode = ListNode(data, None)
    if (self.size == 0):
      self.firstNode = newNode
      self.lastNode = newNode
      self.iterator = newNode
    elif self.iterator == self.firstNode:
      newNode = ListNode(data, None)
      newNode.nextNode = self.firstNode #o próximo elemento do Node será o Node que antes era a cabeça da lista (firstNode)
      #tentar: self.newNode.nextNode = self.firstNode
      self.firstNode = newNode #armazena como primeiro nó o endereço do nó inserido
    elif (self.iterator != self.firstNode) and (self.iterator != self.lastNode): #iterator no meio da lista
          currentNode = self.firstNode
          if currentNode.nextNode == self.iterator: #se a proxima posição do nó atual estiver na mesma posição do iterator
            newNode.nextNode = self.iterator #proximo Nó aponta pra posição do iterator
            currentNode.nextNode = newNode
            self.iterator.antNode = newNode
          else: #terá q percorrer a lista
            while currentNode.nextNode != self.iterator:
              currentNode = currentNode.nextNode
            newNode.nextNode = self.iterator #adiciona novo nó antes do iterator
            currentNode.nextNode = newNode #o nextNode do nó atual (currentNode) aponta pro novo nó
          self.iterator.antNode.nextNode = newNode
          self.iterator = newNode
    self.size += 1
    return True

  def elimNode(self): # elimina Node sob it e it avanca p/ prox Node (pra eliminar: isolar o node)
    if self.iterator == self.firstNode: #iterator no primeiro nó
      if self.size == 1:
        self.firstNode = None
        self.lastNode = None
        self.iterator = None
      else:
        self.firstNode.nextNode = self.firstNode #o segundo nó passa a ser o primeiro
        self.iterator.nextNode = None # isola o nó
        self.iterator = self.firstNode
    else: #iterator no meio da lista
      currentNode = self.firstNode #nó atual no primeiro nó
      while (currentNode != self.iterator and currentNode != None): #percorre a lista (enquanto o nó atual não estiver sobre o iterator)
        currentNode = currentNode.nextNode # passa pro próximo nó do nó atual
      if (self.iterator != self.lastNode): # se o iterador não estiver no último nó
        self.iterator.antNode = None #o endereço do nó anterior recebe nada
        self.iterator.nextNode = None  #o endereço do nó seguinte recebe nada
        currentNode.antNode.nextNode = currentNode.next #o próximo nó do nó anterior ao nó atual, é o nó seguinte do nó atual, isolando o nó
        currentNode.nextNode.antNode = currentNode.antNode #o nó anterior do próximo nó do nó atual (o isolado), é o nó anterior ao nó atual 
        self.iterator = currentNode.next #coloca o iterator sobre o nó seguinte do nó eliminado
      else:
        currentNode = self.lastNode
        self.lastNode.antNode = self.lastNode
        self.iterator.antNode = None
        self.iterator = self.lastNode 
    self.size -= 1
    return True




  def first_Node(self): # coloca o iterador sobre o primeiro Node da Lista
    self.iterator = self.firstNode
    return self.iterator
    


  def last_Node(self): # coloca o iterador sobre o útlimo Node da Lista
    self.iterator = self.lastNode
    return True


  def nextNode(self): # avança it uma posição. Se it no ult Node, it=None
    if(self.iterator):
      self.iterator = self.iterator.nextNode
    return self.iterator

  def antNode(self): #coloca it uma posição anterior
    if(self.iterator):
      self.iterator = self.iterator.antNode
    return True



  def posNode(self, position): #poe it em <=1 pos <=size, senao it=None
    if position >= 1 and position <= self.size:
      i = 1
      self.iterator = self.firstNode
      while (i < position):
        if (self.iterator.nextNode != None):
          self.iterator = self.iterator.nextNode
          i += 1


  def undefinedIterator(self):
    if self.iterator == None:
      return True
    else:
      return False


  def printLista(self):
        firstNode = self.first_Node()
        size = self.getSize()
        for i in range(size):
            self.nextNode()
            print(self.firstNode.data)
        print('/n')



