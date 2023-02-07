package main


/*

Approach 1: 
  
  Recurisve solution to find all possible paths
  
  
Approach 2:

  Dynamic Programming Solution
  
  Array of number of path to the current position in the array

  (i,j) -> 

  2 ways to do DP:

  Linear DP - 
  
  Array of size n
  Number of possible path for row i level j

  Memorization DP - 

  dp(i,j)
  
  dp(i,j) = dp(i,j -1) + dp(i-1,j)



  Time: O(n^2)
  Space: O(n)

*/
import "fmt"
func NumOfPathsToDest(n int) int {
  
  //initlize the dp with all 1's
  dp := make([]int, n)
  
  for i := 0 ;i<n; i++ {
    dp[i] = 1
  }
  
  //loop throught the columns
  for j:= 1; j < n; j++ {
    
    newDP := make([]int, n)
    
    for i:=1 ; i < n; i++ {
      
      //only add temp if we are passed the middle
      var temp = 0
      
      if i >= j {
        temp = newDP[i-1]
        newDP[i] = dp[i] + temp
      }

    }

    dp = newDP
  }
  return dp[n-1]
}


func dp(i int, j int, n int, hm map) int {
  
  if hm.contains( i+','+j ) {
    return hm[i+','+j]
  }

  if j > i {
    return 0
  }
  if j == n -1 {
    return 1
  }

  
  map[i+','+j] = dp(i+1,j,n) + dp(i,j+1,n)
  return hm[i+','+j]
}


func main() {
  hm := make([string,int]map,n*n)
  res := dp(0,0,4,)
  //res := NumOfPathsToDest(4)
  fmt.Println(res)
}