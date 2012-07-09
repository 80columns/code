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

    if(lstat(File, &FileStats) == -1)
    {    
        perror("Error:\n\t");
        return;
    }    

    if(S_ISREG(FileStats.st_mode))
    {    
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
    else if(S_ISDIR(FileStats.st_mode))
    {    
        DIR *Directory;
        struct dirent *Entry;

        if((Directory = opendir(File)) == NULL)
        {    
            perror("Error:\n\t");
            return;
        }
        else
        {
            char FullDirPath[PATH_MAX];
            char FullFilePath[PATH_MAX];

            if(realpath(File, FullDirPath) == NULL)
            {
                perror("Error:\n\t");
                return;
            }

            while((Entry = readdir(Directory)) != NULL)
            {
                if(strcmp(Entry->d_name, ".") != 0 && \
                   strcmp(Entry->d_name, "..") != 0)
                {
                    memset(FullFilePath, 0, PATH_MAX);
                    strcat(FullFilePath, FullDirPath);
                    strcat(FullFilePath, "/");
                    strcat(FullFilePath, Entry->d_name);
                    RemoveFile(FullFilePath);
                }
            }

            if(rmdir(File) == -1)
            {
                perror("Error\n\t");
                return;
            }

            fprintf(stdout, "Directory %s removed\n", File);
            
            if(closedir(Directory) == -1)
            {
                perror("Error:\n\t");
                return;
            }
        }
    }
    else if(S_ISLNK(FileStats.st_mode))
    {
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

    if(argc < 2)
    {
        fprintf(stderr, "Error: Specify at least one file to"
                        " remove\n");
    }

    for(I = 1; I < argc; I++)
    {
        RemoveFile(argv[I]);
    }

    return 0;
}
