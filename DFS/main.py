
from collections import deque

class Node:
    """
    Node class containing value, left and right nodes
    """
    val : int
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None


def bfs(arr):
    """
    Regular BFS
    """
    
    # return early no arr
    if not arr:
        return None
    
    cur = 0
    
    #initalize the queue
    q = deque()
    
    top = Node()
    
    top.val = arr[0]
    
    q.append(top)
    
    cur += 1
    
    #while the queue is not empty and there are more nodes to add
    while q and cur < len(arr)  :
        
        node = q.popleft()

        #create the left node
        if cur < len(arr) and arr[cur] != -1:
            left = Node()
            left.val = arr[cur]
            node.left = left
            q.append(left)
        
        cur += 1
        
        #create the right node
        if cur < len(arr) and arr[cur] != -1:
            right = Node()
            right.val = arr[cur]
            node.right = right
            q.append(right)
        
        cur += 1
        
    return top


def sum_dfs(node):
    """
    DFS to create the SUM
    
    """
    if not node:
        return 0
    
    total = node.val
    
    if node.left:
        total += sum_dfs(node.left)
        
    if node.right:
        total += sum_dfs(node.right)
    
    return total

def solution(arr):

    node = bfs(arr)
    
    if not node:
        return ""
    
    left_value = sum_dfs(node.left)
    right_value =  sum_dfs(node.right)

    if left_value >right_value:
        return "Left"
    elif left_value < right_value:
        return "Right"
    else:
        return ""


