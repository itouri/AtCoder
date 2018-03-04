package main

import "math"

/*
美しい多重配列の初期化の仕方
美しい絶対値の取り方
美しい配列の出力方法
*/

func main() {
	/* 美しい多重配列の初期化の仕方 */
	// 固定長配列 -> 普通使わないからいいや
	// 可変配列（スライス）
	row := 4
	col := 3
	matrix := make([][]int, row)
	for i := range matrix {
		matrix[i] = make([]int, col)
	}

	/* 絶対値の取り方 */
	i := 1
	j := 2
	x := int(math.Abs(3 - i)) //?
	y := int(math.Abs(3 - j)) //?
}
