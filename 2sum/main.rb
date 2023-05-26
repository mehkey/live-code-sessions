
def find_pairs_with_given_difference(arr, k)
    result = [] 
    valToIndex = {}
  
    arr.each_with_index do |currValue, index|
       valToIndex[currValue] = true
    end
    
    arr.each_with_index do |currValue, index|
       valueNeeded = k + currValue
       if valToIndex.has_key?(valueNeeded)
          result.push([valueNeeded, currValue])
        end 
    end
    # puts valToIndex
    return result
  end
  
  # arr = [0, -1, -2, 2, 1] k = 1 
  # [[1, 0], [0, -1], [-1, -2], [2, 1]]
  
  =begin
  
  -1 - y = 1, y = -2 
  x - -1  = 1, x = 0 
  
  
  {
    0: 0,
    -1: 1,
  }
  
  [0, -1]
  =end
  
  =begin
  0 - -1  = 1 
  -1 - -2  = 1 
  -2 - 3 = 1 
  2 - 1 = 1 
  1 - 0 = 1 
  
  
  {
    0: 0,
    -1: 1, 
    -2: 2,
    2: 3,
    1: 4,
  }
  
  [1, 0]
  =end
  
  =begin
  arr = [0, -1]
  k = 1
  puts find_pairs_with_given_difference(arr, k) 
  =end