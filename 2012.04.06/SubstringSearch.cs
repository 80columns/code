using System;
using System.IO;
using System.Text;

class SubstringSearch {

    /* Search the file at FileName for Substring */
    static void SearchFile(string FileName, string Substring) {

        /* Declare the FileStream outside the try block
         * so that it can be closed in the finally block */
        StreamReader FileStream;

        try {
            FileStream = new StreamReader(FileName);
            StringBuilder String = new StringBuilder();
            bool StringsMatch = true;
            int CharacterNumber = 0;
            char Character;

            /* While there is still a character to be read, continue
             * reading */
            while(FileStream.Peek() >= 0) {

                /* Append the next character to the container
                 * string */
                Character = Convert.ToChar(FileStream.Read());
                String.Append(Character);
                CharacterNumber++;

                if(String.ToString().Length == Substring.Length) {

                    /* Set the StringsMatch flag to true, and
                     * get the current container string */
                    StringsMatch = true;
                    string ContainerString = String.ToString();

                    /* Compare the two strings */
                    for(int Index = 0;
                        Index < ContainerString.Length; Index++) {
                        if(ContainerString[Index] !=
                           Substring[Index]) {
                            StringsMatch = false;
                        }
                    }

                    /* Remove the first character of the container
                     * string */
                    String.Remove(0, 1);

                    /* If a match in the file is found, print it */
                    if(StringsMatch == true) {
                        Console.ForegroundColor = ConsoleColor.Blue;
                        Console.WriteLine("[{0}] (@ characters" +
                                          " {1}-{2}) \"{3}\"",
                                          FileName,
                                          (1 + CharacterNumber -
                                           ContainerString.Length),
                                          CharacterNumber,
                                          Substring);
                        Console.ResetColor();
                    }
                }
            }
        }
        catch(Exception E) {

            /* Print the exception and return from the function */
            Console.WriteLine("Exception: {0}", E);
            return;
        }
        finally {

            /* Close the file */
            FileStream.Close();
        }
    }

    static void Main(string[] args) {

        /* Check the number of arguments */
        if(args.Length < 2) {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Error: You must specify a substring" +
                              " to search for and at least one" +
                              " file to search in");
            Console.WriteLine("E.x.: ./SubstringSearch foo bar.txt");
            Console.ResetColor();
            return;
        }

        /* Get the substring to search for */
        string Substring = args[0];

        /* Iterate over the files to be searched */
        for(int Index = 1; Index < args.Length; Index++) {
            SearchFile(args[Index], Substring);
        }

        return;
    }
}
