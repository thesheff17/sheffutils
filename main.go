package main

import (
	"fmt"
	"strings"
	"time"
)

func HelloWorld() string {
	return "Hello, World from go.dev"
}

func GetTimestampHypens() string {
	currentTime := time.Now()
	timestamp := currentTime.Format("20060102150405")

	// Replace parts with hyphens
	year := timestamp[0:4]
	month := timestamp[4:6]
	day := timestamp[6:8]
	hour := timestamp[8:10]
	minute := timestamp[10:12]
	second := timestamp[12:14]

	formattedTimestamp := strings.Join([]string{year, month, day, hour, minute, second}, "-")

	return formattedTimestamp

}
func main() {
	fmt.Println("Welcome to golang.  Please visit https://dev.go for more info.")

	timestamp := GetTimestampHypens()
	fmt.Println("current timestamp with hpyens: ", timestamp)
}
