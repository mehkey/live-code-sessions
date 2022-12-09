package main

func FindPairsWithGivenDifference(arr []int, k int) [][]int {

	var res [][]int

	var hm map[int]int = make(map[int]int)

	for _, v := range arr {
		hm[v] = 1
	}

	for _, v := range arr {
		if hm[k+v] == 1 {
			var r = []int{k + v, v}
			res = append(res, r)
		}
	}

	//if len(res) == 0{
	//  var out [][]int = make([][]int)
	//  return out
	//}
	return res
}

func main() {

}
