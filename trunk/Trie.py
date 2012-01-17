#!/usr/bin/env python

class TrieNode(object):

  def __init__(self,key,value):
    self.key = key
    self.value = value
    self.children = {}

  def __repr__(self):
    return 'TrieNode(%s)' % (self.key)

  def find(self,key):
    currNode = self
    path = [ ]
    for char in key:
      if char in currNode.children:
        path.append(char)
        currNode = currNode.children[char]
      else:
        return ''.join(path),None
    return ''.join(path),currNode.value

  def findNode(self,key):
    parent,currNode = self,self
    path = [ ]
    for char in key:
      if char in currNode.children:
        path.append(char)
        parent,currNode = currNode,currNode.children[char]
      else:
        return None,None
    return parent,currNode

  def delete(self,key):
    parent,node = self.findNode(key)
    if parent and node:
      del parent.children[node.key]
      return True
    return False

  def insert(self,key,value):
    currNode = self
    for i in xrange(len(key)):
      c = key[i]
      if c in currNode.children:
        currNode = currNode.children[c]
      else:
        currNode.children[c] = TrieNode(c,key[:i+1])
        currNode = currNode.children[c]
    currNode.value = value

class Trie(object):

  def __init__(self):
    self.__root = TrieNode('','')

  def find(self,key):
    return self.__root.find(key)

  def insert(self,key,value):
    return self.__root.insert(key,value)

  def delete(self,key):
    return self.__root.delete(key)

def main():
  trie = Trie()
  phone_numbers = [('anthony','5105793184'),('tracy','2396402509'),
                   ('dad','5102203039'),('mom','5137034805')]
  for name,number in phone_numbers:
    trie.insert(name,number)

  return trie,phone_numbers

if __name__ == '__main__':

  trie,phone_numbers = main()
  for name,number in phone_numbers + [('Ryan','5555555555')]:
    print "%20s|%40s" % (name, str(trie.find(name)))


