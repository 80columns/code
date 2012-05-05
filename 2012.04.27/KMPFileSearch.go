/*
 * Purpose: This program searches one or more input files
 *          for a substring. Each file's contents are printed
 *          to the command line with all occurrences of the
 *          substring in bold. The files are printed in the
 *          order they are specified in the command-line
 *          arguments, and each file's contents are separated
 *          by file names such that it is obvious which file
 *          is which. The program uses the KMP string matching
 *          algorithm to find occurrences of the substring
 *          inside the files.
 *
 * Notes: The format of if/else if/else statements in this
 *        program is not by choice. The Go compiler complains
 *        (i.e., it won't compile the input source and
 *        prints an error) unless they are formatted as:
 *
 *        if cond {
 *            code
 *        } else if cond {
 *            code
 *        } else {
 *            code
 *        }
 *
 *        This makes the code less readable, but maybe the
 *        Go developers did this in order to solve the dangling
 *        else problem present in C/C++/Java.
 */

package main

import (
    "fmt"
    "os"
    "io"
)

/*
 * [ I ]
 */
func KMPSearch(Substring string, FileString string, PrefixArray []int,
               M int) int {

    /* == 1 ==
     * [ I := 0 ]
     */
    I := 0

    /* == 2 ==
     * [ M := anything
     *   I := anything ]
     */
    for M + I < len(FileString) {

        /* == 2 Body ==
         * [ if Substring[I] == FileString[M + I] ->
         *       if I == len(Substring) - 1 ->
         *           return M
         *
         *       else ->
         *           I
         *
         *       In any case ->
         *           I +:= 1
         *
         *   else ->
         *       if PrefixArray[I] > -1 ->
         *           I := PrefixArray[I]
         *
         *       else ->
         *           I := 0
         *
         *       In any case ->
         *           M := M + I - PrefixArray[I] ]
         */
        if Substring[I] == FileString[M + I] {
            if I == (len(Substring) - 1) {
                return M
            }
            I++
        } else {
            M = M + I - PrefixArray[I]

            if PrefixArray[I] > -1 {
                I = PrefixArray[I]
            } else {
                I = 0
            }
        }
    }

    /* == 3 ==
     * [ return -1 ]
     */
    return -1
}

/*
 * [ I ]
 */
func ComputePrefix(Substring string) []int {

    /* == 1 ==
     * [ PrefixArray := an integer array
     *   I := 2
     *   J := 0
     *   PrefixArray[0] := -1 ]
     */
    var PrefixArray = make([]int, len(Substring))
    I := 2
    J := 0
    PrefixArray[0] = -1

    /* == 2 ==
     * [ if len(Substring) > 1 ->
     *       PrefixArray[1] := 0 ]
     */
    if len(Substring) > 1 {
        PrefixArray[1] = 0
    }

    /* == 3 ==
     * [ PrefixArray := PrefixArray with some indices changed
     *   I := anything
     *   J := anything ]
     */
    for I < len(Substring) {

        /* == 3 Body ==
         * [ if Substring[I - 1] == Substring[J] ->
         *       J +:= 1
         *       PrefixArray[I] := J
         *       I +:= 1
         *
         *   else if J > 0 ->
         *       J := PrefixArray[J]
         *
         *   else ->
         *       PrefixArray[I] := 0
         *       I +:= 1 ]
         */
        if Substring[I - 1] == Substring[J] {
            J++
            PrefixArray[I] = J
            I++
        } else if J > 0 {
            J = PrefixArray[J]
        } else {
            PrefixArray[I] = 0
            I++
        }
    }

    /* == 4 ==
     * [ return PrefixArray ]
     */
    return PrefixArray
}

/*
 * [ os.Stdout +:= the following text:
 *                 "Usage: ./SubstringSearch [substring] [file(s)]" ]
 */
func Usage() {

    /*
     * == 1 ==
     * [ os.Stdout +:= the following text:
     *                 "Usage: ./SubstringSearch [substring] [file(s)]"
     *   return ]
     */
    fmt.Println("Usage: ./SubstringSearch [substring] [file(s)]")

    return
}

/*
 * [ os.Stdout +:= the following text:
 *                 "========================================" +
 *                 "========================================\n" +
 *                 "== Begin == " + FileName + " ==\n" +
 *                 "========================================" +
 *                 "========================================\n" ]
 */
func PrintHeader(FileName string) {

    /* == 1 ==
     * [ os.Stdout +:= the following text:
     *                 "========================================" +
     *                 "========================================\n" +
     *                 "== Begin == " + FileName + " ==\n" +
     *                 "========================================" +
     *                 "========================================\n"
     *   return ]
     */
    fmt.Print("========================================")
    fmt.Print("========================================\n")
    fmt.Print("== Begin == ")
    fmt.Print(FileName)
    fmt.Print(" ==\n")
    fmt.Print("========================================")
    fmt.Print("========================================\n")

    return
}

/*
 * [ os.Stdout +:= the following text:
 *                 "========================================" +
 *                 "========================================\n" +
 *                 "== End == " + FileName + " ==\n" +
 *                 "========================================" +
 *                 "========================================\n\n" ]
 */
func PrintFooter(FileName string) {

    /* == 1 ==
     * [ os.Stdout +:= the following text:
     *                 "========================================" +
     *                 "========================================\n" +
     *                 "== End == " + FileName + " ==\n" +
     *                 "========================================" +
     *                 "========================================\n\n"
     *
     *   return ]
     */
    fmt.Print("========================================")
    fmt.Print("========================================\n")
    fmt.Print("== End == ")
    fmt.Print(FileName)
    fmt.Print(" ==\n")
    fmt.Print("========================================")
    fmt.Print("========================================\n\n")

    return
}

/*
 * [ os.Stderr +:= the following text:
 *                 "Program Error: [" + ErrorString + "]" ]
 */
func PrintProgramError(ErrorString string) {

    /* == 1 ==
     * [ os.Stderr +:= the following text:
     *                 "Program Error: [" + ErrorString + "]"
     *   return ]
     */
    fmt.Fprintln(os.Stderr, "Program Error: [" + ErrorString + "]")

    return
}

/*
 * [ os.Stderr +:= the following text:
 *                 "System Error: [" + Error + "]\n" ]
 */
func PrintSystemError(Error error) {

    /* == 1 ==
     * [ os.Stderr +:= the following text:
     *                 "System Error: [" + Error + "]\n"
     *   return ]
     */
    fmt.Fprintf(os.Stderr, "System Error: [%s]\n", Error)

    return
}

/*
 * [ os.Stdout +:= the following text:
 *                 "\033[1m" + Character + "\033[0m" ]
 */
func PrintBoldCharacter(Character []byte) {

    /* == 1 ==
     * [ os.Stdout +:= the following text:
     *                 "\033[1m" + Character + "\033[0m"
     *   return ]
     */
    fmt.Print("\033[1m" + string(Character) + "\033[0m")
    return
}

/*
 * [ os.Stdout +:= the following text:
 *                 The contents of File, with all occurrences of the
 *                 substring in bold ]
 */
func PrintReport(File *os.File, SubstringIndices []int,
                 SubstringLength int) {

    /* == 1 ==
     * [ File := File seek'd to the beginning of its stream ]
     */
    File.Seek(0, 0)

    /* == 2 ==
     * [ Character := a byte array
     *   Index := 0
     *   SubstringIndex := 0
     *   PrintingSubstring := -1
     *   AllSubstringsPrinted := false ]
     */
    var Character = make([]byte, 1)
    var Error error
    Index := 0
    SubstringIndex := 0
    PrintingSubstring := -1
    AllSubstringsPrinted := false

    /* == 3 ==
     * [ if len(SubstringIndices) == 0 ->
     *       AllSubstringsPrinted := true
     *       SubstringIndices := SubstringIndices appended with 0
     *
     *   else ->
     *       AllSubstringsPrinted := false ]
     */
    if len(SubstringIndices) == 0 {
        AllSubstringsPrinted = true
        SubstringIndices = append(SubstringIndices, 0)
    } else {
        AllSubstringsPrinted = false
    }

    /* == 4 ==
     * [ Error := the error that occurred while reading
     *            File, if any
     *   File := File advanced by the number of bytes read ]
     */
    _, Error = File.Read(Character)

    /* == 5 ==
     * [ os.Stdout +:= the following text:
     *                 The contents of File, with all occurrences of the
     *                 substring in bold
     *   AllSubstringsPrinted := true
     *   Index := anything
     *   SubstringIndex := anything
     *   Character := the last byte in File
     *   PrintingSubstring := anything
     *   File := File advanced to the end of its stream
     *   Error := io.EOF ]
     */
    for Error != io.EOF {

        /* == 5 Body ==
         * [ if AllSubstringsPrinted == false AND
         *      Index == SubstringIndices[SubstringIndex] ->
         *       os.Stdout +:= the following text:
         *                     Character in bold font
         *       SubstringIndex +:= 1
         *       PrintingSubstring := 1
         *
         *       if SubstringIndex == len(SubstringIndices) ->
         *           AllSubstringsPrinted := true
         *           SubstringIndex := 0
         *
         *       else ->
         *           I
         *
         *   else ->
         *       if PrintingSubstring != -1 ->
         *           if PrintingSubstring < SubstringLength ->
         *               os.Stdout +:= the following text:
         *                             Character in bold font
         *               PrintingSubstring +:= 1
         *
         *           else ->
         *               PrintingSubstring := -1
         *               os.Stdout +:= the following text:
         *                             Character
         *
         *       else ->
         *           os.Stdout +:= the following text:
         *                         Character
         *
         *   In any case ->
         *       Index +:= 1
         *       Error := the error that occurred while reading File,
         *                if any
         *       File := File advanced by the number of bytes read
         *       Character := the next byte in File ]
         */

        /* == 5.1 ==
         * [ if AllSubstringsPrinted == false AND
         *      Index == SubstringIndices[SubstringIndex] ->
         *       os.Stdout +:= the following text:
         *                     Character in bold font
         *       SubstringIndex := SubstringIndex + 1
         *       PrintingSubstring := 1
         *
         *       if SubstringIndex == len(SubstringIndices) ->
         *           AllSubstringsPrinted := true
         *           SubstringIndex := 0
         *
         *       else ->
         *           I
         *
         *   else ->
         *       if PrintingSubstring != -1 ->
         *           if PrintingSubstring < SubstringLength ->
         *               os.Stdout +:= the following text:
         *                             Character in bold font
         *               PrintingSubstring := PrintingSubstring + 1
         *
         *           else ->
         *               PrintingSubstring := -1
         *               os.Stdout +:= the following text:
         *                             Character
         *
         *       else ->
         *           os.Stdout +:= the following text:
         *                         Character ]
         */
        if AllSubstringsPrinted == false &&
            Index == SubstringIndices[SubstringIndex] {
            PrintBoldCharacter(Character)
            SubstringIndex++
            PrintingSubstring = 1

            if SubstringIndex == len(SubstringIndices) {
                AllSubstringsPrinted = true
                SubstringIndex = 0
            }
        } else {
            if PrintingSubstring != -1 {
                if PrintingSubstring < SubstringLength {
                    PrintBoldCharacter(Character)
                    PrintingSubstring++
                } else {
                    PrintingSubstring = -1
                    fmt.Print(string(Character))
                }
            } else {
                fmt.Print(string(Character))
            }
        }

        /* == 5.2 ==
         * [ Index +:= 1
         *   Error := the error that occurred while reading
         *            File, if any
         *   File := File advanced by the number of bytes read
         *   Character := the next byte in File ]
         */
        Index++
        _, Error = File.Read(Character)
    }

    /* == 6 ==
     * [ return ]
     */
    return
}

/*
 * [ I ]
 */
func OpenFile(FileName string) *os.File {

    /* == 1 ==
     * [ File := a file pointer to the file located at FileName
     *   Error := the error that occurred while opening FileName, if any ]
     */
    File, OpenError := os.Open(FileName)

    /* == 2 ==
     * [ if Error != nil ->
     *       os.Stderr +:= the following text:
     *                     "System Error: [" + OpenError + "]\n" +
     *                     "Program Error: [" + "The file " + FileName +
     *                     " could not be opened for reading" + "]\n"
     *       File := nil
     *
     *   else ->
     *       I ]
     */
    if OpenError != nil {
        PrintSystemError(OpenError)
        PrintProgramError("The file " + FileName +
                   " could not be opened for reading")
        File = nil
    }

    /* == 3 ==
     * [ return File ]
     */
    return File
}

/*
 * [ os.Stdout +:= the following text:
 *                 "========================================" +
 *                 "========================================\n" +
 *                 "== Begin == " + FileName + " ==\n" +
 *                 "========================================" +
 *                 "========================================\n" +
 *                 The contents of File, with all occurrences of
 *                 Substring in bold +
 *                 "========================================" +
 *                 "========================================\n" +
 *                 "== End == " + FileName + " ==\n" +
 *                 "========================================" +
 *                 "========================================\n\n"
 *
 *   os.Stderr +:= for each file read error that occurs, the following
 *                 text:
 *                 "System Error: [" + (error) + "]\n" +
 *                 "Program Error: [" +
 *                 "Error reading from file " + FileName +
 *                 "]\n" ]
 */
func ProcessFile(Substring string, FileName string) {

    /* == 1 ==
     * [ File := a file pointer to the file located at FileName ]
     */
    File := OpenFile(FileName)

    /* == 2 ==
     * [ if File == nil ->
     *       return
     *
     *   else ->
     *       I ]
     */
    if File == nil {
        return
    }

    /* == 3 ==
     * [ PrefixArray := an integer array
     *   FileBytes := a byte array
     *   TestByte := a byte array
     *   SubstringIndices := an integer array
     *   BytesRead := 0
     *   FileString := anything
     *   ReadError := anything
     *   Index := 0
     *   M := 0
     *   CurrentFileOffset := 0
     *   ReadingFile := true ]
     */
    PrefixArray := ComputePrefix(Substring)
    var FileBytes = make([]byte, 512)
    var TestByte = make([]byte, 1)
    var SubstringIndices = make([]int, 0)
    var BytesRead int
    var FileString string
    var ReadError error
    var EOFTestError error
    Index := 0
    M := 0
    CurrentFileOffset := 0
    ReadingFile := true

    /* == 4 ==
     * [ ReadingFile := false
     *   ReadError := anything
     *   File := File advanced to the end of its stream
     *   FileBytes := FileBytes with some indices changed
     *   BytesRead := anything
     *   M := anything
     *   Index := anything
     *   CurrentFileOffset := anything
     *   TestByte := TestByte with some indices changed
     *   FileString := anything
     *   SubstringIndices := SubstringIndices with some indices changed ]
     */
    for ReadingFile == true {

        /* == 4 Body ==
         * [ if ReadError != nil ->
         *       os.Stderr +:= the following text:
         *                     "System Error: [" + ReadError + "]\n" +
         *                     "Program Error: [" +
         *                     "Error reading from file " + FileName +
         *                     "]\n"
         *
         *   else ->
         *       I
         *
         *   if EOFTestError != io.EOF AND EOFTestError != nil ->
         *       os.Stderr +:= the following text:
         *                     "System Error: [" + EOFTestError + "]\n" +
         *                     "Program Error: [" +
         *                     "Error reading from file " + FileName +
         *                     "]\n"
         *
         *   else if EOFTestError == io.EOF ->
         *       ReadingFile := false
         *
         *   else ->
         *       File := File seek'd backward by len(Substring) bytes
         *
         *   In any case ->
         *       BytesRead := the number of bytes read from File
         *       ReadError := the error that occurred while reading File,
         *                    if any
         *       EOFTestError := the error that occurred while reading
         *                       File, if any
         *       File := File advanced to a new, positive offset
         *       FileBytes := the bytes read from File
         *       TestByte := a byte read from File
         *       FileString := FileBytes converted to a string
         *       SubstringIndices := SubstringIndices with some indices changed
         *       Index := 0
         *       M := 0
         *       CurrentFileOffset := anything ]
         */

        /* == 4.1 ==
         * [ BytesRead := the number of bytes read from File
         *   ReadError := the error that occurred while reading File,
         *                if any
         *   File := File advanced by BytesRead bytes
         *   FileBytes := the bytes read from File
         *   FileString := FileBytes converted to a string ]
         */
        BytesRead, ReadError = File.Read(FileBytes)
        FileString = string(FileBytes)

        /* == 4.2 ==
         * [ if ReadError != nil ->
         *       os.Stderr +:= the following text:
         *                     "System Error: [" + ReadError + "]\n" +
         *                     "Program Error: [" +
         *                     "Error reading from file " + FileName +
         *                     "]\n"
         *
         *   else ->
         *       I ]
         */
        if ReadError != nil {
            PrintSystemError(ReadError)
            PrintProgramError("Error reading from file " + FileName)
        }

        /* == 4.3 ==
         * [ EOFTestError := the error that occurred while reading File,
         *                   if any
         *   File := File advanced by one byte
         *   TestByte := the byte read from File ]
         */
        _, EOFTestError = File.Read(TestByte)

        /* == 4.4 ==
         * [ if EOFTestError != io.EOF AND EOFTestError != nil ->
         *       os.Stderr +:= the following text:
         *                     "System Error: [" + EOFTestError + "]\n" +
         *                     "Program Error: [" +
         *                     "Error reading from file " + FileName +
         *                     "]\n"
         *
         *   else if EOFTestError == io.EOF ->
         *       ReadingFile := false
         *
         *   else ->
         *       File := File seek'd backward by len(Substring) bytes ]
         */
        if EOFTestError != io.EOF && EOFTestError != nil {
            PrintSystemError(EOFTestError)
            PrintProgramError("Error reading from file " + FileName)
        } else if EOFTestError == io.EOF {
            ReadingFile = false
        } else {
            File.Seek(int64(-len(Substring)), 1)
        }

        /* == 4.5 ==
         * [ Index := -1
         *   SubstringIndices := SubstringIndices with some indices changed
         *   M := anything ]
         */
        for Index != -1 {

            /* == 4.5 Body ==
             * [ if Index != -1 ->
             *       SubstringIndices := SubstringIndices with some indices
             *                           changed
             *
             *   else ->
             *       I
             *
             *   In any case ->
             *       Index := anything
             *       M := anything ]
             */

            /* == 4.5.1 ==
             * [ Index := anything ]
             */
            Index = KMPSearch(Substring, FileString, PrefixArray, M)

            /* == 4.5.2 ==
             * [ if Index != -1 ->
             *       SubstringIndices := SubstringIndices with some indices
             *                           changed
             *
             *   else ->
             *       I ]
             */
            if Index != -1 {
                SubstringIndices = append(SubstringIndices,
                                          Index + CurrentFileOffset)
            }

            /* == 4.5.3 ==
             * [ M := anything ]
             */
            M = Index + 1
        }

        /* == 4.6 ==
         * [ Index := 0
         *   M := 0
         *   CurrentFileOffset := anything ]
         */
        Index = 0
        M = 0
        CurrentFileOffset += 1 + BytesRead - len(Substring)
    }

    /* == 5 ==
     * [ os.Stdout +:= the following text:
     *                 "========================================" +
     *                 "========================================\n" +
     *                 "== Begin == " + FileName + " ==\n" +
     *                 "========================================" +
     *                 "========================================\n" +
     *                 The contents of File, with all occurrences of
     *                 Substring in bold +
     *                 "========================================" +
     *                 "========================================\n" +
     *                 "== End == " + FileName + " ==\n" +
     *                 "========================================" +
     *                 "========================================\n\n" ]
     */
    PrintHeader(FileName)
    PrintReport(File, SubstringIndices, len(Substring))
    PrintFooter(FileName)

    /* == 6 ==
     * [ File := anything ]
     */
    File.Close()

    /* == 7 ==
     * [ return ]
     */
    return
}

/*
 * [ if len(os.Args) < 3 ->
 *       os.Stderr +:= the following text:
 *                     "Program Error: [" +
 *                     "Supply at least two arguments" +
 *                     "]\n"
 *
 *       os.Stdout +:= the following text:
 *                     "Usage: ./SubstringSearch [substring] [file(s)]"
 *
 *   else ->
 *       os.Stdout +:= for each input file specified in the command
 *                     line arguments that could be successfully
 *                     opened, the following text:
 *                     "========================================" +
 *                     "========================================\n" +
 *                     "== Begin == " + (file name) + " ==\n" +
 *                     "========================================" +
 *                     "========================================\n" +
 *                     The contents of the file, with all occurrences of
 *                     the substring in bold +
 *                     "========================================" +
 *                     "========================================\n" +
 *                     "== End == " + (file name) + " ==\n" +
 *                     "========================================" +
 *                     "========================================\n\n"
 *
 *       os.Stderr +:= for each file specified in the command line
 *                     arguments that could not be successfully
 *                     opened, the following text:
 *                     "System Error: [" + (error) + "]\n" +
 *                     "Program Error: [" + "The file " + (file name) +
 *                     " could not be opened for reading" + "]\n"
 *
 *                     for each read error that occurs in each file
 *                     specified in the command line arguments, the
 *                     following text:
 *                     "System Error: [" + (error) + "]\n" +
 *                     "Program Error: [" +
 *                     "Error reading from file " + (file name) +
 *                     "]\n" ]
 */
func main() {

    /* == 1 ==
     * [ if len(os.Args) < 3 ->
     *       os.Stderr +:= the following text:
     *                     "Program Error: [" +
     *                     "Supply at least two arguments" +
     *                     "]\n"
     *
     *       os.Stdout +:= the following text:
     *                     "Usage: ./SubstringSearch [substring] [file(s)]"
     *       return
     *
     *   else ->
     *       I ]
     */
    if len(os.Args) < 3 {
        PrintProgramError("Supply at least two arguments")
        Usage()
        return
    }

    /* == 2 ==
     * [ Substring := os.Args[1] ]
     */
    Substring := os.Args[1]

    /* == 3 ==
     * [ os.Stdout +:= for each input file specified in the command
     *                 line arguments that could be successfully
     *                 opened, the following text:
     *                 "========================================" +
     *                 "========================================\n" +
     *                 "== Begin == " + (file name) + " ==\n" +
     *                 "========================================" +
     *                 "========================================\n" +
     *                 The contents of the file, with all occurrences of
     *                 Substring in bold +
     *                 "========================================" +
     *                 "========================================\n" +
     *                 "== End == " + (file name) + " ==\n" +
     *                 "========================================" +
     *                 "========================================\n\n"
     *                 
     *   os.Stderr +:= for each file specified in the command line
     *                 arguments that could not be successfully
     *                 opened, the following text:
     *                 "System Error: [" + (error) + "]\n" +
     *                 "Program Error: [" + "The file " + (file name) +
     *                 " could not be opened for reading" + "]\n"
     *
     *                 for each read error that occurs in each file
     *                 specified in the command line arguments, the
     *                 following text:
     *                 "System Error: [" + (error) + "]\n" +
     *                 "Program Error: [" +
     *                 "Error reading from file " + (file name) +
     *                 "]\n" ]
     */
    for Index := 2; Index < len(os.Args); Index++ {
        ProcessFile(Substring, os.Args[Index])
    }

    /* == 4 ==
     * [ return ]
     */
    return
}
