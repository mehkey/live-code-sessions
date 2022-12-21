# Busiest Time in The Mall
The Westfield Mall management is trying to figure out what the busiest moment at the mall was last year. You’re given data extracted from the mall’s door detectors. Each data point is represented as an integer array whose size is 3. The values at indices 0, 1 and 2 are the timestamp, the count of visitors, and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), respectively. Here’s an example of a data point: [ 1440084737, 4, 0 ].

Note that time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall reached its busiest moment last year. The return value is the timestamp, e.g. 1480640292. Note that if there is more than one period with the same visitor peak, return the earliest one.

Assume that the array data is sorted in an ascending order by the timestamp. Explain your solution and analyze its time and space complexities.

```
Example:

input:  data = [ [1487799425, 14, 1], 
                 [1487799425, 4,  0],
                 [1487799425, 2,  0],
                 [1487800378, 10, 1],
                 [1487801478, 18, 0],
                 [1487801478, 18, 1],
                 [1487901013, 1,  0],
                 [1487901211, 7,  1],
                 [1487901211, 7,  0] ]

output: 1487800378 # since the increase in the number of people
                   # in the mall is the highest at that point
```

## Constraints:

```
[time limit] 5000ms

[input] array.array.integer data

1 ≤ data.length ≤ 100
[output] integer
```




```javascript

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

```



```python

from aenum import Enum
from collections import defaultdict

class Change(int,Enum):
  Enter = 1
  Exit = 0
  pass

class Epoch:
  def __init__(self,epoch):
    self.epoch  = epoch
    self.visitor  = 0

  def apply_change(self,change, count):
    if change == Change.Enter:
      self.visitor +=  count 

    if change == Change.Exit:
      self.visitor -= count

def find_busiest_period(data):
  
  
  epochs = defaultdict(Epoch)
  
  for epoch in data:
    
    time = epoch[0]
    if time not in epochs:
        epochs[time] = Epoch(Epoch(epoch[0]))

    epochs[time].apply_change(epoch[2],epoch[1])

    

    old_time = epoch_change.epoch

    current_count = epoch_change.apply_change(current_count)

    if i < len(data) -1 and epoch_change.epoch != data[i+1][0]  and current_count > max_count:
      max_count = current_count
      max_time = epoch_change.epoch
      
    if i ==  len(data) -1 and current_count > max_count:
      max_time = epoch_change.epoch


  return max_time

```