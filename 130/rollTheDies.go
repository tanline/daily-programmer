/*
 * Dice Roller
 * by: Tanpreet Grewal
 *
 * Accepts input from command line in the form of "NdM"
 * where M is the number of sides on the die, and
 * where N is the number of rolls to be completed
 *
 * Prints a list of integers
 *
 */

package main

import (
    "fmt"
    "os"
    "strconv"
    "strings"
    "math/rand"
    "time"
)

func rollDie(rollStr, dieStr string) {
    // Convert input strings into appropriate integer values
    rolls, _ := strconv.Atoi(rollStr)
    die, _ := strconv.Atoi(dieStr)

    // Seed random number generator
    r := rand.New(rand.NewSource(time.Now().UnixNano()))

    // Roll the dice
    for i := 0; i < rolls; i++ {
        fmt.Println(r.Intn(die)+1)
    }
}

func main() {
    // Seperate input by the letter 'd'
    roll := strings.Split(os.Args[1],"d")
    rollDie(roll[0], roll[1])
}
