class ListNode:

  def __init__(self, data, nextNode):
    self.data = data
    self.nextNode = nextNode
    self.antNode = None

  def getData(self):
    return self.data

  def setData(self, val):
    self.val = val

  def getNextNode(self):
    return self.nextNode

  def setNextNode(self, val):
    self.nextNode = nextNode

  def getAntNode(self):
    return self.antNode

  def setAntNode(self, val):
    self.val = val