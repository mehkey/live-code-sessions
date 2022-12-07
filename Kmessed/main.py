'''

Aproach 1

sort 

O(N log N)

O(1)


Approach 2

Loop throught the array

  At each position we loop K away to find the minimum, put in the right place
  

O(N * K) K <= 20.  O(N)

O(1) swap in place


Approach 3

time O(N * log(K))
space O(K)

Priority Queue 

Loop through elements


Start put the K elements in the PQ


Loop 
  remove 1 element (smallest) and put it in the right spot
  add 1 element to the PQ



'''

import heapq

def sort_k_messed_array(arr, k):

  pq = []

  for i in range(k+1):
    heapq.heappush(pq, arr[i])

  for i in range(0,len(arr)-k-1):

    smallest =  heapq.heappop(pq)

    arr[i] = smallest

    heapq.heappush(pq, arr[i+k+1])

  for i in range(len(arr)-k-1,len(arr)):
    smallest =  heapq.heappop(pq)
    arr[i] = smallest

  return arr

print(sort_k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))


Google Inteview Rubric
https://blog.tryexponent.com/google-coding-interview-rubric/

  4 Points
  Algorithm
  4 Points 
  Coding
  4 Problem sol
  4 Points 
  Communication

