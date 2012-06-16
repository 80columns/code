package main

import (
        "os"
        "fmt"
        "strconv"
        "math/rand"
        "time"
)

func Concatenate(Lower []int, Pivot int, Higher []int) []int {
    var NumberList = make([]int, len(Lower) + len(Higher) + 1)
    var NumberListIndex int = 0
    var Index int = 0

    /* Concatenate the lower list to the number list */
    for Index = 0; Index < len(Lower); Index++ {
        NumberList[NumberListIndex] = Lower[Index]
        NumberListIndex++
    }

    /* Concatenate the pivot to the number list */
    NumberList[NumberListIndex] = Pivot
    NumberListIndex++

    /* Concatenate the higher list to the number list */
    for Index = 0; Index < len(Higher); Index++ {
        NumberList[NumberListIndex] = Higher[Index]
        NumberListIndex++
    }

    /* Return the number list */
    return NumberList
}

func Partition(NumberList []int) ([]int, int, []int) {
    var Pivot int
    var Lower = make([]int, 0)
    var Higher = make([]int, 0)
    var Random int

    /* Seed the random number generator with the time in nanoseconds */
    rand.Seed(time.Now().UnixNano())

    /* Get a random number */
    Random = rand.Int()

    /* Get the random number mod the list length so that it
     * represends a list index */
    Random = Random % (len(NumberList) - 1)

    /* Get the pivot from a random location in the number list */
    Pivot = NumberList[Random]

    /* Sort the numbers into two lists, one with numbers higher
     * than the pivot, and one with numbers lower than the pivot */
    for Index := 0; Index < len(NumberList); Index++ {
        if NumberList[Index] < Pivot {
            Lower = append(Lower, NumberList[Index])
        }else if NumberList[Index] > Pivot {
            Higher = append(Higher, NumberList[Index])
        }
    }

    /* Return the lower list, the pivot, and the higher list */
    return Lower, Pivot, Higher
}

func Quicksort(NumberList []int) []int {
    var Pivot int
    var Lower []int
    var Higher []int

    /* If the length of this number list is 1 or 0, return it */
    if len(NumberList) <= 1 {
        return NumberList
    }

    /* Split the number list into two parts using a pivot */
    Lower, Pivot, Higher = Partition(NumberList)

    /* Return the concatenated number list using recursion */
    return Concatenate(Quicksort(Lower), Pivot, Quicksort(Higher))
}

func main() {
    /* Get the command line arguments */
    Arguments := os.Args

    /* Create the number list based on the number of arguments */
    var NumberList = make([]int, len(Arguments) - 1)

    /* Get the number list from the command-line arguments */
    for Index := 1; Index < len(Arguments); Index++ {
        Integer, Error := strconv.Atoi(Arguments[Index])

        if Error != nil {
            fmt.Println(Error)
            return
        } else {
            NumberList[Index - 1] = Integer
        }
    }

    /* Sort the number list */
    NumberList = Quicksort(NumberList)

    /* Print the sorted number list */
    fmt.Println(NumberList)

    return
}
