#include <iostream>
#include <map>
#include <cryptopp/sha.h>
#include <cryptopp/hex.h>
#include <cryptopp/filters.h>

using namespace std;
using namespace CryptoPP;

string Hash(string Value);
bool FindElement(string Value, map<string, string> HashTable);

/* Insert an element into the hash table, first checking whether
 * the element is already present in the hash table */
bool InsertElement(string Value, map<string, string> *HashTable)
{
    /* If the element is not already present in the hash table,
     * insert it and return a success status */
    if(FindElement(Value, *HashTable) == false)
    {
        HashTable->insert(pair<string,string>(Hash(Value), Value));
        return true;
    }
    /* If the element is already present in the hash table,
     * return a non-success status */
    else
    {
        return false;
    }
}

/* Delete an element from the hash table, first checking whether
 * the element is present in the hash table */
bool DeleteElement(string Value, map<string, string> *HashTable)
{
    /* If the element is present in the hash table, delete it
     * and return a success status */
    if(FindElement(Value, *HashTable) == true)
    {
        HashTable->erase(Hash(Value));
        return true;
    }
    /* If the element is not present in the hash table,
     * return a non-success status */
    else
    {
        return false;
    }
}

/* Find an element in the hash table */
bool FindElement(string Value, map<string, string> HashTable)
{
    /* If the element is not found in the hash table, return
     * a non-success status */
    if(HashTable.find(Hash(Value)) == HashTable.end())
    {
        return false;
    }
    /* If the element is found in the hash table, return a
     * success status */
    else
    {
        return true;
    }
}

/* Generate a SHA512 hash of a string */
string Hash(string Value)
{
    /* Create the hash object and the digest */
    SHA512 Hash;
    byte Digest[CryptoPP::SHA512::DIGESTSIZE];

    /* Calculate the hash of the input string */
    Hash.CalculateDigest(Digest, (byte*)Value.c_str(), Value.length());

    /* Encode the output from binary to a hexadecimal string */
    HexEncoder Encoder;
    string Output;
    Encoder.Attach(new StringSink(Output));
    Encoder.Put(Digest, sizeof(Digest));
    Encoder.MessageEnd();

    /* Return the SHA512 hash of the input string */
    return Output;
}

int main(int argc, char *argv[])
{
    map<string, string> HashTable;
    bool Finished = false;
    string Option;
    string Value;

    /* Loop indefinitely until the user chooses to exit the
     * program */
    while(Finished == false)
    {
        /* Print the menu */
        cout << "Select an option:" << endl;
        cout << "1 :: Insert a string into the hash table" << endl;
        cout << "2 :: Delete a string from the hash table" << endl;
        cout << "3 :: Look up a string in the hash table" << endl;
        cout << "4 :: Quit the program" << endl;
        cout << endl << "Enter your selection: ";
        cin >> Option;

        /* Insert a string into the hash table */
        if(Option == "1")
        {
            /* Get the string from the user */
            cout << "Enter a string to insert into the hash table: ";
            cin >> Value;

            /* Insert the element into the hash table */
            bool ElementInserted = InsertElement(Value, &HashTable);

            /* If the element was successfully inserted, print a
             * success message */
            if(ElementInserted == true)
            {
                cout << endl << "The string '" << Value
                     << "' was inserted into the hash table"
                     << endl << endl;
            }
            /* If the element was already present in the hash table,
             * print an error message */
            else
            {
                cerr << endl << "Error: The string '"
                     << Value << "' is already in the hash table"
                     << endl << endl;
            }
        }
        /* Delete a string from the hash table */
        else if(Option == "2")
        {
            /* Get the string from the user */
            cout << "Enter a string to delete from the hash table: ";
            cin >> Value;

            /* Delete the element from the hash table */
            bool ElementDeleted = DeleteElement(Value, &HashTable);

            /* If the element was successfully deleted, print a
             * success message */
            if(ElementDeleted == true)
            {
                cout << endl << "The string '" << Value
                     << "' was deleted from the hash table" << endl
                     << endl;
            }
            /* If the element was not present in the hash table,
             * print an error message */
            else
            {
                cerr << endl << "Error: The string '" << Value
                     << "' is not in the hash table" << endl << endl;
            }
        }
        /* Find a string in the hash table */
        else if(Option == "3")
        {
            /* Get the string from the user */
            cout << "Enter a string to find in the hash table: ";
            cin >> Value;

            /* Find the element in the hash table */
            bool ElementFound = FindElement(Value, HashTable);

            /* If the element was found, print a success message */
            if(ElementFound == true)
            {
                cout << endl << "The string '" << Value
                     << "' is in the hash table" << endl << endl;
            }
            /* If the element was not found, print a non-success
             * message */
            else
            {
                cout << endl << "The string '" << Value
                     << "' is not in the hash table" << endl << endl;
            }
        }
        /* Exit the program */
        else if(Option == "4")
        {
            Finished = true;
        }
        /* If the user chose an invalid option, let them know and
         * then display the menu again */
        else
        {
            cout << endl << "Invalid option selected!" << endl << endl;
        }
    }

    return 0;
}
