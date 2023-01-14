import java.io.*;
import java.util.*;

class Solution {

  
  /*
  
  
  Approach 1:
  
  Two pointer
  
  output array = new int[2];
  
  
  while the two pointers don't reach the end
    
    move the pointer with the smallest start time
    
  
  return []


  slotsA = [[10, 50], [60, 120], [140, 210]]
  
                       p1

  slotsB = [[0, 15], [60, 70]]
  
                      p2
  
  m = size of slot1
  n = size of slot2

  TC: O(m+n)
  SC: O(1)

  */
  static int[] meetingPlanner(int[][] slotsA, int[][] slotsB, int dur) {
    
    // create the output
    
    
    
    int pointer1 = 0;
    
    int pointer2 = 0;
    
    // loop while both pointers are in bound
    while (pointer1 < slotsA.length && pointer2 < slotsB.length) {
      
      // compare the start and end time
      int startTime = Math.max(slotsA[pointer1][0], slotsB[pointer2][0]);
        
      int endTime = Math.min(slotsA[pointer1][1],slotsB[pointer2][1]) ;
      
      int overalapTime = 
        // check the overlap and 0 if negative
        Math.max( 
        //check the end time minus the start time
        endTime - startTime, 0) ;
      

      if (overalapTime >= dur) {
        
        
        //create the output
        int[] output = new int[2];
        output[0] = startTime;
          
        output[1] = startTime + dur;
        
        return output;
      }
      
      //increment the pointers
      if (slotsA[pointer1][1] <= slotsB[pointer2][1]){
        pointer1++;
      }
      else{
        pointer2++;
      }
      
    }
      
    return new int[0];
    
  }

  public static void main(String[] args) {
    int[][] slotsA = {{10, 50}, {60, 120}, {140, 210}};
    int[][] slotsB = {{0, 15}, {60, 70}};

    System.out.println(Arrays.toString(meetingPlanner(slotsA,slotsB,8)));
  }

}