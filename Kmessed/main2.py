import heapq
import unittest

def sort_k_messed_array(arr, k):
  '''
  
  Messed up sorted array:
  
  [1, 4, 5, 2, 3, 7, 8, 6, 10, 9] k=2
  
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
  
  Approach 1: Brute Force
  
  Regular Sort: T-O(n log n) 
  
  S-O(1)
  
  Quicksort, Merge(O(n) space)
  
  (Uniform bucketsort, range number was Couting sort Radix Sort... )
  O(N + B or N + K)
  
  
  Approach 2: Take each number and move it K numbers away (
  Bubble, Insert, Seleciton O(n^2)
  )
  
  O(N * K)
  
  
  Approach 3: Use a datastrucure to keep the smallest number
  
  Heap sort
  
  Heap keep the smallest number to the left or top of the heap
  
  Heap has size K
  
  
  1. Start putting the first K elements int the heap
  
  2. For every element from k+1 to end
     
     put the min of the heap at position i-k 
     
     add element i to the heap

  
  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9] K = 2
  
  heap = [5,6,7]
  
  [1,2,3,4,0,0,0,0,0,0,0,0]
  
  T-O(N log K) 
  S-O(K) 
  
  N times- remove min a heap o(logK), add to the heap O(logK)
  
  '''
  
  return KMessedUpArray(k).sort_k_messed_array(arr)

class KMessedUpArray:
  
  def __init__(self,k):
    self.k = k
  
  def sort_k_messed_array(self,arr):
    
    if not arr:
      return arr

    #empty heap
    heap = []

    #1. Start putting the first K elements int the heap
    # e.g K = 2, we want to add 3 elements
    for index in range(self.k+1):
      
      heapq.heappush(heap, arr[index])
    
    # 2. For every element from k+1 to end
    
    for index in range(self.k+1, len(arr)):
      
      #put the min of the heap at position i-k+1 
      # go k+1 back and put the min value
      arr[index-(self.k+1)] = heap[0]
      
      #pop the min value
      heapq.heappop(heap)
      
      #add the next element to the heap
      # e.g. index = 3, add 2
      heapq.heappush(heap, arr[index])

    index = len(arr) - len(heap)

    #put the rest int he heap
    while heap:
      arr[index] = heapq.heappop(heap)
      index+=1
    
    return arr

class TestKMessedUpArray(unittest.TestCase):
  
  def test_example_k_2(self):
    #Arrange
    inp =[1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    
    #Act
    result = KMessedUpArray(k).sort_k_messed_array(inp)
    
    #Assert
    print(result)
    self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

  def test_example_k_1(self):
    #Arrange
    inp =[1, 3, 2, 5, 4]
    k = 1
    
    #Act
    result = KMessedUpArray(k).sort_k_messed_array(inp)
    
    #Assert
    print(result)
    self.assertEqual(result, [1, 2, 3, 4, 5])
  
  def test_example_k_0(self):
    #Arrange
    inp =[1, 3, 2, 5, 4]
    k = 0
    
    #Act
    result = KMessedUpArray(k).sort_k_messed_array(inp)
    
    #Assert
    print(result)
    self.assertEqual(result, [1, 3,2,5,4])

  def test_example_Empty(self):
    #Arrange
    inp =[]
    k = 1
    
    #Act
    result = KMessedUpArray(k).sort_k_messed_array(inp)
    
    #Assert
    print(result)
    self.assertEqual(result, [])

iterable = ['a','b','c']#{'a':1, 'b':2}
print({key: key for key in iterable})
#unittest.main(verbosity=2)