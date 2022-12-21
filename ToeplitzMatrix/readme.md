# Toeplitz Matrix
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any dimensions, not necessarily square.

For example,
```
[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
is a Toeplitz matrix, so we should return true, while

[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]
isn’t a Toeplitz matrix, so we should return false.
```
## Constraints:
```
[time limit] 5000ms
[input] array.array.integer arr
0 ≤ arr.length ≤ 20
0 ≤ arr[i].length ≤ 20
0 ≤ arr[i][j] ≤ 20
[output] boolean
```


```javascript
function isToeplitz(arr) { 
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
  ```  

```py
def isToeplitz(arr):
 
 hm = {}

 for i in range(len(arr)):
  for j in range(len(arr[0])):

   if i - j not in hm:

    hm[i-j] = arr[i][j]

   elif hm[i-j] != arr[i][j]:
    return False

 return True
```