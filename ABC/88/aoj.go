package main

import (
	"bufio"
	"fmt"
	"os"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	sc.Scan()
	qs := []rune(sc.Text())

	var h int
	var top int
	var ans int
	var stack int
	anss := []int{}
	for i := 0; i < len(qs); i++ {
		if qs[i] == 92 {
			h--
		} else if qs[i] == 47 {
			h++
			if h > top {
				top = h
			} else {
				var j int
				for j = i; j >= 0; j-- {
					if qs[j] == 92 {
						qs[j] = '-'
						break
					}
					qs[j] = '-'
				}
				stack += i - j
				ans += i - j
				// new みずたまり
				if last_j < j {
					anss = append(anss, stack)
					stack = 0
				}
			}
		}
	}
	fmt.Println(ans)
	fmt.Printf("%d ", len(anss))
	for i := range anss {
		fmt.Printf("%d", anss[i])
		if i != len(anss) {
			fmt.Print(" ")
		}
	}
}
