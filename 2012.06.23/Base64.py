#!/usr/bin/env python3

import sys

Base64Values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', \
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
                'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', \
                'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', \
                'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', \
                '8', '9', '+', '/']

def EncodeStandardIn():
    # Make sys.stdin a binary stream
    sys.stdin = sys.stdin.detach()

    try:
        # Read 3 bytes at a time
        ReadBytes = sys.stdin.read(3)
        LineLength = 0

        # While there are bytes to be read, process them
        while ReadBytes:
            BitString = ''

            for ReadByte in ReadBytes:
                # With each byte that was read, convert it
                # to a bit string and append it to the
                # bit string for the byte array
                ReadByte = bin(ReadByte)[2:].rjust(8, '0')
                BitString += ReadByte

            # If 76 columns have been printed, write a
            # newline (used for the Base64 standard)
            # 19 is used here because instead of incrementing
            # 4 for every 4 characters printed, 1 is incremented
            # for every 4 characters printed (76 / 19 = 4)
            if LineLength == 19:
                sys.stdout.write('\n')
                LineLength = 0

            # Depending on the number of bytes read, write
            # out the appropriate number of characters
            if len(BitString) == 24:
                for I in range(0,4):
                    sys.stdout.write(Base64Values[int( \
                        BitString[(I*6):((I+1)*6)], 2)])
            elif len(BitString) == 16:
                # Add two zeroes so that the length of the
                # bit string is 18 and results in three
                # 6-bit values
                BitString += '00'
                for I in range(0,3):
                    sys.stdout.write(Base64Values[int( \
                        BitString[(I*6):((I+1)*6)], 2)])
                # Add one padding character at the end so that
                # four characters total are written
                sys.stdout.write('=')
            elif len(BitString) == 8:
                # Add four zeroes so that the length of the
                # bit string is 12 and results in two
                # 6-bit values
                BitString += '0000'
                for I in range(0,2):
                    sys.stdout.write(Base64Values[int( \
                        BitString[(I*6):((I+1)*6)], 2)])
                # Add two padding characters at the end so that
                # four characters total are written
                sys.stdout.write('=')
                sys.stdout.write('=')

            # Increment the length of the line by 1
            LineLength += 1

            # Read the next 3 bytes
            ReadBytes = sys.stdin.read(3)

        # Print a newline at the end of the base64-encoded text
        sys.stdout.write('\n')

    except Exception as Error:
        # Catch all errors here, printing the error information,
        # type, and the line number on which it occurred
        ExcType, ExcObj, ExcTb = sys.exc_info()
        sys.stderr.write('EncodeStandardIn():\n')
        sys.stderr.write('%s error: %s\n\tLine %s\n' \
                         % (str(ExcType), str(Error), \
                            str(ExcTb.tb_lineno)))

def DecodeStandardIn():
    # Make sys.stdin and sys.stdout binary streams so that
    # binary data can be read on stdin and can be written on
    # stdout
    sys.stdin = sys.stdin.detach()
    sys.stdout = sys.stdout.detach()

    try:
        # Set the EndOfFile flag to false
        EndOfFile = False

        # Read 4 bytes at a time, stripping newlines from
        # the input
        NumReadBytes = 0
        ReadBytes = []
        while NumReadBytes < 4 and EndOfFile == False:
            ReadBytes.append(sys.stdin.read(1))

            # If the read byte is empty, then the end of
            # the input file has been reached
            if ReadBytes[len(ReadBytes) - 1] == b'':
                EndOfFile = True
            # If a newline is encountered, remove it from
            # the end of the ReadBytes array and skip over
            # it
            elif ReadBytes[len(ReadBytes) - 1] == b'\n':
                ReadBytes.pop()
            # If the read byte is valid, then increment the
            # number of bytes read
            else:
                NumReadBytes += 1

        # While the end of the file hasn't been reached, continue
        # to read and process the file's contents
        while EndOfFile == False:
            BitString = ''

            for ReadByte in ReadBytes:
                # If the read byte is not a padding character,
                # then process it and add its binary value to
                # the bit string
                if ReadByte != b'=':
                    Base64Index = Base64Values.index( \
                        chr(ord(ReadByte)))
                    BitString += bin(Base64Index)[2:].rjust(6, '0')

            # Depending on the amount of padding at the end of the
            # read bytes, process the bit string accordingly
            if len(BitString) == 24:
                # Get 3 integers from the bit string
                Integers = []
                for I in range(0,3):
                    Integers.append(int( \
                        BitString[(I*8):((I+1)*8)], 2))
                # Create a hexadecimal string from the integers
                # to convert into bytes
                HexString = ''
                for Integer in Integers:
                    if len(hex(Integer)[2:]) == 1:
                        HexString += "0" + hex(Integer)[2:]
                    else:
                        HexString += hex(Integer)[2:]
                # Convert the hexadeciaml string into bytes
                ByteString = bytes.fromhex(HexString)
                # Write the bytes to stdout
                sys.stdout.write(ByteString)

            elif len(BitString) == 18:
                # Cut the end of the bit string off such that
                # it is 16 bits long for two bytes
                BitString = BitString[:16]
                # Get 2 integers from the bit string
                Integers = []
                for I in range(0,2):
                    Integers.append(int( \
                        BitString[(I*8):((I+1)*8)], 2))
                # Create a hexadecimal string from the integers
                # to convert into bytes
                HexString = ''
                for Integer in Integers:
                    if len(hex(Integer)[2:]) == 1:
                        HexString += "0" + hex(Integer)[2:]
                    else:
                        HexString += hex(Integer)[2:]
                # Convert the hexadecimal string into bytes
                ByteString = bytes.fromhex(HexString)
                # Write the bytes to stdout
                sys.stdout.write(ByteString)

            elif len(BitString) == 12:
                # Cut the end of the bit string off such that
                # it is 8 bits long for one byte
                BitString = BitString[:8]
                # Get 1 integer from the bit string
                Integers = []
                for I in range(0,1):
                    Integers.append(int( \
                        BitString[(I*8):((I+1)*8)], 2))
                # Create a hexadecimal string from the integers
                # to convert into bytes
                HexString = ''
                for Integer in Integers:
                    if len(hex(Integer)[2:]) == 1:
                        HexString += "0" + hex(Integer)[2:]
                    else:
                        HexString += hex(Integer)[2:]
                # Convert the 
                ByteString = bytes.fromhex(HexString)
                sys.stdout.write(ByteString)

            # Read the next 4 bytes
            NumReadBytes = 0
            ReadBytes = []
            # While 4 bytes have not yet been read and the
            # end of the input file hasn't been reached,
            # read a byte at a time from the file
            while NumReadBytes < 4 and EndOfFile == False:
                ReadBytes.append(sys.stdin.read(1))

                if ReadBytes[len(ReadBytes) - 1] == b'':
                    EndOfFile = True
                elif ReadBytes[len(ReadBytes) - 1] == b'\n':
                    ReadBytes.pop()
                else:
                    NumReadBytes += 1

    except Exception as Error:
        ExcType, ExcObj, ExcTb = sys.exc_info()
        sys.stderr.write('DecodeStandardIn():\n')
        sys.stderr.write('%s error: %s\n\tLine %s\n' \
                         % (str(ExcType), str(Error), \
                            str(ExcTb.tb_lineno)))

def EncodeFile(FileName):
    # Open the file
    File = open(FileName, "rb")

    try:
        # Read 3 bytes at a time
        ReadBytes = File.read(3)
        LineLength = 0

        while ReadBytes:
            BitString = ''

            # For each of the 3 bytes read, convert it to bits
            # and add the bits to the bit string
            for ReadByte in ReadBytes:
                ReadByte = bin(ReadByte)[2:].rjust(8, '0')

                BitString += ReadByte
           
            # If a line of base64 text has been
            # written (a line being defined as 76 characters),
            # print a newline
            if LineLength == 19:
                sys.stdout.write('\n')
                LineLength = 0

            # Based on the length of the bit string, print out
            # the corresponding number of characters
            if len(BitString) == 24:
                for I in range(0,4):
                    sys.stdout.write(Base64Values[int( \
                        BitString[(I*6):((I+1)*6)], 2)])
            elif len(BitString) == 16:
                BitString += '00'
                for I in range(0,3):
                    sys.stdout.write(Base64Values[int( \
                        BitString[(I*6):((I+1)*6)], 2)])
                sys.stdout.write('=')
            elif len(BitString) == 8:
                BitString += '0000'
                for I in range(0,2):
                    sys.stdout.write(Base64Values[int( \
                        BitString[(I*6):((I+1)*6)], 2)])
                sys.stdout.write('=')
                sys.stdout.write('=')

            LineLength += 1

            # Read the next 3 bytes
            ReadBytes = File.read(3)

        # Write a newline at the end of the base64 output
        sys.stdout.write('\n')

    # If an error occurs, print out the error, the type of
    # error, and the line number of the source file that
    # the error occurred on
    except Exception as Error:
        ExcType, ExcObj, ExcTb = sys.exc_info()
        sys.stderr.write('EncodeFile():\n')
        sys.stderr.write('%s error: %s\n\tLine %s\n' \
                         % (str(ExcType), str(Error), \
                            str(ExcTb.tb_lineno)))

    # Close the input file
    finally:
        File.close()

def DecodeFile(FileName):
    # Open the input file in binary mode and set stdout
    # to binary mode
    File = open(FileName, "rb")
    sys.stdout = sys.stdout.detach()

    try:
        EndOfFile = False

        # Read 4 bytes at a time, stripping newlines from
        # the input
        NumReadBytes = 0
        ReadBytes = []
        while NumReadBytes < 4 and EndOfFile == False:
            ReadBytes.append(File.read(1))

            # If the read byte is an end-of-file char
            # or a newline, process it. Otherwise, add
            # the byte to the byte array.
            if ReadBytes[len(ReadBytes) - 1] == b'':
                EndOfFile = True
            elif ReadBytes[len(ReadBytes) - 1] == b'\n':
                ReadBytes.pop()
            else:
                NumReadBytes += 1

        # While the end of the file has not been reached
        while EndOfFile == False:
            BitString = ''

            # Convert each read byte into binary and append
            # the bits to the bit string
            for ReadByte in ReadBytes:
                if ReadByte != b'=':
                    Base64Index = Base64Values.index( \
                        chr(ord(ReadByte)))
                    BitString += bin(Base64Index)[2:].rjust(6, '0')

            # Based on the length of the bit string, print
            # the corresponding number of bytes
            if len(BitString) == 24:
                Integers = []
                for I in range(0,3):
                    Integers.append(int( \
                        BitString[(I*8):((I+1)*8)], 2))
                HexString = ''
                for Integer in Integers:
                    if len(hex(Integer)[2:]) == 1:
                        HexString += "0" + hex(Integer)[2:]
                    else:
                        HexString += hex(Integer)[2:]
                ByteString = bytes.fromhex(HexString)
                sys.stdout.write(ByteString)

            elif len(BitString) == 18:
                BitString = BitString[:16]
                Integers = []
                for I in range(0,2):
                    Integers.append(int( \
                        BitString[(I*8):((I+1)*8)], 2))
                HexString = ''
                for Integer in Integers:
                    if len(hex(Integer)[2:]) == 1:
                        HexString += "0" + hex(Integer)[2:]
                    else:
                        HexString += hex(Integer)[2:]
                ByteString = bytes.fromhex(HexString)
                sys.stdout.write(ByteString)

            elif len(BitString) == 12:
                BitString = BitString[:8]
                Integers = []
                for I in range(0,1):
                    Integers.append(int( \
                        BitString[(I*8):((I+1)*8)], 2))
                HexString = ''
                for Integer in Integers:
                    if len(hex(Integer)[2:]) == 1:
                        HexString += "0" + hex(Integer)[2:]
                    else:
                        HexString += hex(Integer)[2:]
                ByteString = bytes.fromhex(HexString)
                sys.stdout.write(ByteString)

            # Read the next 4 bytes
            NumReadBytes = 0
            ReadBytes = []
            while NumReadBytes < 4 and EndOfFile == False:
                # Append the next read byte to the byte array
                ReadBytes.append(File.read(1))

                if ReadBytes[len(ReadBytes) - 1] == b'':
                    EndOfFile = True
                elif ReadBytes[len(ReadBytes) - 1] == b'\n':
                    ReadBytes.pop()
                else:
                    NumReadBytes += 1

    except Exception as Error:
        ExcType, ExcObj, ExcTb = sys.exc_info()
        sys.stderr.write('DecodeFile():\n')
        sys.stderr.write('%s error: %s\n\tLine %s\n' \
                         % (str(ExcType), str(Error), \
                            str(ExcTb.tb_lineno)))

    finally:
        File.close()

def main():
    # Determine if there are command-line arguments
    if len(sys.argv) > 1:
        # If there is at least one command-line argument,
        # check to see if it is an option or if it is a file
        if sys.argv[1] == '-d' or sys.argv[1] == '--decode':
            if len(sys.argv) > 2:
                for I in sys.argv[2:]:
                    # Decode each file specified on the command line
                    DecodeFile(I)
            else:
                # Decode base64 data sent to standard in
                DecodeStandardIn()
        else:
            for I in sys.argv[1:]:
                # Encode each file specified on the command line
                EncodeFile(I)

    # If there are no command-line arguments to process, then process
    # standard in
    else:
        EncodeStandardIn()

    sys.exit(0)

if __name__ == "__main__":
    main()
