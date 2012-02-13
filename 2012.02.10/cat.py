#!/usr/bin/env python3.2


import sys
import fileinput
import getopt
import math
import mmap


#==============================================================================#
# ================================= Version ================================== #
#==============================================================================#
def Version():
    '''
        [ sys.stdout +:= "PyCat v1.0" ]
    '''

    print("PyCat v1.0")
#==============================================================================#


#==============================================================================#
# ================================= Help ===================================== #
#==============================================================================#
def Help():
    '''
        [ sys.stdout +:= "PyCat v1.0\n" +
                         "Usage: pycat [OPTIONS] [FILE]\n" +
                         "Concatenate FILE(S) to standard output.\n\n" +
                         "-b\t\tnumber nonempty output lines, overrides -n\n" +
                         "-E\t\tdisplay $ at the end of each line\n" +
                         "-n\t\tnumber all output lines\n" +
                         "-s\t\tsuppress repeated empty output lines\n" ]
    '''

    print("PyCat v1.0")
    print("Usage: pycat [OPTIONS] [FILE]")
    print("Concatenate FILE to standard output.")
    print("")
    print("-b\t\tnumber nonempty output lines, overrides -n")
    print("-E\t\tdisplay $ at the end of each line")
    print("-n\t\tnumber all output lines")
    print("-s\t\tsuppress repeated empty output lines")
#==============================================================================#


#==============================================================================#
# ============================== CountLines ================================== #
#==============================================================================#
def CountLines(FileName):
    '''
        [ Read the number of newlines in the file referenced by FileName
          and return that number ]
    '''

    File = open(FileName, "r+")
    Buffer = mmap.mmap(File.fileno(), 0)
    NumLines = 0
    Readline = Buffer.readline
    while Readline():
        NumLines += 1
    return NumLines
#==============================================================================#


#==============================================================================#
# ========================== NumberNonBlankPrint ============================= #
#==============================================================================#
def NumberNonBlankPrint(Line, ShowEnds, SqueezeBlank, PreviousLineBlank,
                        LineNumber, LineIndent):
    '''
        [ if SqueezeBlank == True and PreviousLineBlank == True and
          len(Line) == 0 ->
              I
          else if ShowEnds == True ->
              if len(Line) == 0 ->
                  PreviousLineBlank := True
                  sys.stdout +:= "$\n"
              else ->
                  PreviousLineBlank := False
                  Temp := 0
                  LinePrefix := At least four spaces
                  LineNumber := LineNumber + 1
                  sys.stdout +:= "LinePrefix LineNumber    Line$\n"
          else ->
              if len(Line) == 0 ->
                  PreviousLineBlank := True
                  sys.stdout +:= "\n"
              else ->
                  PreviousLineBlank := False
                  Temp := 0
                  LinePrefix := At least four spaces
                  LineNumber := LineNumber + 1
                  sys.stdout +:= "LinePrefix LineNumber    Line$\n"
          
          return PreviousLineBlank, LineNumber ]
    '''

    if SqueezeBlank == True and PreviousLineBlank == True and len(Line) == 0:
        pass
    elif ShowEnds == True:
        if len(Line) == 0:
            PreviousLineBlank = True
            sys.stdout.write("$\n")
        else:
            PreviousLineBlank = False
            Temp = LineIndent - math.floor(math.log10(LineNumber))
            LinePrefix = "   "
            while Temp > 0:
                LinePrefix += " "
                Temp -= 1
            sys.stdout.write(LinePrefix + str(LineNumber) + "  " + Line + "$\n")
            LineNumber += 1
    else:
        if len(Line) == 0:
            PreviousLineBlank = True
            sys.stdout.write("\n")
        else:
            PreviousLineBlank = False
            Temp = LineIndent - math.floor(math.log10(LineNumber))
            LinePrefix = "   "
            while Temp > 0:
                LinePrefix += " "
                Temp -= 1
            sys.stdout.write(LinePrefix + str(LineNumber) + "  " + Line + "\n")
            LineNumber += 1

    return PreviousLineBlank, LineNumber

#==============================================================================#


#==============================================================================#
# ============================== NumberAllPrint ============================== #
#==============================================================================#
def NumberAllPrint(Line, ShowEnds, SqueezeBlank, PreviousLineBlank, LineNumber,
                   LineIndent):
    '''
        [ if SqueezeBlank == True and PreviousLineBlank == True and
          len(Line) == 0 ->
              I
          else if ShowEnds == True ->
              if len(Line) == 0 ->
                  PreviousLineBlank := True
                  LineNumber := LineNumber + 1
                  sys.stdout +:= "LinePrefix LineNumber    Line$\n"
              else ->
                  PreviousLineBlank := False
                  LineNumber := LineNumber + 1
                  sys.stdout +:= "LinePrefix LineNumber    Line$\n"
          else ->
              if len(Line) == 0 ->
                  PreviousLineBlank := True
                  LineNumber := LineNumber + 1
                  sys.stdout +:= "LinePrefix LineNumber    \n"
              else ->
                  PreviousLineBlank := False
                  LineNumber := LineNumber + 1
                  sys.stdout +:= "LinePrefix LineNumber    Line\n"

          return PreviousLineBlank, LineNumber ]
    '''

    Temp = LineIndent - math.floor(math.log10(LineNumber))
    LinePrefix = "   "
    while Temp > 0:
        LinePrefix += " " 
        Temp -= 1

    if SqueezeBlank == True and PreviousLineBlank == True and len(Line) == 0:
        pass
    elif ShowEnds == True:
        if len(Line) == 0:
            PreviousLineBlank = True
            sys.stdout.write(LinePrefix + str(LineNumber) + "  " + "$\n")
            LineNumber += 1
        else:
            PreviousLineBlank = False
            sys.stdout.write(LinePrefix + str(LineNumber) + "  " + Line + "$\n")
            LineNumber += 1
    else:
        if len(Line) == 0:
            PreviousLineBlank = True
            sys.stdout.write(LinePrefix + str(LineNumber) + "  " + "\n")
            LineNumber += 1
        else:
            PreviousLineBlank = False
            sys.stdout.write(LinePrefix + str(LineNumber) + "  " + Line + "\n")
            LineNumber += 1

    return PreviousLineBlank, LineNumber
#==============================================================================#


#==============================================================================#
# ============================ NoNumberPrint ================================= #
#==============================================================================#
def NoNumberPrint(Line, ShowEnds, SqueezeBlank, PreviousLineBlank):
    '''
        [ if SqueezeBlank == True and PreviousLineBlank == True and
          len(Line) == 0 ->
              I
          else if ShowEnds == True ->
              if len(Line) == 0 ->
                  PreviousLineBlank := True
                  sys.stdout +:= "$\n"
              else ->
                  PreviousLineBlank := False
                  sys.stdout +:= "Line$\n"
          else ->
              if len(Line) == 0 ->
                  PreviousLineBlank := True
                  sys.stdout +:= "\n"
              else ->
                  PreviousLineBlank := False
                  sys.stdout +:= "Line\n"

          return PreviousLineBlank ]
    '''

    if SqueezeBlank == True and PreviousLineBlank == True and len(Line) == 0:
        pass

    elif ShowEnds == True:
        if len(Line) == 0:
            PreviousLineBlank = True
            sys.stdout.write("$\n")
        else:
            PreviousLineBlank = False
            sys.stdout.write(Line + "$\n")
    else:
        if len(Line) == 0:
            PreviousLineBlank = True
            sys.stdout.write("\n")
        else:
            PreviousLineBlank = False
            sys.stdout.write(Line + "\n")

    return PreviousLineBlank
#==============================================================================#


#==============================================================================#
# ================================= ProcessLine ============================== #
#==============================================================================#
def ProcessLine(Line, NumberAll, ShowEnds, SqueezeBlank, NumberNonblank,
                PreviousLineBlank, LineNumber, LineIndent):
    '''
        [ if NumberNonblank == True ->
              PreviousLineBlank, LineNumber =
                  NumberNonblankPrint(Line, ShowEnds, SqueezeBlank,
                                      PreviousLineBlank, LineNumber, LineIndent)
          else if NumberAll == True ->
              PreviousLineBlank, LineNumber = NumberAllPrint(Line, ShowEnds,
                                                             SqueezeBlank,
                                                             PreviousLineBlank,
                                                             LineNumber,
                                                             LineIndent)
          else ->
              PreviousLineBlank = NoNumberPrint(Line, ShowEnds,
                                                SqueezeBlank,
                                                PreviousLineBlank,
                                                LineNumber)
          return PreviousLineBlank, LineNumber ]
    '''

    if NumberNonblank == True:
        # [ if SqueezeBlank == True and PreviousLineBlank == True and
        #   len(Line) == 0 ->
        #       I
        #   else if ShowEnds == True ->
        #       if len(Line) == 0 ->
        #           PreviousLineBlank := True
        #           sys.stdout +:= "$\n"
        #       else ->
        #           PreviousLineBlank := False
        #           Temp := 0
        #           LinePrefix := At least four spaces
        #           LineNumber := LineNumber + 1
        #           sys.stdout +:= "LinePrefix LineNumber    Line$\n"
        #   else ->
        #       if len(Line) == 0 ->
        #           PreviousLineBlank := True
        #           sys.stdout +:= "\n"
        #       else ->
        #           PreviousLineBlank := False
        #           Temp := 0
        #           LinePrefix := At least four spaces
        #           LineNumber := LineNumber + 1
        #           sys.stdout +:= "LinePrefix LineNumber    Line$\n"
        #
        #   return PreviousLineBlank, LineNumber ]
        PreviousLineBlank, LineNumber = NumberNonBlankPrint(Line, ShowEnds,
                                                            SqueezeBlank,
                                                            PreviousLineBlank,
                                                            LineNumber,
                                                            LineIndent)
    elif NumberAll == True:
        # [ if SqueezeBlank == True and PreviousLineBlank == True and
        #   len(Line) == 0 ->
        #       I
        #   else if ShowEnds == True ->
        #       if len(Line) == 0 ->
        #           PreviousLineBlank := True
        #           LineNumber := LineNumber + 1
        #           sys.stdout +:= "LinePrefix LineNumber    Line$\n"
        #       else ->
        #           PreviousLineBlank := False
        #           LineNumber := LineNumber + 1
        #           sys.stdout +:= "LinePrefix LineNumber    Line$\n"
        #   else ->
        #       if len(Line) == 0 ->
        #           PreviousLineBlank := True
        #           LineNumber := LineNumber + 1
        #           sys.stdout +:= "LinePrefix LineNumber    \n"
        #       else ->
        #           PreviousLineBlank := False
        #           LineNumber := LineNumber + 1
        #           sys.stdout +:= "LinePrefix LineNumber    Line\n"
        #
        #   return PreviousLineBlank, LineNumber ]
        PreviousLineBlank, LineNumber = NumberAllPrint(Line, ShowEnds,
                                                       SqueezeBlank,
                                                       PreviousLineBlank,
                                                       LineNumber,
                                                       LineIndent)
    else:
        # [ if SqueezeBlank == True and PreviousLineBlank == True and
        #   len(Line) == 0 ->
        #       I
        #   else if ShowEnds == True ->
        #       if len(Line) == 0 ->
        #           PreviousLineBlank := True
        #           sys.stdout +:= "$\n"
        #       else ->
        #           PreviousLineBlank := False
        #           sys.stdout +:= "Line$\n"
        #   else ->
        #       if len(Line) == 0 ->
        #           PreviousLineBlank := True
        #           sys.stdout +:= "\n"
        #       else ->
        #           PreviousLineBlank := False
        #           sys.stdout +:= "Line\n"
        #
        #   return PreviousLineBlank ]
        PreviousLineBlank = NoNumberPrint(Line, ShowEnds, SqueezeBlank,
                                          PreviousLineBlank)

    return PreviousLineBlank, LineNumber
#==============================================================================#


#==============================================================================#
# ================================= Main ===================================== #
#==============================================================================#
def main():
    '''
        [ Read in options and the name of a file from the command line,
          then read the contents of the file and print it line-by-line
          with extra information if specified by the command line
          options ]
    '''

    # [ Set initial values for the program ->
    #       PreviousLineBlank = False
    #       NumberAll = False
    #       ShowEnds = False
    #       SqueezeBlank = False
    #       NumberNonblank = False
    #       LineNumber = 0
    #       LineIndent = "" ]
    PreviousLineBlank = False
    NumberAll = False
    ShowEnds = False
    SqueezeBlank = False
    NumberNonblank = False
    LineNumber = 0
    LineIndent = ""

    # [ if -v or --version is present ->
    #       sys.stdout +:= Version message
    #       Exit program
    #   else if -h or --help is present ->
    #       sys.stdout +:= Help message
    #       Exit program
    #   else if -n is present ->
    #       NumberAll = True
    #       LineNumber = 1
    #   else if -E is present ->
    #       ShowEnds = True
    #   else if -s is present ->
    #       SqueezeBlank = True
    #       PreviousLineBlank = False
    #   else if -b is present ->
    #       NumberNonblank = True
    #       LineNumber = 1
    #       NumberAll = False ]
    Opts = getopt.getopt(sys.argv[1:], 'nEsbvh', ['version', 'help'])
    Opts = Opts[0]
    for opt in Opts:
        if '-v' in opt or '--version' in opt:
            Version()
            sys.exit(0)
        elif '-h' in opt or '--help' in opt:
            Help()
            sys.exit(0)
        elif '-n' in opt:
            NumberAll = True
            LineNumber = 1
        elif '-E' in opt:
            ShowEnds = True
        elif '-s' in opt:
            SqueezeBlank = True
        elif '-b' in opt:
            NumberNonblank = True
            LineNumber = 1
        else:
            pass

    if NumberNonblank == True:
        NumberAll = False

    # [ Read the number of newlines in the file referenced by sys.argv[1]
    #   and return that number ]
    NumLines = CountLines(sys.argv[len(sys.argv) - 1])

    # [ Take the log base 10 of NumLines and put the result in NumSpace ]
    LineIndent = math.log10(NumLines)

    # [ Iterate over the lines in the input file, and for
    #   each line in the file pass it to ProcessLine() ]
    for Line in fileinput.input([sys.argv[len(sys.argv) - 1]]):
        # [ Take a string as input with all options ->
        #       if NumberNonblank == True ->
        #           PreviousLineBlank, LineNumber =
        #               NumberNonblankPrint(Line, ShowEnds, SqueezeBlank,
        #                                   PreviousLineBlank, LineNumber,
        #                                   LineIndent)
        #       else if NumberAll == True ->
        #           PreviousLineBlank, LineNumber =
        #               NumberAllPrint(Line, ShowEnds, SqueezeBlank,
        #                              PreviousLineBlank, LineNumber,
        #                              LineIndent)
        #       else ->
        #           PreviousLineBlank = NoNumberPrint(Line, ShowEnds,
        #                                             SqueezeBlank,
        #                                             PreviousLineBlank,
        #                                             LineNumber, LineIndent)
        #       return PreviousLineBlank, LineNumber ]
        Line = Line.strip('\n')
        PreviousLineBlank, LineNumber = ProcessLine(Line, NumberAll, ShowEnds,
                                                    SqueezeBlank,
                                                    NumberNonblank,
                                                    PreviousLineBlank,
                                                    LineNumber, LineIndent)

    # [ Exit the program, returning an exit status of 0 to the shell ]
    sys.exit(0)
#==============================================================================#


if __name__ == "__main__":
    main()
