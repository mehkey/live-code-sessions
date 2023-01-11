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




import java.io.*;
import java.util.*;

class Solution {

  
  /*
  
    arr = [1, 4, 5, 2, 3, 6], k = 2
    
    n is the number of elemnts int he array
    

    Arroach 1: Sort
    
    Runtime: O(n*log(n))
    
    Space: O(n)
    
    TimSort for sorting ( Insertion, Merge, Quicksort)
    
    
    Approach 2: 
    
    Double Loop : For each pos, go k numbers away to find the min to move to the position
    
    Runtime: O(n * k )
    
    Space: O(1)
    
    
    Approach 3:
    
    Monotonic Queue (X) or the Heap (Priority Queue)
    
    Runtime: O(n * log(k) for adding and removing )
    
    Space: O(k)
    
    
    
    arr = [1, 4, 5, 2, 3, 6], k = 2
  
  
    Start
    [1,4]
    
    Middle
    [middle]
    
    End
    
  */
  static int[] sortKMessedArray(int[] arr, int k) {
    // Start: Populate the first k elements in PQ
    PriorityQueue<Integer> kQueue = new PriorityQueue<Integer>();
    
    //Used in all 3 stages
    int index = 0;
    
    for (;index <= k;index++){
      kQueue.add(arr[index]);
    }

    //System.out.println(Arrays.toString(arr));
    //System.out.println(kQueue);
    
    // Middle: Loop from k to end
      // remove the min value
      // put the min value in position
      // add the new value to the PQ

    //pos 0 to len(arr) - k -1
    for (;index < arr.length;index++){
      int current = kQueue.poll();
      arr[index-k-1] = current;
      kQueue.add(arr[index]);
      //System.out.println(current);
    }
    //System.out.println(Arrays.toString(arr));
    
    //System.out.println(kQueue);
    // End: Add the last elements from the PQ to the result

    for (int i =  arr.length-k-1; i<arr.length; i++){
      arr[i] = kQueue.poll();
    }

    
    //System.out.println(Arrays.toString(arr));
    // return the result
    return arr;
  }
  
  
  
  
  
  
  //////////////
  
  
  static int[] sortKMessedArray(int[] arr, int k) {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    int len =arr.length;
    // initializaion
    for (int i =0; i< Math.min(1+2*k, len); i++){
      pq.offer(arr[i]);
      
    }
    
    
    int j = Math.min(1+2*k, len);
  
    
    for (int i =0; i< len ; i++  ){
        arr[i] = pq.poll();
      
      if (j > len-1) continue;
        pq.offer(arr[j]);
          j++;
     
      
    }
    return arr;
    // your code goes here
  }
  
  

  public static void main(String[] args) {
    int[] arr = {1, 4, 5, 2, 3, 7, 8, 6, 10, 9};
    sortKMessedArray(arr,2);
  }

}}


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