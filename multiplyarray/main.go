package main

/*

Approach 1:

Two Loops

runtime:O(N^2)
space:O(1)



Approach 2:

Left and Right Array

runtime: O(N)
space: O(N)


Approach 3:

Left array only

runtime: O(N)
space: O(N)


[8, 10, 2]


*/

func ArrayOfArrayProducts(arr []int) []int {

	if len(arr) <= 1 {
		return []int{}
	}

	//left_arr  []int;
	left_arr := make([]int, len(arr))

	//fmt.Println(left_arr)

	//Loop and add to the left array

	current := 1
	for i, val := range arr {
		left_arr[i] = current
		current *= val
	}

	//fmt.Println(left_arr)

	//Loop through  the array from the right to multiply with the the right value
	current = 1
	for i := len(arr) - 1; i >= 0; i-- {
		left_arr[i] = left_arr[i] * current
		current *= arr[i]
	}

	//fmt.Println(left_arr)

	// we have the multiplication of the right and left values
	return left_arr
}

func main() {
	arr := []int{8, 10, 2}

	ArrayOfArrayProducts(arr)
}
