function findPairsWithGivenDifference(arr, k) {

    var unique_numbers = new Set(arr);
  
    result = [];
  
    for (number of arr){
  
      if ( unique_numbers.has(number + k) ){
        result.push([number + k,number]);
      }
    }
    return result
  }
  