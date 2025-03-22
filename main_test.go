package main

import "testing"

func TestHelloWorld(t *testing.T) {
	v1 := HelloWorld()
	expected := "Hello, World from go.dev"

	if v1 != expected {
		t.Errorf("basic Hello, World test failed v1: %q expected %q", v1, expected)
	}
}
