[Secret Answer🤫] Double BFS with A Double Set of Visited Nodes 👌😍 [Python🐍]


/*
Input:
  - Nonempty matrix of integers
  
Output:
  - The length of the longest strictly increasing path
    - To construct a path, start from any position in the matrix, and then traverse either up, down, left, right until you cannot traverse any further

Example 1:

1 2 3
6 5 4

1 -> 2 -> 3 -> 4 -> 5 -> 6
Return 6

Example 2:

7 3 6
7 5 -1
8 1 1

3 -> 5 -> 7 -> 8
-1 -> 5 -> 7 -> 8
Return 4


Approach 1:

Start at any number

DFS 
  - returnt the length of the longest increasing path
  - Store the number in a new matrix
  
Loop for all numbers in the matrix:
  call the DFS if the node hasn't been visited
  

n rows, m columns
Runtime: O(n*m)
Space: O(n*m) (New matrix)



*/

const calculateTheLongestIncreasingPath = ( matrix ) => {
  
  const maxMatrix = new Array(matrix.length);
  for (var i = 0; i < matrix.length; i++){
    maxMatrix[i] = new Array(matrix[0].length);
    for (var j = 0; j < matrix[0].length; j++ ){
      maxMatrix[i][j] = 0;
    }
  }
  
  //keep the max
  var max = 0;

  //loop though all the numbers
  for (var i = 0; i < matrix.length; i++){
    
    for (var j = 0; j < matrix[0].length; j++ ){
      
      max = Math.max( max,dfs(i,j, matrix, maxMatrix) );
      
    }
    
  }
  
  //return the max
  return max
  
};

//Store the directions for fast access
const DIRS = [
  [-1,0],
  [0,1],
  [0,-1],
  [1,0]
]

const dfs = ( i, j, matrix , maxMatrix) => {
  
  if (maxMatrix[i][j] != 0 ){
    return maxMatrix[i][j];
  }
  
  var max = 1;

  for (var dir of DIRS){
    
    const newX = i+dir[0];
    const newY = j+dir[1];
    
    // dont go out of bounds and 
    if (matrix[newX]?.[newY] === undefined && matrix[newX][newY] > matrix[i][j] ){
      max = Math.max( dfs(newX, newY, matrix, maxMatrix)+1, max);
    }
    
  }
  
  maxMatrix[i][j] = max;

  return maxMatrix[i][j];

};

/*


https://stackoverflow.com/questions/72114300/how-to-generate-k-largest-subset-sums-for-a-given-array-contains-positive-and-n/72117947#72117947


6198 pairs satisfy inequality

2163 earliest possible day to bloom

Find the Kth largest subset

https://excalidraw.com/#room=dc9e31681612e25b3d29,ogKrpD2OL4tgDLrGZ_ic4w

https://stackoverflow.com/questions/72114300/how-to-generate-k-largest-subset-sums-for-a-given-array-contains-positive-and-n/72117947#72117947
https://sites.cs.ucsb.edu/~agrawal/fall2009/PNUTS.pdf
http://nil.csail.mit.edu/6.824/2020/papers/memcache-fb.pdf
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html


*/
