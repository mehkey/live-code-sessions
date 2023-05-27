'''

O(N^4)

4 Loops


Binary search

N log N  + search

TC: O (N^3)
SC: O (N)

O (N^3)



O(N^3 * log(N) + N log N)





'''

def binary_search(arr, left,right,s):
  
  
  while left < right:
    
    total = arr[left] + arr[right]
    
    if total == s:
      return [arr[left],arr[right]]
    
    if total > s:
      right -= 1
    else:
      left += 1


  return -1

def find_array_quadruplet(arr, s):
  
  arr.sort()

  se = set(arr)
  
  for i in range(0,len(arr)-3):
    
    for j in range(i+1,len(arr)-2):

      for k in range(j+1,len(arr)-1):
        
        total = arr[i] + arr[j] 
        
        while left < right:
    
          total = arr[left] + arr[right]
          
          if total == s:
            return [arr[i], arr[j], arr[left],arr[right]]
          
          if total > s:
            right -= 1
          else:
            left += 1


          
    
  return []

'''
def twoSumHelper(arr, start, target):
  for i: [start:arr.length - 1]
    if set.contains(target - arr[i]):
      return [arr[i], target - arr[i]]
  return []
'''

'''
def find_array_quadruplet_up_to_k(arr, s, k):
  
  arr.sort()
  #sort by ascending
  
  current = []
  
  return find_array_quadruplet_up_to_k(arr,s,k, current,k  )

def find_array_quadruplet_up_to_k(arr, s, k, current, start):
  
  if k == 1:
    res =  binary_search(arr, k+1, len(arr)-1, s - total )
        
    if res != -1:

      return current
  
  for i in range(start,len(arr)-k+1):
    
    current.append(arr[start])
    
    res = find_array_quadruplet_up_to_k(arr,s,k-1, current, start+1):
    
    if len(res) > 0;
      return res
  
  return []
'''

#print(find_array_quadruplet([2, 7, 4, 0, 9, 5, 1, 3],20))

#print(binary_search([1,2,3,4,5,6],0,5,3))


    '''

    mid = left + ((right-left) // 2)
    
    if arr[mid] == s:
      return mid

    if arr[mid] > s:
      left = mid + 1
    else:
      right = mid - 1

    '''