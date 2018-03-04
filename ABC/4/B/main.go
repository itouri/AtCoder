package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	COL = 4
	ROW = 4
)

var sc = bufio.NewScanner(os.Stdin)

func nextStr() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	/* 初期化開始 */
	matrix := make([][]string, ROW)
	ansMatrix := make([][]string, ROW)
	sc.Split(bufio.ScanWords)
	for i := 0; i < ROW; i++ {
		ansMatrix[i] = make([]string, COL)
		matrix[i] = make([]string, COL)
		for j := 0; j < COL; j++ {
			matrix[i][j] = nextStr()
		}
	}
	/* 初期化終了 */

	/* 変換開始 */
	for i := 0; i < ROW; i++ {
		for j := 0; j < COL; j++ {
			x := int(math.Abs(float64(3 - i))) //?
			y := int(math.Abs(float64(3 - j))) //?
			ansMatrix[x][y] = matrix[i][j]
		}
	}
	/* 変換終了 */

	for i := 0; i < ROW; i++ {
		fmt.Printf("%s %s %s %s\n", ansMatrix[i][0], ansMatrix[i][1], ansMatrix[i][2], ansMatrix[i][3])
	}
}

// OK 00:43:56
/*
標準入力の扱いかたにわりと時間がかかった
ansMatrix := matrix をやってはいけない 参照渡しだから
標準入力の取り方については悪くないと思う
TODO
	美しい多重配列の初期化の仕方
	美しい絶対値の取り方
	美しい配列の出力方法
*/
