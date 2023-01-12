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

from collections import Counter

def compare(x):
  return (abs(x),x)


def absSort(arr):
  # Quicksort O(1) space
  # Heapsort O(1) space
  # return sorted(arr, key = lambda x: (abs(x), x))
  #return sorted(arr, key=compare)

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

print(absSort([2, -7, -2, -2, 0]))


'''
def lcs(i, j, dic={}):
    if (i,j) in dic:
        return dic[(i,j)]
    elif i == len(text1) or j == len(text2):
        return 0
    elif text1[i] == text2[j]:
        dic[(i,j)] = 1 + lcs(i+1, j+1) 
    else:
        dic[(i,j)] = max(lcs(i+1, j), lcs(i, j+1))
    return dic[(i,j)]
return lcs(0, 0)

m len(word1)
n len(word2)

O(m*n)
O(m*n)

5. abcde. 6 defghi

6 * 5 * 4 * 3 * 2

n! / (n-m) !

6 * 6 * 6 = n ^ m

CLRS

Algorithm DS Cheatsheet (Major DS)

neetcode.io/practice

Blind 75
-> Contest, Daily, Company (premium)

'''



# https://linkedin.com/in/primetimetran
meki.chk@gmail.com


lloy




import collections
"""
approach 1:
time complexity : O(N^2)
space : O(1)
approach 2:
time complexity: O(NlogN)
space : O(N)

Inplace sort(Quicksort, Heapsort)
O(1) space


"""
#from collections import OrderedDict
#from sortedcontainers import SortedDict

def absSort(arr):
  
  return sorted(arr, key=lambda x : (abs(x),x) )
  '''
  arrmappos=collections.defaultdict(int)
  arrmapneg=collections.defaultdict(int)
  
  #count=collections.Counter(arr)
  #print(count)
  for i in range(len(arr)):
    
    if arr[i] >= 0:
      arrmappos[abs(arr[i])] += 1
    else:
      arrmapneg[abs(arr[i])] += 1

  #print(arrmappos)
  #print(arrmapneg)
  i=0
  for x in sorted( list(set(arrmapneg.keys()+arrmappos.keys()))):
    print(x)
    for j in range(arrmapneg[x]):
      arr[i]=-x
      i+=1
    
    for j in range(arrmappos[x]): 
      arr[i]=x
      i+=1

  return arr
  '''


print(absSort([2, -7, -2, -2, 0]))


import collections
"""
approach 1:
time complexity : O(N^2)
space : O(1)
approach 2:
time complexity: O(NlogN)
space : O(N)

Inplace sort(Quicksort, Heapsort)
O(1) space


"""
#from collections import OrderedDict
#from sortedcontainers import SortedDict

def absSort(arr):
  
  return sorted(arr, key=lambda x : (abs(x),x) )
  '''
  arrmappos=collections.defaultdict(int)
  arrmapneg=collections.defaultdict(int)
  
  #count=collections.Counter(arr)
  #print(count)
  for i in range(len(arr)):
    
    if arr[i] >= 0:
      arrmappos[abs(arr[i])] += 1
    else:
      arrmapneg[abs(arr[i])] += 1

  #print(arrmappos)
  #print(arrmapneg)
  i=0
  for x in sorted( list(set(arrmapneg.keys()+arrmappos.keys()))):
    print(x)
    for j in range(arrmapneg[x]):
      arr[i]=-x
      i+=1
    
    for j in range(arrmappos[x]): 
      arr[i]=x
      i+=1

  return arr
  '''


print(absSort([2, -7, -2, -2, 0]))