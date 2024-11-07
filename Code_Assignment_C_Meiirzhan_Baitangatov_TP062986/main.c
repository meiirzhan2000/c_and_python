#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include "TaskManager.h"
#include "AccountManager.h"

int main()
{
    struct logWithNum lWN;
    int key;
    while(1)
    {
        printf("\t\t\t\t\t\t-------------------------------------\n");
        printf("\t\t\t\t\t\t>>>Personal Task Management System<<<\n\n");
        printf("\t\t\t\t\t\t\t\tMenu\n");
        printf("\t\t\t\t\t\t\tEnter [1] to log in\n\t\t\t\t\t\t\tEnter [2] to register\n\t\t\t\t\t\t\tEnter [3] to exit\n\n\n--->"); // give a user choose
        scanf("%d", &lWN.Num);
        switch(lWN.Num)
        {
            case 1: loginToSys(&lWN.tempUsername, &key); break; //log in
            case 2: registerNewAccount(&lWN.tempUsername, &key); break; // register
            case 3: exit(EXIT_SUCCESS); break; // exit a program
            default: fflush(stdin);
                     pressEnterM("\t\t\t\t\t\t\t\a     Invalid value\n\a");
                     continue; //invalid value
        }
        if(key == 2) //check if a user log in successfully or not
            return userMenu(lWN.tempUsername);
        else
            {
                pressEnterM("\t\t\t\t\t\t     Invalid username or password\n\a");
                continue;
            }
    }
    return 0;
}

//Meiirzhan Baitangatov TP069286
