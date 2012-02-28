#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/socket.h>
#include <string.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>

int ConnectToServer(int Port, char *Address);
void ProcessCommands(int ClientSocket);
void SendCharacter(char Data, int ClientSocket);
char ReceiveCharacter(int ClientSocket);

int main(int argc, char **argv)
{
    if(argc != 3)
    {
        fprintf(stderr, "Error: Supply an IP address and port to connect"
                        " to as two arguments\n");
        fprintf(stderr, "E.g. %s 127.0.0.1 80\n", argv[0]);
        return 1;
    }

    int ClientSocket = ConnectToServer(atoi(argv[2]), argv[1]);
    fprintf(stdout, "Connected to server\n");

    ProcessCommands(ClientSocket);
    fprintf(stdout, "Exiting shell\n");

    close(ClientSocket);

    exit(EXIT_SUCCESS);
}

/* Connect to the server */
int ConnectToServer(int Port, char *Address)
{
    int ClientSocket = 0;
    struct hostent *HE;
    struct sockaddr_in ServerData;

    if((ClientSocket = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("");
        fprintf(stderr, "Error creating client socket\n");
        exit(EXIT_FAILURE);
    }

    if((HE = gethostbyname(Address)) == NULL)
    {
        herror("");
        fprintf(stderr, "Error getting address name\n");
        exit(EXIT_FAILURE);
    }

    memcpy(&ServerData.sin_addr, HE->h_addr_list[0], HE->h_length);
    ServerData.sin_family = AF_INET;
    ServerData.sin_port = htons(Port);

    if(connect(ClientSocket, (struct sockaddr *)&ServerData, \
       sizeof(ServerData)) == -1)
    {
        perror("");
        fprintf(stderr, "Error connecting to server\n");
        exit(EXIT_FAILURE);
    }

    return ClientSocket;
}

/* Process commands for the session */
void ProcessCommands(int ClientSocket)
{
    int Running = 1;
    char ReadCharacter;
    char ReceivedCharacter;
    char *CommandString = (char *)malloc(sizeof(char));
    char *ResponseString = (char *)malloc(sizeof(char));
    int CommandStringLength;
    int ResponseStringLength;
    int Index = 0;

    while(Running == 1)
    {
        memset(CommandString, '\0', strlen(CommandString));
        memset(ResponseString, '\0', strlen(ResponseString));
        ReadCharacter = ' ';
        ReceivedCharacter = ' ';
        CommandStringLength = 1;
        ResponseStringLength = 1;

        fprintf(stdout, "$ ");

        while((ReadCharacter = fgetc(stdin)) != '\n')
        {
            if(strlen(CommandString) == CommandStringLength)
            {
                CommandStringLength *= 2;
                CommandString =
                    (char *)realloc(CommandString, CommandStringLength \
                                    * sizeof(char));
            }

            strncat(CommandString, &ReadCharacter, 1);
        }

        for(Index = 0; Index < strlen(CommandString); Index++)
        {
            SendCharacter(CommandString[Index], ClientSocket);
        }
        SendCharacter('\0', ClientSocket);

        if(strncmp(CommandString, "exit", 4) == 0)
        {   
            Running = 0;
            continue;
        }

        while((ReceivedCharacter =
                   ReceiveCharacter(ClientSocket)) != '\0')
        {
            if(strlen(ResponseString) == ResponseStringLength)
            {
                ResponseStringLength *= 2;
                ResponseString =
                    (char *)realloc(ResponseString,
                                    ResponseStringLength * sizeof(char));
            }

            strncat(ResponseString, &ReceivedCharacter, 1);
        }

        fprintf(stdout, "%s", ResponseString);
    }

    free(CommandString);
    free(ResponseString);
}

/* Send a character to the server */
void SendCharacter(char Data, int ClientSocket)
{
    if(send(ClientSocket, &Data, sizeof(Data), 0) == -1)
    {
        perror("");
        fprintf(stderr, "Error sending data to server\n");
        exit(EXIT_FAILURE);
    }
}

/* Receive a character from the server */
char ReceiveCharacter(int ClientSocket)
{
    char ReceivedCharacter;

    if(recv(ClientSocket, &ReceivedCharacter, sizeof(ReceivedCharacter), \
            0) == -1)
    {
        perror("");
        fprintf(stderr, "Error receiving data from server\n");
        exit(EXIT_FAILURE);
    }

    return ReceivedCharacter;
}
