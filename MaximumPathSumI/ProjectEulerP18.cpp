/*
 * http://projecteuler.net/problem=18
 *
 * By starting at the top of the triangle below and moving to adjacent
 * numbers on the row below, the maximum total from top to bottom is
 * 23.
 *
 *                            _3_
 *                           _7_4
 *                           2_4_6
 *                          8 5_9_3
 *
 * That is, 3 + 7 + 4 + 9 = 23.
 * Find the maximum total from top to bottom of the triangle below:
 *
 *                                  75
 *                                95  64
 *                              17  47  82
 *                            18  35  87  10
 *                          20  04  82  47  65
 *                        19  01  23  75  03  34
 *                      88  02  77  73  07  63  67
 *                    99  65  04  28  06  16  70  92
 *                  41  41  26  56  83  40  80  70  33
 *                41  48  72  33  47  32  37  16  94  29
 *              53  71  44  65  25  43  91  52  97  51  14
 *            70  11  33  28  77  73  17  78  39  68  17  57
 *          91  71  52  38  17  14  91  43  58  50  27  29  48
 *        63  66  04  68  89  53  67  30  73  16  69  87  40  31
 *      04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
 *
 * NOTE: As there are only 16384 routes, it is possible to solve this
 * problem by trying every route. However, Problem 67, is the same
 * challenge with a triangle containing one-hundred rows; it cannot be
 * solved by brute force, and requires a clever method! ;o)
 *
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

/* This function recursively calculates the longest path from the base
 * of the triangle to the top. It does this by selecting the larger of
 * the two paths of a node's children and adding the larger sum to the
 * node's value. The triangle is similar to a binary tree, but nodes
 * have children in common so getting the index of a child node in the
 * triangle is different than getting the index of a child node in a
 * binary tree. A two-dimensional vector is used to store the
 * triangle - the first index stores the node's value, the second
 * index stores the vector index of the node's left child, and the
 * third index stores the vector index of the node's right child.
 */
int GetLongestPath(vector< vector<int> > Triangle, int CurrentIndex) {
    /* First check to make sure that the node has children. If it
     * doesn't, then return the node's value. If it does, calculate
     * the longest paths for its two children and then return
     * the value of the longer path plus the node's value.
     */
    if(Triangle[CurrentIndex][1] >= Triangle.size()) {
        return Triangle[CurrentIndex][0];
    }
    else {
        int Path1 = GetLongestPath(Triangle,
                                   Triangle[CurrentIndex][1]);
        int Path2 = GetLongestPath(Triangle,
                                   Triangle[CurrentIndex][2]);

        if(Path1 > Path2) {
            return Path1 + Triangle[CurrentIndex][0];
        }
        else {
            return Path2 + Triangle[CurrentIndex][0];
        }
    }
}

int main() {
    string Line;
    string TokenString;
    ifstream InputFile;
    vector< vector<int> > Triangle;
    const char Delimiter = ' ';
    int Position0 = 0;
    int Position1 = 0;
    int TokenInteger = 0;
    int ChildOffset = 0;

    /* Open the input file */
    InputFile.open("triangle.txt");

    /* Read the numbers in the triangle */
    if(InputFile.is_open()) {
        while(InputFile.good()) {
            getline(InputFile, Line);
            ChildOffset++;

            if(Line.length() == 0) { continue; }
        
            Position0 = 0;
            Position1 = 0;

            /* Pull the numbers out of each line and add them to the
             * vector
             */
            while(Position0 <= Line.length()) {
                /* Find the first instance of the delimiter */
                Position1 = Line.find_first_of(Delimiter, Position0);

                if(Position1 != Position0) {
                    TokenString = Line.substr(Position0,
                                              Position1 - Position0);
                    vector<int> NewRow;
                    Triangle.push_back(NewRow);

                    istringstream(TokenString) >> TokenInteger;
                    Triangle[(int)Triangle.size() - 1].\
                        push_back(TokenInteger);
                    Triangle[(int)Triangle.size() - 1].\
                        push_back((2*((int)Triangle.size() - 1)) + \
                                  ChildOffset);
                    Triangle[(int)Triangle.size() - 1].\
                        push_back((2*((int)Triangle.size() - 1)) + \
                                  ChildOffset + 1);
                    ChildOffset--;
                }

                Position0 = \
                    Line.find_first_not_of(Delimiter, Position1);
            }
        }
    }

    /* Close the input file */
    InputFile.close();

    /* Print the answer */
    cout << GetLongestPath(Triangle, 0) << endl;

    return 0;
}
