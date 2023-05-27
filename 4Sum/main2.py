import unittest

def find_array_quadruplet(arr, s):
  '''

  4 numbers that add to 20

  Approach1 : 4 Loops 
  O(N^4)
  
  Apporach2: Sort + 3 Loop + Binarysearch
  
  O(nlogn + N^3*logN)
  
  Approach3: Sort + 2 Loops + Double Pointer
  
  runtime:O(NlogN + N^2 * N ) = O(N^3)
  
  spacetime:O(1)
  
  
  Approach 4: Kuplet: Sort + K-2 Loops + Double Pointer
  
  Recursive K for >2
  
  Double Pointer for K == 2
  
  O(N^K-1)

  '''

  # new kuplet of size 4 
  kuplet = Kuplet(4)

  #return the numbers if found
  return kuplet.find_Kuplet(arr, s)

class Kuplet:
  def __init__(self, K):
    self.K = K

  def find_Kuplet(self, arr, s):

    # Sort 
    arr.sort()

    return self.find_Kuplet_recursive(arr, self.K, 0, s)


  def find_Kuplet_recursive(self, arr, current_K, start, s):
    if s < 0:
      return False
    # find Kuplet recursively
    if current_K > 2:
      # 2 7 4 0 9
      for i in range(start,len(arr)-current_K+1):
        ans = self.find_Kuplet_recursive(arr,current_K-1,i+1, s - arr[i])
        if ans:
          return [arr[i]] + ans

      return False

    #double pointer
    elif current_K == 2:
      left = start
      right = len(arr)-1
      while left < right:
        target = arr[left] + arr[right]
        if target == s:
          #self.result.extend([arr[left],arr[right]])

          return [arr[left],arr[right]]
        elif target > s:
          right -= 1
        elif target < s:
          left +=1

      #no match found
      return False
    else:
      raise Exception("K should be greater than 1")



print(find_array_quadruplet([2, 7, 4, 0, 9, 5, 1, 3], 20))

'''
neetcode Youtube

neetcode.io/practice

Blind 75 (major topics)

14 patterns 

Pramp

CLRS book - reference

Code and system design


'''