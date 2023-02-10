import java.io.*;
import java.util.*;

class Solution {

  /**
  
  
  Approach 1:
  
  arr
  
  Loop from right to left N
    Find the highest element N -> N^2
    
    Flip to put element at positon 0 N -> N^2
    Flip to put element at positon i N -> N^2

  N^2
  
  Return the answer

  RT: O(n^2)
  
  ST: O(1)

  and put the highest element on the right
  
  or lowest element on the the left
  
  K elements
  
  First K 
  
  [1,2,3,4]
  
  [4,3,2,1] K = 4
  
  
  Empty arrray is OK
  Negative numbers is OK
  Test large sample
  
  */
  static int[] pancakeSort(int[] arr) {
    
    //loop backwards
    
    for (int i = arr.length -1; i >= 0; i-- ){
      
      // start max at min value
      int positionOfMax = -1;
      int max = Integer.MIN_VALUE;
      
      //loop from 0 to i to find the the max
      for (int j = 0; j <= i; j++){
        if (arr[j] > max){
          max = arr[j];
          positionOfMax = j;
        }
      }

      //flip the max to pos 0
      flip(arr,positionOfMax);
      //flip pos 0 to index i
      flip(arr, i);
      
    }
    
    return arr;
  }

  public static void main(String[] args) {
    //writing a sample test
    int[] arr = {1,-5,-1000,3,2};
    
    //sort
    arr = pancakeSort(arr);
    
    //print the answer
    System.out.println(Arrays.toString(arr));
  }
  
  static void flip(int[] arr, int k){
    //loop from 0 to k. e.g. 4 will do 0,1,2,3
    for (int i = 0, j = k; i < j; i++, j--){
      int temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;

    }
  }

}

