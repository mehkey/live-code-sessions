function getDifferentNumber(arr) {
  
    /*
    
     [0,1,2,3,4,5]
     
     positive integer missing
     
     Approach 1:
     
     Loop from 0 to len(arr) + 1
     
       0, 1, 2, 3, 4, 5
     
       Loop through the array to find the number
       
       
          if you find return it
          
     O(N^2)
  
  
  
     Approach 2:
     
     HashSet
     
     Put in the numbers in a set
     
     Loop from 0 to len(arr) + 1
        if its not in the hashset, retun number
        
     time:O(N)
     space:O(N)
      
     
     Approach 3:
     
     N:size
     
     N * (N+1) // 2
     Sum
     
     add all numbers
     
     solution: Sum - (addednumbers)
     
     time: O(N)
     space: O(1)
     
     
     Approach 4:
     
     XOR of all the numbers
     
     should have the solution at the end
     
     time: O(N)
     space: O(1)
     
  
     setting numbers: negative 
     
  
     https://www.geeksforgeeks.org/find-the-missing-number/
  
  
    */
  
    let valid_number_count = 0;
  
    for (current of arr){
      if (current < arr.length+1){
        valid_number_count += 1;
      }
    }
    
    //[0]
    //arr = [0, -5, 2, 3]
  
    let targetSum  = valid_number_count * (valid_number_count+1) / 2;
  
    //1+2+3+4 = n*n+1
    //if (n == 1 ){
    //  return arr[0] == 0 ? 1 : 0;
    //}
    //console.log(sum)
  
    let currentSum = 0;
  
    //s = new Set(arr);
    
    
    for (current of arr){
      if (current < valid_number_count+1){
        currentSum += current;
      }
      //sum -= cur;
    }
  
    // #x^or
    //1 ^ n
    //console.log(x)
    
    //console.log(targetSum-addNumbers)
    return targetSum-currentSum;
    
  }
  
  getDifferentNumber([4, 1, 2, 3])