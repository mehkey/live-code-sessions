'''

K-Messed Array Sort
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer k

0 ≤ k ≤ 20
[output] array.integer


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


import java.io.*;
import java.util.*;

class Solution {

  static int[] sortKMessedArray(int[] arr, int k) {

    PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
  
    for (int i = 0; i< k+1; i++){
      pq.add(arr[i]);
    }

  
    for  (int i = 0; i< arr.length-k-1; i++){ 
    
      int smallest =  pq.remove();
    
      arr[i] = smallest;
    
      pq.add( arr[i+k+1] );
    }
    
    for (int i = arr.length-k-1; i <  arr.length; i++) { 
      int smallest =  pq.remove();
      arr[i] = smallest;s
    }
    return arr;
  }

  public static void main(String[] args) {
    
  }

}


/***
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
***/
