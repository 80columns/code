#include <iostream>
#include <map>
#include <cryptopp/sha.h>
#include <cryptopp/hex.h>
#include <cryptopp/filters.h>

using namespace std;
using namespace CryptoPP;

string Hash(string Value);
bool FindElement(string Value, map<string, string> HashTable);

bool InsertElement(string Value, map<string, string> *HashTable)
{
    if(FindElement(Value, *HashTable) == false)
    {
        HashTable->insert(pair<string,string>(Hash(Value), Value));
        return true;
    }
    else
    {
        return false;
    }
}

bool DeleteElement(string Value, map<string, string> *HashTable)
{
    if(FindElement(Value, *HashTable) == true)
    {
        HashTable->erase(Hash(Value));
        return true;
    }
    else
    {
        return false;
    }
}

bool FindElement(string Value, map<string, string> HashTable)
{
    if(HashTable.find(Hash(Value)) == HashTable.end())
    {
        return false;
    }
    else
    {
        return true;
    }
}

string Hash(string Value)
{
    SHA512 Hash;
    byte Digest[CryptoPP::SHA512::DIGESTSIZE];

    Hash.CalculateDigest(Digest, (byte*)Value.c_str(), Value.length());

    HexEncoder Encoder;
    string Output;
    Encoder.Attach(new StringSink(Output));
    Encoder.Put(Digest, sizeof(Digest));
    Encoder.MessageEnd();

    return Output;
}

int main(int argc, char *argv[])
{
    map<string, string> HashTable;
    bool Finished = false;
    string Option;
    string Value;

    while(Finished == false)
    {
        cout << "Select an option:" << endl;
        cout << "1 :: Insert a string into the hash table" << endl;
        cout << "2 :: Delete a string from the hash table" << endl;
        cout << "3 :: Look up a string in the hash table" << endl;
        cout << "4 :: Quit the program" << endl;
        cout << endl << "Enter your selection: ";
        cin >> Option;

        if(Option == "1")
        {
            cout << "Enter a string to insert into the hash table: ";
            cin >> Value;

            bool ElementInserted = InsertElement(Value, &HashTable);

            if(ElementInserted == true)
            {
                cout << endl << "The string '" << Value << "' was inserted into the hash table" << endl << endl;
            }
            else
            {
                cout << endl << "Error: The string '" << Value << "' is already in the hash table" << endl << endl;
            }
        }
        else if(Option == "2")
        {
            cout << "Enter a string to delete from the hash table: ";
            cin >> Value;

            bool ElementDeleted = DeleteElement(Value, &HashTable);

            if(ElementDeleted == true)
            {
                cout << endl << "The string '" << Value << "' was deleted from the hash table" << endl << endl;
            }
            else
            {
                cout << endl << "Error: The string '" << Value << "' is not in the hash table" << endl << endl;
            }
        }
        else if(Option == "3")
        {
            cout << "Enter a string to find in the hash table: ";
            cin >> Value;

            bool ElementFound = FindElement(Value, HashTable);

            if(ElementFound == true)
            {
                cout << endl << "The string '" << Value << "' is in the hash table" << endl << endl;
            }
            else
            {
                cout << endl << "The string '" << Value << "' is not in the hash table" << endl << endl;
            }
        }
        else if(Option == "4")
        {
            Finished = true;
        }
        else
        {
            cout << endl << "Invalid option selected!" << endl << endl;
        }
    }

    return 0;
}
