package main

func IndexEqualsValueSearch(arr []int) int {
	/*

	   Approach 1:
	    Loop
	    return the first value

	    Otherwise return -1

	    T O(n)
	    S O(1)

	*/
	/*
	  index  [0 1 2 3 4 5 6 7 8 9]   index 3
	  value  [0 1 2 3 4 5 6 7 8 9]   val :
	    1/ arr[mid] > mid:

	    2/ arr[mid] < mid:

	    3/ arr[mid] = mid:
	      while arr[mid-1] == mid-1:
	        mid -= 1
	      return mid
	*/
	//loop through arr
	/*for i,val := range(arr){
	    if i == val{
	      return i // or val
	    }
	  }

	*/

	left := 0

	right := len(arr) - 1

	last := 1000000

	//Binary Search
	for left <= right {

		mid := (left + right) / 2

		if arr[mid]-mid < 0 {
			left = mid + 1
		} else if arr[mid]-mid > 0 {
			right = mid - 1
		} else {
			if mid < last {
				last = mid
			}
			right = mid - 1
		}
	}

	if last == 1000000 {
		return -1
	}

	return last

}

func main() {

}
