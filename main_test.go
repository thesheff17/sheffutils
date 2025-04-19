package main

import (
	"net/http"
	"net/http/httptest"
	"regexp"
	"strings"
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

// TestWebHealthCheck tests the WebHealthCheck function.
func TestWebHealthCheck(t *testing.T) {
	// Create a request to pass to our handler.  Use a dummy URL.
	req, err := http.NewRequest("GET", "/health", nil)
	if err != nil {
		t.Fatal(err) // Use t.Fatal for non-recoverable errors.
	}

	// We create a ResponseRecorder (which satisfies http.ResponseWriter) to record the response.
	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(WebHealthCheck) // Wrap your function with http.HandlerFunc

	// Our handler expects a http.ResponseWriter and http.Request.
	// The ResponseRecorder satisfies http.ResponseWriter.
	handler.ServeHTTP(rr, req)

	// Check the status code.
	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v",
			status, http.StatusOK)
	}

	// Check the response body.
	expectedPrefix := "status: running \ntimestamp: " // Changed to expectedPrefix
	actualBody := rr.Body.String()

	if !strings.HasPrefix(actualBody, expectedPrefix) {
		t.Errorf("handler returned unexpected body: got %v want prefix %v", actualBody, expectedPrefix)
	}
}
