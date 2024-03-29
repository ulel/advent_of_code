package main

import (
	"testing"
)

/*
Each bit in the gamma rate can be determined by finding the most common bit in
the corresponding position of all numbers in the diagnostic report. For
example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven
1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the
second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0,
respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

*/

func TestGetGammaRate(t *testing.T) {
	input := []string{
		"00100",
		"11110",
		"10110",
		"10111",
		"10101",
		"01111",
		"00111",
		"11100",
		"10000",
		"11001",
		"00010",
		"01010",
	}

	expected := uint(22)
	actual, _ := getGammaRate(input)

	if actual != expected {
		t.Errorf("Gamma rate wrong, expected: %b, actual: %b", expected, actual)
	}
}

func TestConvertToGammaRate(t *testing.T) {
	input := []uint{
		7,
		5,
		10,
		4,
		8,
	}

	expected := uint(0b10101)
	lengthOfReport := 10

	actual := convertToGammaRate(input, lengthOfReport)

	if actual != expected {
		t.Errorf("Gamma rate wrong, expected: %b, actual: %b", expected, actual)
	}
}

/*
The epsilon rate is calculated in a similar way; rather than use the most
common bit, the least common bit from each position is used. So, the epsilon
rate is 01001, or 9 in decimal.
*/

func TestGetEpsilonRateFromGammaRate(t *testing.T) {
	input := uint(22)
	expected := uint(9)

	actual := getEpsilonRateFromGammaRate(input, 5)

	if actual != expected {
		t.Errorf("Epsilon rate wrong, expected: %b, actual: %b", expected, actual)
	}
}

func TestGetOxygenGeneratorRating(t *testing.T) {
	input := []string{
		"00100",
		"11110",
		"10110",
		"10111",
		"10101",
		"01111",
		"00111",
		"11100",
		"10000",
		"11001",
		"00010",
		"01010",
	}

	expected := uint(0b10111)

	actual := getOxygenGeneratorRating(input)

	if expected != actual {
		t.Errorf("Oxygen Generator Rating wrong, expected: %b, actual: %b", expected, actual)
	}
}

func TestCo2ScrubberRating(t *testing.T) {
	input := []string{
		"00100",
		"11110",
		"10110",
		"10111",
		"10101",
		"01111",
		"00111",
		"11100",
		"10000",
		"11001",
		"00010",
		"01010",
	}

	expected := uint(0b01010)

	actual := getCo2ScrubberRating(input)

	if expected != actual {
		t.Errorf("Oxygen Generator Rating wrong, expected: %b, actual: %b", expected, actual)
	}
}
