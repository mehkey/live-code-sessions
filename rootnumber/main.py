
function root(x, n) {

  l = 0

  r = x
  
  if (n == 1){
    return x
  }
  
  mid = (l+r) / 2
  
  while (l <= r){
  

    mid = (l+r) / 2
    
    new_x = mid ** n
    
    if x - 0.001 <= new_x <= x +0.001:
      return mid

    if new_x > x:
      r = mid
    else:
      l = mid

  return -1
}



Friring rounds
  bad teams
  Regular annual 10% reduction (Amazon)
  
  January 