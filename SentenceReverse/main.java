import java.io.*;
import java.util.*;

class Solution {

  
  /**
    
    Appraoch 1
    Array
    
    1 fina  all the words
    
    2 Add all to the words to Arraylist
    
    3 reverse backwards in the ArrayList and add back to the arr
    
    time O(N)
    space O(N)
    
    
    ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ','p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
  
                
    ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
    
    reversed: ['e''c''i''t'....'r''e''p']   

    
    Approach 2


    Reverse all characters
    
    loop for i in all index

       find the first space at index j

       reverse from i to j
       
    return the answer


    time: O(N)
    
    space: O(1)
       
       
    
    Extra Space

  */
  static char[] reverseWords(char[] arr) {
    /*int total = arr.length;
    for (int i =0; i < total/2; i++){
      char temp = arr[i];
      arr[i] = arr[total- i-1];
      arr[total- i-1] = temp;
    }*/

    int total = arr.length;
    
    reverse(arr, 0, total-1);
    
    //System.out.println(new String(arr));
    
    int i = 0;
    
    while (i < total) {
      
      int j = i;
      
      while (j < total && arr[j] != ' '){
        j++;
      }
      reverse(arr,i,j-1);
      i = j +1;

    }
    //System.out.println(new String(arr));
    
    return arr;
  }

  public static void reverse(char[] arr, int start, int end){
    //int total = start + (end - start) /2 ;
    //int last = 
    
    /*int index = 0;

    for (int i =start; i < total ; i++){
      char temp = arr[i];
      arr[i] = arr[end- index];
      arr[end- index] = temp;
      index++;
    }*/
    
    while (start <= end){
      char temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;
      start++;
      end--;
    }
    
  }
  
  public static void main(String[] args) {
    //char[] test = {'p', 'e', 'r', 'f', 'e', 'c', 't', '  ','p', 'r', 'a', 'c', 't', 'i', 'c', 'e' };
    String s = "perfect practice";
    reverseWords(s.toCharArray());
  }

}