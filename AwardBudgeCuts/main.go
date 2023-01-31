package main

import (
	"fmt"
	"sort"
)

func FindGrantsCap(grantsArray []float64, newBudget float64) float64 {

	/**

	  sort.Float64s(arr);
	  Approach 1:

	    remove the grants

	    Keep an average = start at 190 / 5 (newBudget / len(grantsArray))

	    Start at 38


	    Sort(gransArray)

	    Loop
	       if the number is smaller than the average

	       Remove number from total sum

	       Recalculate a new average

	       If number > average:
	          break

	    return average


	    RT O(nlogn)
	    Space O(1)
	*/

	// Check if newBudget > total
	total := 0.0

	for _, grant := range grantsArray {
		total += grant
	}

	if total < newBudget {
		return -1
	}

	//start by sorting
	sort.Float64s(grantsArray)
	//fmt.Println(grantsArray)

	totalGrants := float64(len(grantsArray))
	//remove the numbers smaller than average from total
	for _, grant := range grantsArray {

		// new average
		average := newBudget / totalGrants

		// remove grant from the newBudget
		if grant < average {
			totalGrants--
			newBudget -= grant
		} else {
			break
		}

	}

	return newBudget / totalGrants
}

func main() {
	arr := []float64{2, 100, 50, 120, 1000}
	res := FindGrantsCap(arr, 20000)
	fmt.Println(res)
}

/*
  static double findGrantsCap(double[] grantsArray, double newBudget) {
    Arrays.sort(grantsArray);

    for(int i = 0; i < grantsArray.length; i++) {
      double grant = grantsArray[i];

      double remainingPerGrant = newBudget / (grantsArray.length - i);
      newBudget -= grant;

      if(remainingPerGrant <= grant) {
        return remainingPerGrant;
      }
    }

    return -1;
  }
*/
