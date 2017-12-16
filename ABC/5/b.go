package main

// OK! 10'05

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
	n := nextInt() - 1
	min := nextInt()
	for ; n > 0; n-- {
		t := nextInt()
		if min > t {
			min = t
		}
	}
	/* 初期化終了 */
	fmt.Printf("%d\n", min)
}
