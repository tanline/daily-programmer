package main

import (
	"fmt"
	"os"
	"strconv"
)

func sumDigits(x string) string {
	var sum = 0
	strLen := len(x)

    // Return string if only one digit
	if strLen < 2 {
		return x
	}

	fmt.Println(x)
    // Convert string to integer
	num, _ := strconv.Atoi(x)

    // Sum up the digits of the integer
	for strLen > 0 {
		sum += num % 10
		num = num / 10
		strLen -= 1
	}

    // Convert to string and repeat
	return sumDigits(strconv.Itoa(sum))
}

func main() {
	fmt.Println(sumDigits(os.Args[1]))
}
