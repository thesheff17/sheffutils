package main

import (
	"regexp"
	"testing"
)

func TestHelloWorld(t *testing.T) {
	v1 := HelloWorld()
	expected := "Hello, World from go.dev"

	if v1 != expected {
		t.Errorf("basic Hello, World test failed v1: %q expected %q", v1, expected)
	}
}

func TestGetTimestampHypens(t *testing.T) {
	timestamp := GetTimestampHypens()

	// Define the regular expression pattern.
	// It checks for the format YYYY-MM-DD-HH-MM-SS
	pattern := `^\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}$`
	regex := regexp.MustCompile(pattern)

	// Check if the timestamp matches the pattern.
	if !regex.MatchString(timestamp) {
		t.Errorf("GetTimestampHypens() returned an invalid format: %s, expected format: YYYY-MM-DD-HH-MM-SS", timestamp)
	}
}

func TestHealthCheck(t *testing.T) {
	v1 := HealthCheck()
	expected := true

	if v1 != expected {
		t.Errorf("basic health check test failed v1: %v expected %v", v1, expected)
	}
}
