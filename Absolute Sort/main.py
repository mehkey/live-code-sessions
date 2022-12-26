'''
1. Constraints
We receive 1 input and should return 1 result arr/list

Assume we have valid input, any integer


2. Diagram

hm = {
  0: 1,
  -2: 2,
  2: 2,
  7: 0
}


1) [2, -7, -2, -2, 0]

2) [0, 2, 2, 2, 7]

2.5) Use Counter to identify the numbers which are negative and their counts.

3) [0, -2, -2, 2, -7]

3. Pseudocode

4. Code

time:
o(nlogn) where n is the input arr size

space:
o(n) where n the size of the list. We add one item to our output for every item in our input n


'''


'''




'''

from collections import Counter

def compare(x):
  return (abs(x),x)

def absSort(arr):
  # Quicksort O(1) space
  # Heapsort O(1) space
  #return sorted(arr, key = lambda x: (abs(x), x))
  return sorted(arr, key=compare)
  

  '''
  counts = Counter(arr) # o(n)
  res = [abs(n) for n in arr]
  res.sort() # o(nlogn)
  output = []
  for n in res: # o(n)
    if -n in counts and counts[-n] > 0: # o(1)
      output.append(-n) # o(1)
      counts[-n] -=1 # o(1)
    else: 
      output.append(n)
  return output
  '''

print(absSort([2, -7, -2, -2, 0])) # [0, -2, -2, 2, -7]