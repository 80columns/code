#include <sstream>
#include <iostream>
#include <unistd.h>
#include <arpa/inet.h>

using namespace std;

/* Scan a single port and host */
void ScanPort(string HostToScan, int PortToScan)
{
    cout << "Scanning Port " << PortToScan << " ... ";
    struct sockaddr_in ServerAddress;
    int Socket;

    /* Set up the server information in the address */
    ServerAddress.sin_family = AF_INET;
    ServerAddress.sin_port = htons(PortToScan);
    ServerAddress.sin_addr.s_addr = inet_addr(HostToScan.c_str());

    /* Set up the socket */
    Socket = socket(AF_INET, SOCK_STREAM, 0);

    /* Attempt to connect to the host */
    if(connect(Socket, (struct sockaddr *)&ServerAddress,
               sizeof(ServerAddress)) == 0)
    {
        cout << "Port " << PortToScan << " is open" << endl;
    }
    else
    {
        cout << "Port " << PortToScan << " is closed" << endl;
    }

    /* Shutdown and close the socket */
    shutdown(Socket, SHUT_RDWR);
    close(Socket);
}

/* Process an argument list of ports to scan and a host */
void ScanHost(string HostToScan, string ArgumentList)
{
    bool ReadingPort = false;
    bool ReadingPortRange = false;
    int FirstPortInRange = 0;
    int PortBeginningIndex = 0;
    int CurrentPortLength = 0;
    int PortNumber = 0;

    for(int i = 0; i < ArgumentList.length(); i++)
    {
        /* If the current character is a digit, process it */
        if(isdigit(ArgumentList.at(i)) != 0)
        {
            /* If this is the last digit in the argument string, it
             * is part of the last port to scan */
            if(i == ArgumentList.length() - 1)
            {
                /* Get the last port number */
                istringstream buffer(ArgumentList.substr(
                    PortBeginningIndex, CurrentPortLength + 1));
                buffer >> PortNumber;

                /* If we are currently reading a single port, scan it
                 * on the host */
                if(ReadingPortRange == false)
                {
                    if(PortNumber < 1 || PortNumber > 65535)
                    {
                        cerr << "Error: " << PortNumber << " is" <<
                                " not a valid port number" <<
                                endl;
                    }
                    else
                    {
                        ScanPort(HostToScan, PortNumber);
                    }
                }

                /* If we are currently reading a port range, scan
                 * all of the ports in the range */
                else
                {
                    for(int j = FirstPortInRange; j <= PortNumber;
                        j++)
                    {
                        if(j < 1 || j > 65535)
                        {
                            cerr << "Error: " << PortNumber <<
                                    " is not a" << 
                                    " valid port number" << endl;
                        }
                        else
                        {
                            ScanPort(HostToScan, j);
                        }
                    }
                }
            }

            /* If this is not the last character in the string,
             * process it normally */
            else
            {
                /* We are now reading a port, so set the beginning
                 * index if we were not previously reading a port,
                 * and in all cases increment the current port
                 * length */
                if(ReadingPort == false)
                {
                    PortBeginningIndex = i;
                    ReadingPort = true;
                }
                CurrentPortLength++;
            }
        }

        /* If the current read character is a comma, we have either
         * just finished reading a port or a port range, so perform
         * the scan operation on the port(s) */
        else if(ArgumentList.at(i) == ',')
        {
            ReadingPort = false;
            istringstream buffer(ArgumentList.substr(
                PortBeginningIndex, CurrentPortLength + 1));
            buffer >> PortNumber;

            /* We just read a single port, so scan it */
            if(ReadingPortRange == false)
            {
                if(PortNumber < 1 || PortNumber > 65535)
                {
                    cerr << "Error: " << PortNumber << " is not a"
                            " valid port number" << endl;
                }
                else
                {
                    ScanPort(HostToScan, PortNumber);
                }
            }

            /* We just read a port range, so scan all of the ports in
             * the range */
            else
            {
                for(int j = FirstPortInRange; j <= PortNumber; j++)
                {
                    if(j < 1 || j > 65535)
                    {
                        cerr << "Error: " << PortNumber <<
                                " is not a valid port number" <<
                                endl;
                    }
                    else
                    {
                        ScanPort(HostToScan, j);
                    }
                }
                ReadingPortRange = false;
            }

            CurrentPortLength = 0;
        }
        /* If the current read character is a dash, we are in the
         * middle of reading a port range, so set the flag for
         * processing a range and get ready to read another port */
        else if(ArgumentList.at(i) == '-')
        {
            ReadingPort = false;
            ReadingPortRange = true;
            istringstream buffer(ArgumentList.substr(
                PortBeginningIndex, CurrentPortLength + 1));
            buffer >> FirstPortInRange;

            CurrentPortLength = 0;
        }
    }
}

int main(int argc, char *argv[])
{
    /* If there are less than two arguments, print an error and help
     * message */
    if(argc != 3)
    {
        cerr << "Error: You must specify an IP address to scan" <<
                " and a list of ports" << endl;
        cerr << "E.g. " << argv[0] << " 127.0.0.1 80" << endl;
        cerr << "     " << argv[0] << " 127.0.0.1 80,443" << endl;
        cerr << "     " << argv[0] << " 127.0.0.1 5-10,80" << endl;
        cerr << "     " << argv[0] << " 127.0.0.1 80,90-100" << endl;
        cerr << "     " << argv[0] << " 127.0.0.1 50-70" << endl;
        return 1;
    }

    /* Get the arguments as strings */
    string HostToScan = argv[1];
    string ArgumentList = argv[2];

    /* Display the host we are scanning */
    cout << endl << "[==========]     " << HostToScan <<
            "     [==========]" << endl;

    /* Scan the host */
    ScanHost(HostToScan, ArgumentList);

    return 0;
}
