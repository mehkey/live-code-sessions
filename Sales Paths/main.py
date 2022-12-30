def get_cheapest_cost(rootNode):
  if rootNode == None :
    return 0
  
  if len(rootNode.children) == 0:
    return 0

  minimum = float('inf')
  
  for node in rootNode.children :
    
    val = get_cheapest_cost(node)
    #print(val)
    minimum = min( minimum, val + node.cost )
  
  #print(minimum)
  
  return minimum
  

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
 

root = Node(1)
root.children.append(Node(2))
#root.children.append(Node(3))
root.children.append(Node(4))
root.children[0].children.append(Node(5))
root.children[0].children[0].children.append(Node(10))
root.children[0].children.append(Node(6))
root.children[0].children[1].children.append(Node(11))
root.children[0].children[1].children.append(Node(12))
root.children[0].children[1].children.append(Node(13))
root.children[1].children.append(Node(7))
root.children[1].children.append(Node(8))
root.children[1].children.append(Node(10))


'''
      
      1
   /  |  \
  /   |   \
 2    3    4
/ \      / | \
/   \    7  8  9
5     6    
/    / | \ 
10   11 12 13
'''
print(get_cheapest_cost(root) + root.cost)



'''
package main

/*

BFS or DFS

start at the root


Approach DFS
  Recurively or with a Stack
  Count the Children
  return the min children
  
  DFS
  
Approach BFS
  Use a queue
  Add the root to the queue
  pop from the queue and add the children to the queue
  (children and the minimum current path)
  
  If you reach a leaf, then you store the minimum path



*/



type Node struct {
  cost int
  parent *Node
  children []*Node
}

func GetCheapestCost(rootNode *Node) int {
  if rootNode == nil {
    return 0
  }
  
  minimum := MaxInt
  
  for node := range children {
    
    val := GetCheapestCost(node)
    
    minimum = min( minimum, val + node.cost )
    
  }
  
  return minimum
  
}

func main() {
  //Node
}

func min(a int, b int) int {
  if a <= b {
    return a
  }
  return b
}


'''