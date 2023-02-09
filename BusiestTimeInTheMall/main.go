package main

/*

  Approach 1:

  maxPeople := 0
  maxTime := 0


  Loop trought the array

    comparing the current timestamp to the nexttimestamp

    epochSum the totalamount of people entering for that timestamp

    totalSum += epochSum

    totalSum  (only update totalsum when the timesamps are different between the current timestamep and the next timestamp)


    if totalSum > maxMariable {
      maxMariable = totalSum
      maxTime = currentTime
    }

  return maxTime

  N is the number of elements in the array

  time O(N)
  space O(1)


*/
import (
	"fmt"
)

func FindBusiestPeriod(data [][]int) int {

	var maxPeople int = 0
	var maxTime int = 0

	var totalSum int = 0
	var epochSum int = 0

	for i, _ := range data {

		//assuming only 0 and 1 could be present
		if data[i][2] == 1 {
			epochSum += data[i][1]
		} else {
			epochSum -= data[i][1]
		}

		//we don't want to read the array at len(data) -1
		if i == len(data)-1 || data[i][0] != data[i+1][0] {

			totalSum += epochSum

			if totalSum > maxPeople {
				maxPeople = totalSum
				maxTime = data[i][0]
			}

			epochSum = 0
		}

	}

	return maxTime

}

func main() {

	input := [][]int{{1487799425, 14, 1},
		{1487799425, 4, 0},
		{1487799425, 2, 0},
		{1487800378, 10, 1},
		{1487801478, 18, 0},
		{1487801478, 18, 1},
		{1487901013, 1, 0},
		{1487901211, 7, 1},
		{1487901211, 7, 0}}

	response := FindBusiestPeriod(input)
	fmt.Println(response)

}

//[ 1440084737, 4, 0 ].

/*input:  data = [ [1487799425, 14, 1],
  [1487799425, 4,  0],
  [1487799425, 2,  0],
  [1487800378, 10, 1],
  [1487801478, 18, 0],
  [1487801478, 18, 1],
  [1487901013, 1,  0],
  [1487901211, 7,  1],
  [1487901211, 7,  0] ] */
