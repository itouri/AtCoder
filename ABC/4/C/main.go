package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return i
}

func main() {
	/* 初期化開始 */
	sc.Split(bufio.ScanWords)
	N := nextInt()
	ans := [6]int{}
	/* 初期化終了 */

	// 30回の入れ替えごとに並びは元に戻る
	N %= 30

	// 5回の入れ替えで数字が最後に1つスライドするだけになる
	n := N / 5

	for i := range ans {
		ans[i] = (i+n)%6 + 1
	}

	// 残りは純粋に入れ替え
	c := N % 5
	for i := 0; i < c; i++ {
		t := ans[i]
		ans[i] = ans[i+1]
		ans[i+1] = t
	}

	for _, a := range ans {
		fmt.Printf("%d", a)
	}
	fmt.Println()
}

// OK 00:19:30
/*
特に思うことはない
どこまで効率化できるのか気になる
*/
