package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Query struct {
	i int
	j int
}

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return i
}

func nextNInt(n int) []int {
	ret := []int{}
	for i := 0; i < n; i++ {
		ret = append(ret, nextInt())
	}
	return ret
}

func main() {
	/* 初期化開始 */
	sc.Split(bufio.ScanWords)
	n := nextInt()
	d := make([][]int, n, n)
	for i := 0; i < n; i++ {
		d[i] = nextNInt(n)
	}
	q := nextInt()
	P := nextNInt(q)
	/* 初期化終了 */

	query := []Query{}
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			query = append(query, Query{i: i + 1, j: j + 1})
			if i != j {
				query = append(query, Query{i: j + 1, j: i + 1})
			}
		}
	}

	for _, p := range P {
		que := makeQuery(p, query)
		fmt.Println(search(que, n, d))
	}
}

func search(query []Query, n int, d [][]int) int {
	max := 0
	for _, q := range query {
		for i := 0; i < n-q.j+1; i++ {
			for j := 0; j < n-q.i+1; j++ {
				fmt.Printf("%d,%d,%d,%d\n", i, j, q.i, q.j)
				v := addGrid(i, j, q.i, q.j, d)
				if v > max {
					max = v
				}
			}
		}
	}
	return max
}

func addGrid(I int, J int, w int, h int, d [][]int) int {
	v := 0
	for i := I; i < I+h; i++ {
		for j := J; j < I+w; j++ {
			v += d[i][j]
		}
	}
	//fmt.Printf("\n")

	return v
}

func makeQuery(p int, query []Query) []Query {
	var index int
	for index = len(query) - 1; index != 0; index-- {
		if query[index].i*query[index].j < p {
			break
		}
	}
	for i := index; i >= 0; i-- {
		for j := i - 1; j >= 0; j-- {
			if query[j].i == 0 && query[j].j == 0 {
				continue
			}
			if query[j].i < query[i].i && query[j].j < query[i].j {
				query[j] = Query{}
			}
		}
	}
	que := []Query{}
	for _, q := range query {
		if q.i != 0 && q.j != 0 {
			que = append(que, q)
		}
	}
	//fmt.Printf("%#v\n", que)
	return que
}
