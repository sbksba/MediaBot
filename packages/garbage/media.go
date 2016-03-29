package main

import (
	"./packages/cfg"
	//"fmt"
	"log"
	//"strconv"
	"os"
	"os/exec"
	"syscall"
)

func Extend(slice []string, element string) []string {
	n := len(slice)
	if n == cap(slice) {
		// Slice is full; must grow.
		// We double its size and add 1, so if the size is zero we still grow.
		newSlice := make([]string, len(slice), 2*len(slice)+1)
		copy(newSlice, slice)
		slice = newSlice
	}
	slice = slice[0 : n+1]
	slice[n] = element
	return slice
}

// Append appends the items to the slice.
// First version: just loop calling Extend.
func Append(slice []string, items ...string) []string {
	for _, item := range items {
		slice = Extend(slice, item)
	}
	return slice
}

func main() {
	// create the map
	mymap := make(map[string]string)
	err := cfg.Load("config.cfg", mymap)
	if err != nil {
		log.Fatal(err)
	}
	m := mymap["movie"]
	s := mymap["serie"]
	//t := mymap["time"]
	v := mymap["verb"]

	//ti,_ := strconv.Atoi(t)
	binary, lookErr := exec.LookPath("/usr/bin/perl")
	if lookErr != nil {
		panic(lookErr)
	}

	env := os.Environ()
	args := []string{"","MediaBot.pl"}

	if v == "true" {
		args = Append(args, "v", m, s)
	} else {
		args = Append(args, m, s)
	}

	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}
