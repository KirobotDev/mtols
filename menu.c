#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <windows.h>

#define RESET   "\033[0m"
#define RED     "\033[31m"
#define GREEN   "\033[32m"
#define BLUE    "\033[34m"
#define CYAN    "\033[36m"
#define PURPLE  "\033[35m"
#define WHITE   "\033[37m"

void clearcsl(void)
{
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

void ascii(void)
{
    SetConsoleOutputCP(CP_UTF8);
    printf(
        PURPLE
    "   ▄▄█▄      ▄▀█▄ ▄█▀███▄    ▄▄█▀█▄▄      ▄▄█       ▄▄▄█▀▄▄\n"
    "   █■▀▀█▄██▄   ▀ █■▀▀ ▀██▀   █■▀  ▀███    █■▀      ▄█■▀▀▀███\n"
    "  ██  ▄▀ ▀■█▌   █▀          ██     ▐■█▌  █▀       ▐█▄     ▀▀\n"
    " ▐█      ▐▀█▌  ▐▌          ▐█▌     ▐▀██ ▐▌         ▀▀▀█▄█▄▄\n"
    " ■       ██▀   ■            ▀█▄   ▄██▀  ■ ▄▄██▄▄▄ ▄▀▄▄  ▄█▀▀\n"
    " ▀      █▀     ▀               ▀▀▀      ▀▀▀  ▀▀▀   ▀▀▀▀▀▀\n"
    "\n"
   BLUE "1. Lookup\n"
   RESET "choisis ton option : "
);
}

int main()
{
    int i = 1;
    int choice = 0;

    while (i > 0) {
        clearcsl();
        ascii();

        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                clearcsl();
                system("py ./src/python/lookup.py");
                break;

            default:
                clearcsl();
                printf("Choix invalide");
                break;
        }
    }
    return 0;
}