package main

import (
	"testing"
)

/*
For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263

This report indicates that, scanning outward from the submarine, the sonar
sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases,
just so you know what you're dealing with - you never know if the keys will get
carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the
previous measurement. (There is no measurement before the first measurement.)
In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

In this example, there are 7 measurements that are larger than the previous
measurement.
*/

func TestNumberTimesTheDepthIncreases(t *testing.T) {

	expected := 7
	depthMeasurements := []int{
		199,
		200,
		208,
		210,
		200,
		207,
		240,
		269,
		260,
		263,
	}

	total := NumberTimesTheDepthIncreases(depthMeasurements)

	if total != expected {
		t.Errorf("Sum was incorrect, got: %d, want: %d.", total, expected)
	}
}

/*
In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
*/
func TestGroupByThree(t *testing.T) {
	expected := []int{
		607,
		618,
		618,
		617,
		647,
		716,
		769,
		792,
	}

	depthMeasurements := []int{
		199,
		200,
		208,
		210,
		200,
		207,
		240,
		269,
		260,
		263,
	}

	actual := GroupByThree(depthMeasurements)

	if !slicesEqual(actual, expected) {
		t.Errorf("Group sum was incorrect, got: %d, want: %d.", actual, expected)
	}
}

func slicesEqual(sliceA, sliceB []int) bool {
	if len(sliceA) != len(sliceB) {
		return false
	}

	for i, value := range sliceA {
		if value != sliceB[i] {
			return false
		}
	}

	return true
}

func TestSumSlice(t *testing.T) {
	slice := []int{1, 2, 3}
	expected := 1 + 2 + 3
	actual := SumSlice(slice)

	if actual != expected {
		t.Errorf("Sum of slice incorrect, got: %d, want: %d.", actual, expected)
	}
}

func TestNumberOfTimesGroupedByThree(t *testing.T) {

	depthMeasurements := []int{
		199,
		200,
		208,
		210,
		200,
		207,
		240,
		269,
		260,
		263,
	}

	expected := 5
	actual := NumberOfTimesGroupedByThree(depthMeasurements)

	if actual != expected {
		t.Errorf("Number of times incorrect, got: %d, want: %d.", actual, expected)
	}
}
