package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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
	sc.Split(bufio.ScanWords)
	N := nextInt()
	a := []int{}
	for i := 0; i < N; i++ {
		a = append(a, nextInt())
	}
	sort.Ints(a)
	var alice int
	var bob int
	for i := N - 1; i > -1; i-- {
		alice += a[i]
		i--
		if i == -1 {
			break
		}
		bob += a[i]
	}
	fmt.Println(alice - bob)
}
