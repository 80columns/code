/*
 * http://projecteuler.net/problem=15
 *
 * Starting in the top left corner of a 2x2 grid, there are 6 routes
 * (without backtracking) to the bottom right corner.
 *
 * http://projecteuler.net/project/images/p_015.gif
 *
 * How many routes are there through a 20x20 grid?
 */

/* Initialize the array */
var GridPoints = new Array(19);
var Answer = 0;

/* Make the array two-dimensional. The first index will
 * reference the column, and the second index will reference
 * the row.
 */
for(var i = 0; i < 19; i++) {
    GridPoints[i] = new Array(20);
}

/* Fill the right-hand column of the array with 1s */
for(var i = 0; i < 20; i++) {
    GridPoints[18][i] = 1;
    Answer += 1;
}

/* Calculate the rest of the array entries. Each array entry X is
 * equal to the sum of the entry to its right Y plus all entries
 * below entry Y that are in the same column as Y. Variable i is
 * the column and variable j is the row. The array is filled one
 * column at a time right-to-left and top-to-bottom.
 */
for(var i = 17; i >= 0; i--) {
    for(var j = 0; j < 20; j++) {
        var Sum = 0;

        for(var k = j; k < 20; k++) {
            Sum += GridPoints[i+1][k];
        }

        GridPoints[i][j] = Sum;
        Answer += Sum;
    }
}

/* Increment by 1 to account for the path that goes from the top
 * left corner to the top right corner and then to the bottom right
 * corner
 */
Answer += 1;

/* Multiply by 2 as the paths that we have found travel right and
 * then down. There are an equal number of paths that travel down
 * and then right, because if you flip the grid from the top right
 * corner to the bottom left corner then the paths match.
 */
Answer *= 2;

document.write(Answer);
