from typing import List
# from queue import Queue

# def bucket_sort(lst: List[int], K: int) -> list:
  # buckets = [[] for _ in range(K)]

  # shift = min(lst)
  # max_value = max(lst) - shift
  # bucket_size = max(1, max_value // K)

  # for i, elem in enumerate(lst):
  #   index = (elem - shift) // bucket_size

  #   if index == K:
  #     buckets[K - 1].append(elem)
  #   else:
  #     buckets[index].append(elem)
  
  # for bucket in buckets:
  #   bucket.sort()

  # sorted_array = []
  # for bucket in buckets:
  #   sorted_array.extend(bucket)
  
  # for i in range(len(sorted_array)):
  #   lst[i] = sorted_array[i]
  
  # return lst 

# def smallest_trimmed_numbers(nums, queries):
  # ans = []
  # for k, t in queries:
  #   arr = []
  #   for i, x in enumerate(nums):
  #     arr.append((int(x[-t:]), i))
  #   arr.sort()
  #   ans.append(arr[k - 1][1])
  # return ans

# print(smallest_trimmed_numbers(["102","473","251","814"], [[1,1],[2,3],[4,2],[1,2]]))
# print(bucket_sort([50, -10, 20, 40, 50, 100, 30, 90], 5))


class Node:
  def __init__(self, value, parent):
    self.value = value
    self.parent = parent
    self.left = None
    self.right = None  

  def __repr__(self):
    from pprint import pformat

    if self.left is None and self.right is None:
      return str(self.value)
  
    return pformat({f"{self.value}": (self.left, self.right)}, indent=1)

class BinarySearchTree:
  def __init__(self, root=None):
    self.root = root

  def empty(self):
    return self.root is None
    
  def search(self, value):
    if self.empty():
      raise IndexError("Warning: Tree is empty!")
    else:
      node = self.root
      while node is not None and node.value is not value:
        node = node.left if value < node.value else node.right
      return node

  def insert(self, *values):
    for value in values:
      self._insert(value)
    return self
  

  def r_delete(self, root: Node, key: int):
    if not root: return None

    if root.value == key:
      # 4 cases
      if not root.left and not root.right: return None
      if not root.right and root.left: return root.left 
      if not root.left and root.right: return root.right
      pnt = root.right
      while pnt.left: pnt = pnt.left
      root.value = pnt.value  
      root.right = self.r_delete(root.right, root.value)
        
    elif key < root.value:
      root.left = self.r_delete(root.left, key)
    else:
      root.right = self.r_delete(root.right, key)
    
    return root

  def remove(self, value):
    node = self.search(value)

    if node is not None:
      if node.left is None and node.right is None:
        self._reassign_nodes(node, None)
      elif node.left is None: # has right children
        self._reassign_nodes(node, node.right)
      elif node.right is None:
        self._reassign_nodes(node, node.left)
      else:
        tmp_node = self.get_max(node.left) # get max value from left
        self.remove(tmp_node.value)
        node.value = tmp_node.value

  def get_max(self, node=None):
    if node is None:
      node = self.root
    if not self.empty():
      while node.right is not None:
        node = node.right
    return node 

  def get_min(self, node=None):
    if node is None:
      node = self.root
    if not self.empty():
      while node.left:
        node = node.left
    return node 
      
  def _reassign_nodes(self, node, new_children):
    if new_children is not None:
      new_children.parent = node.parent
    if node.parent is not None:
      if node == node.parent.right:
        node.parent.right = new_children
      else:
        node.parent.left = new_children
    else:
        self.root = new_children
    
    
  def _insert(self, value):
    """
    Insert a new node into BST with value 
    """
    new_node = Node(value, None)
    if self.empty():
      self.root = new_node
    else:
      parent_node = self.root
      while True:
        if value < parent_node.value: #Go to the left
          if parent_node.left is None:
            parent_node.left = new_node
            break
          else:
            parent_node = parent_node.left
        else: 
          if value > parent_node.value: # We go right
            if parent_node.right is None:
              parent_node.right = new_node
              break
            else:
              parent_node = parent_node.right
        new_node.parent = parent_node 

  def inorder_traversal(self, node: Node):
    if node:
      self.inorder_traversal(node.left)
      print(node.value)
      self.inorder_traversal(node.right)


def binary_search_tree():
  tree = BinarySearchTree()
  """
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
  """
  
  tree.insert(8, 3, 6, 1, 10, 14, 13, 4, 7)

  tree.r_delete(tree.root, 1)

  tree.inorder_traversal(tree.root)

# binary_search_tree()

class LLNode:
  def __init__(self, value):
    self.value = value
    self.next = None

def reverse_list(node: LLNode) -> LLNode:
  if node is None or node.next is None:
    return node

  p = reverse_list(node.next)
  node.next.next = node
  node.next = None
  return p 

def print_list(head: LLNode) -> LLNode:
  temp = head
  while temp:
    print(temp.value, end=" ")
    temp = temp.next

  
n1 = LLNode(1)
n2 = LLNode(2)
n3 = LLNode(3)
n4 = LLNode(4)
n5 = LLNode(5)

n1.next = n2
n2.next = n3
n3.next = n4 
n4.next = n5


class TreeNode:
  def __init__(self, value) -> None:
    self.value = value
    self.left = None
    self.right = None



def insert(node: TreeNode, value:int) -> None:
    if not node:
      return TreeNode(value)
      
    if value <= node.value:
      node.left = insert(node.left, value)
    else: 
      node.right = insert(node.right, value)
    
    return node

def max_tree(node) -> TreeNode:
  if node.right is None:
    return node 
  return max_tree(node.right) 

def print_tree(node: TreeNode):
  if not node:
    return 
  
  print_tree(node.left)
  print(node.value)
  print_tree(node.right) 

seq = [1, 5, 9, 2, 4, 10, 6, 3, 8]

#             1
#               \
#                9 
#               / \
#              2   10
#               \    
#                4   
#               /  \
#              3    6 
#                    \
#                     8
# root = None
# for value in seq:
#   root = insert(root, value)
  
# print(max_tree(root).value)

import os



def find_directories(path: str):
  for file in os.listdir(path):
    f = os.path.join(path, file)
    
    if os.path.isfile(f):
      print(f)
    
    if os.path.isdir(f): 
      find_directories(f) 

find_directories("../")