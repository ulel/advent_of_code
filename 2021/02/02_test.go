package main

import (
	"bytes"
	"testing"
)

func TestParseCommands(t *testing.T) {
	expected := []command{
		command{direction: "forward", units: 5},
		command{direction: "down", units: 5},
		command{direction: "forward", units: 8},
		command{direction: "up", units: 3},
		command{direction: "down", units: 8},
		command{direction: "forward", units: 2},
	}

	var buffer bytes.Buffer
	buffer.WriteString("forward 5\n")
	buffer.WriteString("down 5\n")
	buffer.WriteString("forward 8\n")
	buffer.WriteString("up 3\n")
	buffer.WriteString("down 8\n")
	buffer.WriteString("forward 2\n")

	actual := parseCommands(&buffer)

	checkSlicesEqual(expected, actual, t)
}

func checkSlicesEqual(expected, actual []command, t *testing.T) {
	if len(expected) != len(actual) {
		t.Errorf("Slice have wrong size, expected: %d, actual: %d", len(expected), len(actual))
		return
	}

	for i, value := range expected {
		if value != actual[i] {
			t.Errorf("Unexpected valua at %d, expected: %+v, actual: %+v", i, expected, actual)
		}
	}
}

/*
Your horizontal position and depth both start at 0. The steps above would then
modify them as follows:

    forward 5 adds 5 to your horizontal position, a total of 5.
    down 5 adds 5 to your depth, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13.
    up 3 decreases your depth by 3, resulting in a value of 2.
    down 8 adds 8 to your depth, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15.

After following these instructions, you would have a horizontal position of 15
and a depth of 10. (Multiplying these together produces 150.)
*/
func TestGetFinalPosition(t *testing.T) {
	input := []command{
		command{direction: "forward", units: 5},
		command{direction: "down", units: 5},
		command{direction: "forward", units: 8},
		command{direction: "up", units: 3},
		command{direction: "down", units: 8},
		command{direction: "forward", units: 2},
	}

	expectedHorizontal := 15
	expectedDepth := 10

	actualHorizontal, actualDepth := getFinalPosition(input)

	if expectedHorizontal != actualHorizontal {
		t.Errorf("Horizontal position wrong, want: %d, got: %d", expectedHorizontal, actualHorizontal)
	}

	if expectedDepth != actualDepth {
		t.Errorf("Depth position wrong, want: %d, got: %d", expectedDepth, actualDepth)
	}
}

/*
Now, the above example does something different:

    forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
    down 5 adds 5 to your aim, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
    up 3 decreases your aim by 3, resulting in a value of 2.
    down 8 adds 8 to your aim, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.

After following these new instructions, you would have a horizontal position of
15 and a depth of 60. (Multiplying these produces 900.)
*/
func TestFinalPositionWithAim(t *testing.T) {
	input := []command{
		command{direction: "forward", units: 5},
		command{direction: "down", units: 5},
		command{direction: "forward", units: 8},
		command{direction: "up", units: 3},
		command{direction: "down", units: 8},
		command{direction: "forward", units: 2},
	}

	expectedHorizontal := 15
	expectedDepth := 60

	actualHorizontal, actualDepth := getFinalPositionWithAim(input)

	if expectedHorizontal != actualHorizontal {
		t.Errorf("Horizontal position wrong, want: %d, got: %d", expectedHorizontal, actualHorizontal)
	}

	if expectedDepth != actualDepth {
		t.Errorf("Depth position wrong, want: %d, got: %d", expectedDepth, actualDepth)
	}
}
