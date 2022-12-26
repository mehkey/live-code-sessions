import java.io.*;
import java.util.*;

class Solution {

	static int[] absSort(int[] arr) {
		// your code goes here
    
    Integer[] arrv = Arrays.stream(arr).boxed().toArray(Integer[]::new);
    
    Arrays.sort(arrv, (a,b) ->  {
      int res = Math.abs(a) -  Math.abs(b);
      if (res != 0){
        return res;
      }
      return a - b;
    } );
    
    int[] intArray =  Arrays.stream(arrv).mapToInt(Integer::intValue).toArray();
    
    //System.out.println(intArray);
    return intArray;
    
    //--> [-2 -2 0 -7]
    
	}

	public static void main(String[] args) {
    int[] input = {2, -7, -2, -2, 0};
	  int[] result = absSort(input);
    System.out.println(Arrays.toString(result));
	}
}
