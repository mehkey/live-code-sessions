function findDuplicates(arr1, arr2) {
    const smaller = arr1.length > arr2.length ? arr2 : arr1
    const larger = arr1.length > arr2.length ? arr1 : arr2
    
    const bSearch = (target, j) => {
      let left = j
      let right = larger.length - 1
  
      let smallestIdx = -1
      
      while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (larger[mid] === target) {
          smallestIdx = mid
        }
  
        if (larger[mid] >= target) {
          right = mid - 1
        } else {
          left = mid + 1
        }
      }
  
      return smallestIdx
    }
  
    let i = 0
    let j = 0
    const res = []
    
    while (i < smaller.length) {
      const idx = bSearch(smaller[i], j)
      if (idx !== -1) {
        res.push(smaller[i])
        j = idx + 1
      }
      i += 1
    }
    return res
  }
  
  const arr1 = [11]
  const arr2 = [11]
  
  console.log(findDuplicates(arr1, arr2))
  
  
  function findDuplicatesEqualSize(arr1, arr2) {
    let i = 0, j = 0;
    const res = [];
    
    foo() // it's going to call the return value of foo
    (1 > someThingWithSideEffect() ? 1 : 2)
    
    while (i < arr1.length && j < arr2.length) {
      if (arr1[i] === arr2[j]) {
        res.push(arr1[i]);
        
      }
      
      /*
         res = [1, 1]

         arr1 = [1, 2]
                 i

         arr2 = [1, 1, 1, 1]
                    j

         arr[1] = 1 < arr[j] = 1 is not true

         j += 1
          
      */
      
      if (arr1[i] < arr2[j]) {
        i += 1
      } else {
        j += 1
      }
    }
    return res
  }
  