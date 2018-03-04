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
	sc.Split(bufio.ScanWords)
	var grid [3][3]int
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			grid[i][j] = nextInt()
		}
	}
	c := grid[0][0] + grid[1][1] + grid[2][2]
	if c != grid[0][1]+grid[1][2]+grid[2][0] || c != grid[0][2]+grid[1][0]+grid[2][1] {
		fmt.Printf("No")
		return
	}
	fmt.Printf("Yes")
	return
}
