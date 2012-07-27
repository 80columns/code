#define _BSD_SOURCE

#include <stdio.h>
#include <errno.h>
#include <dirent.h>
#include <limits.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

void RemoveFile(char *File)
{
    struct stat FileStats;
    int Status;

    /* Get the file's information */
    if(lstat(File, &FileStats) == -1)
    {    
        perror("Error:\n\t");
        return;
    }

    /* If the file is a regular file, then delete it */
    if(S_ISREG(FileStats.st_mode))
    {
        /* Attempt to delete the file, and print a message
         * telling whether deletion was successful */
        if(unlink(File) == -1)
        {    
            perror("Error:\n\t");
            return;
        }
        else 
        {    
            fprintf(stdout, "File %s removed\n", File);
        }
    }
    /* If the file is a directory, loop over its contents and
     * pass each one to the FileRemove function */
    else if(S_ISDIR(FileStats.st_mode))
    {    
        DIR *Directory;
        struct dirent *Entry;

        /* Attempt to open the directory */
        if((Directory = opendir(File)) == NULL)
        {    
            perror("Error:\n\t");
            return;
        }
        else
        {
            char FullDirPath[PATH_MAX];
            char FullFilePath[PATH_MAX];

            /* Get the full path of the directory */
            if(realpath(File, FullDirPath) == NULL)
            {
                perror("Error:\n\t");
                return;
            }

            /* Loop over the directory contents */
            while((Entry = readdir(Directory)) != NULL)
            {
                /* Don't try to remove . or .. from the directory */
                if(strcmp(Entry->d_name, ".") != 0 && \
                   strcmp(Entry->d_name, "..") != 0)
                {
                    /* Get the full file path of the entry and remove it */
                    memset(FullFilePath, 0, PATH_MAX);
                    strcat(FullFilePath, FullDirPath);
                    strcat(FullFilePath, "/");
                    strcat(FullFilePath, Entry->d_name);
                    RemoveFile(FullFilePath);
                }
            }

            /* Close the directory */
            if(closedir(Directory) == -1)
            {
                perror("Error:\n\t");
                return;
            }

            /* Remove the directory itself */
            if(rmdir(File) == -1)
            {
                perror("Error\n\t");
                return;
            }

            fprintf(stdout, "Directory %s removed\n", File);
        }
    }
    /* If the file is a symbolic link, then delete it */
    else if(S_ISLNK(FileStats.st_mode))
    {
        /* Attempt to delete the symbolic link, and print a message
         * telling whether deletion was successful */
        if(unlink(File) == -1)
        {
            perror("Error:\n\t");
            return;
        }
        else
        {
            fprintf(stdout, "Symbolic link %s removed\n", File);
        }
    }
    /* If the file is not a directory, regular file, or symbolic
     * link, print an error message */
    else
    {
        fprintf(stderr, "Error: %s is not a directory or regular"
                        " file\n", File);
    }

    return;
}

int main(int argc, char **argv)
{
    int I;

    /* Check the number of command-line arguments */
    if(argc < 2)
    {
        fprintf(stderr, "Error: Specify at least one file to"
                        " remove\n");
    }

    /* Loop over the files and folders specified in the
     * command-line arguments */
    for(I = 1; I < argc; I++)
    {
        RemoveFile(argv[I]);
    }

    return 0;
}
