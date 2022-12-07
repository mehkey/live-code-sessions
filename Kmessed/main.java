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
      arr[i] = smallest;
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