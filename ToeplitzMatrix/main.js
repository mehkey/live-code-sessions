function isToeplitz(arr) {
	/**
	@param arr: integer[][]
	@return: boolean
	*/

  /**
  
  Approach 1:
  
  Loop throught the top row
    counter start at 1
    c = 1
    go to 
    [startx + c][start y + c]
    c+=1

  Loop throught the left column 
    counter start at 1
    c = 1
    go to 
    [startx + c][start y + c]
    c+=1
  
  r rows, c cols
  runtime; O(r * c)
  
  space: O(1)
  
  
  Approach 2
  
  row_id + col_id 
  
  0 0
  
  01  10
  
  1 1
  
  2 2
  
  A
 [[1,2,3,4],
 [2,3,4,5],
 [3,4,5,6]]
 
 row_id - col_id
  
  B
 [[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
 
 
 map (key row-col) val start
 
 space( row + col)
 
 
 Approach 3:
 
   Check if the number is equal to the next one on the right
  

 
  */
  
  //const because it won't change
  const M = arr.length;
  const N = arr[0].length;
  const MIN_M_N = Math.min(M,N);
  
  //start at the left column
  for(let i = 0; i < M ; i++ ){
    for(let j = 0; j < N ; j++ ){
      if ( (i + 1) < M && (j + 1) < N){
        if (arr[i][j] != arr[i+1][j+1]){
          return false;
        }
      } 
    }
  }
  
  return true;
  
  /*
  //start at the top row
  for(let j = 0; j < N ; j++ ){
    const startX = 0;
    const startY = j;
    const startVal = arr[startX][startY]
    //loop +1 at the time until min -1
    for(let c = 1; c < MIN_M_N -1; c++){
      if (arr[startX+c][startY+c] != startVal) {
        return false;
      }
    } 
  }
  
  //start at the left column
  for(let i = 1; i < M ; i++ ){
    const startX = i;
    const startY = 0;
    const startVal = arr[startX][startY]
    //loop +1 at the time until the min -1 
    for (let c = 1; c < MIN_M_N-1; c++){
      if (arr[startX+c][startY+c] != startVal) {
        return false;
      }
    } 
  }

  return true;
  */
}
