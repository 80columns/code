<?php

    /* Initialize Variables */
    $ChildPIDs = array();
    $ConnectedSockets = array();
    $FinishedChildren = array();
    $ServerSocket = null;
    $Host = "127.0.0.1";
    $Port = 80;

    /* Set ticks = 1 to allow the signal handler to
     * be executed, set a signal handler for Ctrl-C
     * input, and set the execution time limit to
     * infinite so that the script doesn't time out
     * while waiting for incoming connections */
    declare(ticks = 1);
    pcntl_signal(SIGINT, "SIGINTHandler");
    set_time_limit(0);

    /* Set up the server socket for incoming connections */
    $ServerSocket = socket_create(AF_INET, SOCK_STREAM, 0);
    socket_bind($ServerSocket, $Host, $Port);
    socket_listen($ServerSocket);
    socket_set_nonblock($ServerSocket);

    /* Loop infinitely, handling client connections */
    while(true)
    {
        /* Check for finished child functions, and close
         * their sockets of they are done */
        $ChildPIDsLength = count($ChildPIDs);
        for($Index = 0; $Index < $ChildPIDsLength; $Index++)
        {
            if(pcntl_waitpid($ChildPIDs[$Index], $Status,
                             WNOHANG) != 0)
            {
                array_push($FinishedChildren, $Index);
                socket_shutdown($ConnectedSockets[$Index], 2);
                socket_close($ConnectedSockets[$Index]);
            }
        }

        /* Remove the finished child function information
         * after a child function has finished executing */
        $FinishedChildrenLength = count($FinishedChildren);
        for($Index = 0; $Index < $FinishedChildrenLength; $Index++)
        {
            array_splice($ChildPIDs, $FinishedChildren[$Index], 1);
            array_splice($ConnectedSockets,
                         $FinishedChildren[$Index], 1);
        }

        /* Reset the list of finished children */
        $FinishedChildren = array();

        /* Check for a new connection, and if one is present,
         * process it */
        array_push($ConnectedSockets, null);
        $ConnectedSocketsLastIndex = count($ConnectedSockets) - 1;
        if(($ConnectedSockets[$ConnectedSocketsLastIndex] = 
            @socket_accept($ServerSocket)) !== false)
        {
            /* Fork a new process to handle the incoming
             * connection */
            $PID = pcntl_fork();

            /* This is the child process */
            if($PID == 0)
            {
                /* Unset the signal handler, process the new
                 * connection, and exit the child process */
                pcntl_signal(SIGINT, SIG_IGN);
                ProcessClient(
                    $ConnectedSockets[$ConnectedSocketsLastIndex]);
                exit();
            }

            /* This is the parent process */
            else
            {
                /* Add the new child process PID to the parent's list
                 * of PIDs */
                array_push($ChildPIDs, $PID);
            }
        }
        else
        {
            /* If no new connection is available, remove the last
             * element from the list of connected sockets */
            array_pop($ConnectedSockets);
        }
    }

    /* This is the signal handler for the parent process. It handles
     * Ctrl-C input to the program from the command line so that the
     * server can exit cleanly */
    function SIGINTHandler($Signal)
    {
        /* Make external variables available inside the signal
         * handler */
        global $ChildPIDs, $ConnectedSockets, $ServerSocket;

        print "\n[Server] Waiting for children to exit...\n";

        /* Wait for all of the child processes to finish before
         * proceeding to shut down */
        $ChildPIDsLength = count($ChildPIDs);
        for($Index = 0; $Index < $ChildPIDsLength; $Index++)
        {
            pcntl_waitpid($ChildPIDs[$Index], $Status, 0);
            socket_shutdown($ConnectedSockets[$Index], 2);
            socket_close($ConnectedSockets[$Index]);
        }

        /* Close the server's main socket */
        if($ServerSocket != null)
        {
            socket_shutdown($ServerSocket, 2);
            socket_close($ServerSocket);
        }

        /* Finally, exit the server */
        print "[Server] Exiting...\n";
        exit();
    }

    /* This is the function for child processes, used to process
     * a new connection from a client */
    function ProcessClient($ConnectedSocket)
    {
        $ClientString = "";

        /* Receive the client's message */
        while(($ReadCharacter = socket_read($ConnectedSocket, 1)) !=
              "\n")
        {
            $ClientString .= $ReadCharacter;
        }

        /* Get the individual parts of the client string */
        $ClientStringPieces = explode(" ", $ClientString);

        /* If this is a GET request, process it */
        if($ClientStringPieces[0] == "GET")
        {
            /* If the requested file exists, send an OK message
             * and the file */
            if(file_exists($ClientStringPieces[1]))
            {
                $ServerString = "HTTP/1.1 200 OK\n";
                socket_send($ConnectedSocket, $ServerString, 
                            strlen($ServerString), 0); 

                $FileHandle = fopen($ClientStringPieces[1], "r");

                while(($FileLine = fgets($FileHandle)) !== false)
                {
                    socket_send($ConnectedSocket, $FileLine, 
                                strlen($FileLine), 0); 
                }
            }

            /* If the requested file does not exist, let the
             * client know */
            else
            {
                $ServerString = "HTTP/1.1 404 Not Found\n";
                socket_send($ConnectedSocket, $ServerString, 
                            strlen($ServerString), 0); 
            }
        }

        /* If this is not a GET request, notify the client */
        else
        {
            $ServerString = "HTTP/1.1 9000 Method Not Supported\n";
            socket_send($ConnectedSocket, $ServerString, 
                        strlen($ServerString), 0); 
        }
    }
?>
