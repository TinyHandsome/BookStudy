package main

import "testing"

func TestAdd(t *testing.T) {
	res := Add(2, 2)
	if res != 3 {
		t.Fatalf("res should be 3")
	}

	t.Logf("正确")
}
