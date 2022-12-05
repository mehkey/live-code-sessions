function root(x, n) {

    let l = 0
  
    let r = x
  
    if (n == 1){
      return x
    }
  
    let mid = (l+r) / 2
  
    while (l < r) {
  
      mid = (l+r) / 2
  
      const new_x = Math.pow(mid,n)
  
      if ( (x - 0.001) <= new_x && new_x <= (x +0.001)){
        return Math.round(mid * 1000) / 1000
      }
  
      if (new_x > x){
        r = mid
      }
      else{
        l = mid
      }
    }
  
    return -1
  }