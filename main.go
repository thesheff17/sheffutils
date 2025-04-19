package main

import (
	"fmt"
	"net/http"
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

func MessageHandler(message string) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "%s", message)
	}
}

func WebHealthCheck(w http.ResponseWriter, r *http.Request) {
	m1 := "status: running \ntimestamp: " + GetTimestampHypens()
	fmt.Fprintf(w, "%s", m1)
}

func main() {
	fmt.Println("Welcome to golang.  Please visit https://dev.go for more info.")

	timestamp := GetTimestampHypens()
	fmt.Println("current timestamp with hpyens: ", timestamp)

	// example of passing a message through to the function handler.
	defaultMsg := "hello world from go.dev webserver."
	http.HandleFunc("/", MessageHandler(defaultMsg))

	http.HandleFunc("/healthcheck", WebHealthCheck)

	fmt.Println("Server is starting on port 8080...")
	http.ListenAndServe(":8080", nil)
}
