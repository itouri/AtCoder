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

func sum(n int) int {
	return n * (n + 1) / 2
}

func main() {
	/* 初期化開始 */
	sc.Split(bufio.ScanWords)
	R, G, B := nextInt(), nextInt(), nextInt()
	/* 初期化終了 */
	var ans int
	/* 3つがくっつく */
	if R+2*G+B >= 400 {
	} else if R+G >= 200 || G+B >= 200 { /* 2つがくっつく */
		
	} else { /* 1つもくっつかない */
		// R,G,Bが偶数ならそれぞれマイナスn回
		ans += 2*sum(R/2) - (1-R%2)*R/2
		ans += 2*sum(G/2) - (1-G%2)*G/2
		ans += 2*sum(B/2) - (1-B%2)*B/2
	}
	fmt.Printf("%d\n", ans)
}
