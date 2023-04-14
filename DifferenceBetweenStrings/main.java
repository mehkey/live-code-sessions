import java.io.*;
import java.util.*;

class Solution {

  
  /*

  2 linear, memo (recursive)

  recursion
  base case
  start case
  Input/Ouput

  Output = minimum size
  Input = Two Index

  */
  static int dp(int sourceIndex, int targetIndex, Map<String,Integer> memo, String source, String target){

    if (sourceIndex == source.length()){
      return target.length() - targetIndex;
    } 
    
    if (targetIndex == target.length()){
      return source.length() - sourceIndex;
    }

    if (memo.containsKey(sourceIndex + "-" + targetIndex)){
      return memo.get(sourceIndex + "-" + targetIndex);
    }

    if (source.charAt(sourceIndex) == target.charAt(targetIndex) ){
      int result = 1+ dp(sourceIndex+1, targetIndex+1,memo, source,target);
      memo.put(sourceIndex + "-" + targetIndex , result);
      return result;
    }

    int result = 1 + Math.min( dp(sourceIndex+1, targetIndex, memo, source,target), dp(sourceIndex, targetIndex + 1, memo, source,target) );

    memo.put(sourceIndex + "-" + targetIndex , result);

    return result;
  }
  
	static String[] diffBetweenTwoStrings(String source, String target) {
		// your code goes here
    // source = "ABCDEFG"
    // target = "ABDFFGH"
    // result = ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]
    
    // If there are multiple answers, use the answer that favors removing from the source first.
    // Uses the least edits possible. the least number of + and -
    
     //-A-B-C-D-E-F-G  +A+B+D+F+F+G+H
       
    // loop through, if there are some duplicates characters
    // they have to be in sequence, we need to keep track of the sequence
    // 
    // if there are removals

    
    // source = "ABCDEFG"
    // target = "ABCDEFG"
    // result = "ABCDEFG"
       
       
    // source = "ABCDEFG"
    // target = " BCDEFG"
       
    // result = "-ABCDEFG"
       
    // source = " BCDEFG"
    // target = "ABCDEFG"
       
    // result = "+ABCDEFG"
       
    // source = "      AAAAB"
    // target = "AAAAAAAAAAB"
       
    // source = "AAAAAAAAAAAAB"
    // target = "AAAAB"
       
       
    // Dynamic programming
       

    int sourceIndex = 0;
    int targetIndex = 0;
    
    List<String> answer = new LinkedList<String>();
    
    Map<String, Integer> memo = new HashMap<>();
    
    while (sourceIndex < source.length() && targetIndex < target.length()){

      if (source.charAt(sourceIndex) == target.charAt(targetIndex)){
        answer.add("" + source.charAt(sourceIndex));
        sourceIndex++;
        targetIndex++;
      }
      else if (dp(sourceIndex+1,targetIndex, memo, source,target) <= dp(sourceIndex,targetIndex+1, memo, source,target)){
        answer.add("-" + source.charAt(sourceIndex));
        sourceIndex++;
      }
      else{
        answer.add("+" + target.charAt(targetIndex));
        targetIndex++;
      }

    }
 
    while (targetIndex < target.length()){
      answer.add("+" + target.charAt(targetIndex));
      targetIndex++;
    }
    while (sourceIndex < source.length()){
      answer.add("-" + source.charAt(sourceIndex));
      sourceIndex++;
    }
    return answer.stream().toArray(String[]::new);

	}

	public static void main(String[] args) {
	                System.out.println(Arrays.toString(diffBetweenTwoStrings("ABCDEFG","ABDFFGH")));
	}

}
