import unittest

def pancake_sort(arr):
  
  '''
  
  [1, 5, 4, 3, 2]
  
  1. Find the largest
  2. Move to the left
  3. Move to the right

  runtime: O(N^2) Fist loop N, second loop N
  
  space: O(1)
  
  
  Edge case; Check array of numbers greater than 0
  
  Use Flip
  K numbers not index
  Off by 1
  
  '''
  
  
  return PackakeSort(arr).sort()
    
    
class PackakeSort:
  
  def __init__(self,arr):
    self.arr = arr

  def sort(self):
    # go from the last index to the first index
    for large_index in range(len(self.arr)-1,-1,-1):

      max_val = float('-inf')
      max_index = 0
      # find the largets number from 0 to large_index

      for index in range(0,large_index+1):

        if self.arr[index] > max_val:
          max_val = self.arr[index] 
          max_index = index
      
      #print(max_index)

      #flip
      self._flip(max_index+1)
      
      
      self._flip(large_index+1)
      

    return self.arr

  def _flip(self, k ):

    # val 1 2 3
    # pos 0 1 2

    for i in range( (k//2) ):
      self.arr[i], self.arr[k-i-1] = self.arr[k-i-1] , self.arr[i]

class TestPackakeSort(unittest.TestCase):

  def test_flip(self):

    p = PackakeSort([1, 2,3,4,5])
    
    p._flip(5)
    
    self.assertEqual(p.arr, [5,4,3,2,1]  )

  def test_sort(self):
    
    self.assertEqual(PackakeSort([1, 5, 4, 3, 2]).sort(),[1, 2, 3, 4, 5]  )
    
  def test_sort_2(self):
    
    self.assertEqual(PackakeSort([1, 5,2, 4, 3, 6,7]).sort(),[1, 2, 3, 4, 5,6,7]  )
    
#unittest.main(verbosity=2)