package main

import (
	"fmt"
	"math"
)

func Root(x float64, n float64) float64 {
	left := 0.0
	right := x

	for left < right {

		//fmt.Println("left", left)
		//fmt.Println("right", right)

		mid := (left + right) / 2.0
		//fmt.Println("mid", mid)

		power := math.Pow(mid, n)

		if power >= x-0.001 && power <= x+0.001 {
			return mid
		}
		if power > x {
			right = mid
		} else {
			left = mid
		}
	}

	return -1

}

func main() {
	fmt.Println(Root(7.0, 3.0))
}
