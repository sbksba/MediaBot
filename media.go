package main

import (
	"./pkg/cfg"
	"fmt"
	"log"
	"time"
	"strconv"
	"os/exec"
)

func worker(id int, jobs string, verbose string) {
	binary := exec.Command("./MediaBot.pl", jobs)
	if verbose == "true" {
		fmt.Println("worker #",id,"[",jobs,"]");
	}
	binary.Run()
}

func periodic() {
	// create the map
	mymap := make(map[string]string)
	err := cfg.Load("config/config.cfg", mymap)
	if err != nil {
		log.Fatal(err)
	}
	m := mymap["movie"]
	s := mymap["serie"]
	v := mymap["verb"]
	t := mymap["time"]
	ti,_ := strconv.Atoi(t)

	slice := make([]string, 2)
	slice[0] = m
	slice[1] = s

	// Timestamp
	if v == "true" {
		fmt.Println("\n--",time.Now(),"--")
	}

	// Start workers
	go worker(1, slice[0], v)
	go worker(2, slice[1], v)
		
	time.AfterFunc(time.Second*time.Duration(ti), periodic)
}

func main() {
	periodic()
	select{}
}
