'''

[-8,0,2,5]

arr[0] != 0 BAD

arr[1] != 1 BAD

arr[2] != 2 GOOD

Approach:

Loop through the array

From left to right and find the first elmment where arr[i] == i

return it


runtime: O(N)
spacetime: O(1)


'''

def index_equals_value_search(arr):
  
  for i in range(len(arr)):
    
    if arr[i] == i :
      return i
    
  return -1

#print(index_equals_value_search([-8,0,2,5]))
      
  