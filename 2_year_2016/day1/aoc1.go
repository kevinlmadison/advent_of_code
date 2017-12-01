package main

import (
	"fmt"
)

type Direction struct {
	dirs [4]byte
}

func (dir *Direction) get_len() (len int) {
	len = len(dir.dirs)
	return
}

func main() {
	fmt.Printf("hello, world")
}
