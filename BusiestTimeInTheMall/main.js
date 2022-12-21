function findBusiestPeriod(data) {
    // your code goes here
    let maxPeople = 0;
    let people = 0;
    let maxTimestamp = 0
    for(let i=0; i<data.length; i++){
      if(data[i][2] === 1){
        people += data[i][1]
      }
      else {
        people -= data[i][1]
      }
      if (people > maxPeople && ( i === data.length-1 || data[i][0] !== data[i+1][0]) ){
        maxPeople = people;
        maxTimestamp = data[i][0];
      }
    }
    
    return maxTimestamp
    
  }
  
  /*
  maxPeople = 
  [14,10, 8, 18, 0, 18, 17, 24, 17]
  max value = 18
  find index = 3
  return data[3][0]
  
  
  data =         [ [1487799425, 14, 1], 
                   [1487799425, 4,  0],
                   [1487799425, 2,  0],
                   [1487800378, 10, 1],
                   [1487801478, 18, 0],
                   [1487801478, 18, 1],
                   [1487901013, 1,  0],
                   [1487901211, 7,  1],
                   [1487901211, 7,  0] ]
  
  */