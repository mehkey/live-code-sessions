package main

/**

  Approach 1:
  
  Find all the words delimited by ' '
  create a list of words
  reverse the list of words
  
  n characters
  
  TC O(n)
  SC O(n)
  
  
  Approach 2:
  
  Revese the string
  Reverse every word
  
  n characters
  
  TC O(n)
  SC O(1)
  
  
  
  

*/
//import "fmt"
func ReverseWords(arr []string) []string {
  
  //reverse all characters
  Reverse(arr,0,len(arr)-1)
  
  //reverse each word
  // i is the start of the word
  // j is the end of the word
  i := 0
  for ; i < len(arr) ; i++ {
    
    //find the last character
    j := i
    for ; j < len(arr); j++ {
      
      if arr[j] == " " {
        break
      }
    }
    //reverse the word
    Reverse(arr,i,j-1)
    
    //move i to the last position
    i = j 

  }
  
  return arr
}

//Reverse arr from position start to position end
func Reverse(arr []string, start int, end int) {
  
  j := end
  i := start 
  //loop through each
  for  ; i < j; {
    
    temp := arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    i++
    j--
  }
  
  return
}

func main() {
  arr := []string{"a","b","c", " ", "d","e","f"}
  //reverse(arr,0,2)
  ReverseWords(arr)

}

linkedin/in/m-chk
changjun kim

Regression
Classification
Clustering
NLP
ImageProcessing
Robtitcs


AI = Optimization + ML 

A* shortest path
Traveling salesman
MinMax 
monte carlo search tree on board game such as chess

Stochastic or Baysian

GANS = Generative Adversarial Neural Network


https://www.geeksforgeeks.org/generative-adversarial-networks-gans-an-introduction/

Leetcode

Leetcode Contest
6%




