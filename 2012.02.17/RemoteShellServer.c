#define _POSIX_C_SOURCE 2

#include <stdio.h>
#include <stdlib.h>
#include <error.h>
#include <sys/socket.h>
#include <string.h>
#include <signal.h>
#include <netinet/in.h>
#include <unistd.h>

typedef struct
{
    int ServerSocket;
    struct sockaddr_in ServerAddress;
} ServerData;

/* Use a global variable so that we can free the socket
 * if the user ctrl-c's the program */
ServerData SD;

void SigIntHandler();
void InitiateServer(int Port);
int AcceptNewConnection();
void SendCharacter(char Data, int ConnectedServerSocket);
char ReceiveCharacter(int ConnectedServerSocket);

int main(int argc, char **argv)
{
    if(argc != 2)
    {
        fprintf(stderr, "Error: Supply a port to listen on as a single"
                        " argument\n");
        fprintf(stderr, "E.g. %s 80\n", argv[0]);
        return 1;
    }

    /* Set up listening socket */
    InitiateServer(atoi(argv[1]));

    /* Set up a signal to catch ctrl-c/SIGINT */
    signal(SIGINT, SigIntHandler);

    /* Accept connections from clients forever */
    while(1)
    {
        AcceptNewConnection();
    }

    exit(EXIT_SUCCESS);
}

/* Handle ctrl-c/SIGINT */
void SigIntHandler()
{
    close(SD.ServerSocket);
    exit(EXIT_SUCCESS);
}

/* Set up listening socket */
void InitiateServer(int Port)
{
    if((SD.ServerSocket = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("");
        fprintf(stderr, "Error creating server socket");
        exit(EXIT_FAILURE);
    }

    SD.ServerAddress.sin_family = AF_INET;
    SD.ServerAddress.sin_addr.s_addr = INADDR_ANY;
    SD.ServerAddress.sin_port = htons(Port);
    if(bind(SD.ServerSocket, (struct sockaddr *)&SD.ServerAddress, \
            sizeof(SD.ServerAddress)) == -1)
    {
        perror("");
        fprintf(stderr, "Error binding server socket to port %d\n", \
                Port);
        exit(EXIT_FAILURE);
    }

    fprintf(stdout, "Socket bound to port %d\n", Port);

    if(listen(SD.ServerSocket, 1) == -1)
    {
        perror("");
        fprintf(stderr, "Error listening on server socket\n");
        exit(EXIT_FAILURE);
    }

    fprintf(stdout, "Listening on server socket\n");
}

/* Accept a new connection from a client and process their data */
int AcceptNewConnection()
{
    int ConnectedServerSocket = 0;
    int AddressLength = sizeof(struct sockaddr_in);
    char ReceivedCharacter;
    char *CommandString = (char *)malloc(sizeof(char));
    int CommandStringLength;
    FILE *CommandPipe;
    char OutputCharacter;
    char *OutputString = (char *)malloc(sizeof(char));
    int OutputStringLength;
    int Index = 0;
    int ClientIsConnected = 1;

    if((ConnectedServerSocket =
            accept(SD.ServerSocket, \
                   (struct sockaddr *)&SD.ServerAddress, \
                   (socklen_t *)&AddressLength)) == -1)
    {   
        perror("");
        fprintf(stderr, "Error accepting connection\n");
        exit(EXIT_FAILURE);
    }   

    fprintf(stdout, "Accepted an incoming connection\n");

    while(ClientIsConnected == 1)
    {
        ReceivedCharacter = ' ';
        CommandStringLength = 1;
        OutputStringLength = 1;
        memset(CommandString, '\0', strlen(CommandString));
        memset(OutputString, '\0', strlen(OutputString));

        while((ReceivedCharacter =
                   ReceiveCharacter(ConnectedServerSocket)) != '\0')
        {
            if(strlen(CommandString) == CommandStringLength)
            {
                CommandStringLength *= 2;
                CommandString =
                    (char *)realloc(CommandString,
                                    CommandStringLength * sizeof(char));
            }

            strncat(CommandString, &ReceivedCharacter, 1);
        }

        if(strncmp(CommandString, "exit", 4) == 0)
        {
            fprintf(stdout, "Client disconnected\n");
            ClientIsConnected = 0;
            continue;
        }

        if((CommandPipe = popen(CommandString, "r")) == NULL)
        {
            perror("");
            fprintf(stderr, "Error running command\n");
            exit(EXIT_FAILURE);
        }

        fprintf(stdout, "Executed command\n");

        while((OutputCharacter = fgetc(CommandPipe)) != EOF)
        {
            if(strlen(OutputString) == OutputStringLength)
            {
                OutputStringLength *= 2;
                OutputString =
                    (char *)realloc(OutputString, OutputStringLength * \
                    sizeof(char));
            }
        
            strncat(OutputString, &OutputCharacter, 1);
        }

        pclose(CommandPipe);

        for(Index = 0; Index < strlen(OutputString); Index++)
        {
            SendCharacter(OutputString[Index], ConnectedServerSocket);
        }
        SendCharacter('\0', ConnectedServerSocket);
    }

    free(CommandString);
    free(OutputString);
    close(ConnectedServerSocket);
}

/* Send a character to the client */
void SendCharacter(char Data, int ConnectedServerSocket)
{
    if(send(ConnectedServerSocket, &Data, sizeof(Data), 0) == -1)
    {
        perror("");
        fprintf(stderr, "Error sending data to server\n");
        exit(EXIT_FAILURE);
    }
}

/* Receive a character from the client */
char ReceiveCharacter(int ConnectedServerSocket)
{
    char ReceivedCharacter;

    if(recv(ConnectedServerSocket, &ReceivedCharacter, \
       sizeof(ReceivedCharacter), 0) == -1)
    {
        perror("");
        fprintf(stderr, "Error receiving data from client\n");
        exit(EXIT_FAILURE);
    }

    return ReceivedCharacter;
}
