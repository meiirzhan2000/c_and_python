struct taskManager //register a user info
{
    char allValue[255];
    char username[30];
    char password[30];
    char firstName[30];
    char secondName[30];
};

void loginAndPass(char logOrPass[], char display[])
{
    while(1)
        {
            printf("%s", display);
            scanf("%s", logOrPass);
            if(strcmp(logOrPass, "e") == 0 || strcmp(logOrPass, "E") == 0) // exit if a user wants to
                exit(EXIT_SUCCESS); // exit this program
            else if(strlen(logOrPass) <= 5){ // check if the value more or equal 5
                pressEnterM("\n\t\t\t\t\t\t\t\tError\a");//produce sound and display error
                fflush(stdin); //clean the input buffer
                continue;
            }
            fflush(stdin);
            break;
        }
}

void loginToSys(char username[], int* key)
{
    char usernameDuplicate[30], password[30];
    char passwordLine[] = "\nEnter Password: ", usernameLine[] = "\nEnter Username: ";
    loginAndPass(&usernameDuplicate, &usernameLine); //pass pointers in order to change value without returning it
    loginAndPass(&password, &passwordLine);
    *key = usernameSimilarityCheck(&usernameDuplicate, 2, &password); // one function was used in order to get password and username similarity
    strcpy(username, usernameDuplicate);// pass username
}

int usernameSimilarityCheck(char value[], int usernameOrSimilarityCheck, char optionalPassword[])//will check if the username is exist
{
    char line[255];
    FILE * read;
    read = fopen("Accounts.txt", "r");
    while((fgets(line, 255, read)) != NULL) // to read each line
        {
            char* p = strtok(line, ":"); // pointer p was created to take the first value which is username. Username:Password:FirstName:SecondName
            if(strcmp(value, p) == 0 && usernameOrSimilarityCheck == 1)
                {
                    return 1; // will return one which means the username has similarity
                }
            else if(strcmp(value, p) == 0 && usernameOrSimilarityCheck == 2)
                p = strtok(NULL, ":"); // will continue splitting one array
                if(strcmp(optionalPassword, p) == 0) // enter as a simple user
                    {
                        pressEnterM("\n\t\t\t\t\t\t      You are successfully log in");
                        return 2;
                    }
        }
    return 0;
}

int checkRegisterValue(char value[], char display[], int length/*Each value will be checked on its own minimum length*/) // will check values
{
    struct logWithNum lWN;// to pass username to another function
    for(int i = 0; i = 20; i++)
        {
            lWN.Num = 0;
            fflush(stdin); // clean input buffer
            printf("\t\t\t\t\t\t\tEnter %s\n--->", display);
            scanf("%s", value);
            if(strcmp(value, "e") == 0 || strcmp(value, "E") == 0) // exit this program
                exit(EXIT_SUCCESS);
            else if(strlen(value) < length) // check length
            {
                pressEnterM("\n\t\t\t\t\t\t\tThe value is too short\a\n");
                continue;
            }
            else if(strcmp(display, "Username") == 0) // // one function was used in order to get password and a username similarity
            {
                strcpy(lWN.tempUsername, value); // will copy username value
                if(usernameSimilarityCheck(&lWN.tempUsername, 1, "Nothing") == 1){
                    pressEnterM("\n\t\t\t\t\t\t   Someone already took this username\n\a");
                    continue;
                }
            }
            else if(strcmp(display, "Your First Name") == 0 || strcmp(display, "Your Second Name") == 0)
                {
                    for(int c = 0; value[c] != '\0';/*end of array*/ c++) // check digits in first and second name
                    {
                        if(isalpha(value[c]) == 0)
                        {
                            lWN.Num = -1;
                            break;
                        }
                    }
                }
            for(int d = 0; value[d] != '\0'; d++) // check values
                {
                    if((value[d] == ':' || value[d] == '\\') || value[d] == '%'){
                        lWN.Num = -1;
                        break;
                    }
                }
            if(lWN.Num == -1)// return back
                 {
                    pressEnterM("\n\t\t\t\t\t\t\tDo Not Include Digit(s)\n\a");
                    continue;
                }
            return 0; // will return back if all conditions satisfied
        }
    pressEnterM("\n\t\t\t\t\t\t\tPlease try again later\n\a");// exit program if a user will not enter the correct value 20 times in a row
    exit(EXIT_SUCCESS);
}
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


void registerNewAccount(char username[], int* key)
{
    struct taskManager log; //register a user info
    printf("\t\t\t\t\t\t\t-----------------------\n");
    printf("\t\t\t\t\t\t\t>>>Registration menu<<<\n\n");
    checkRegisterValue(&log.firstName, "Your First Name", 2); // take all info in order to create account
    checkRegisterValue(&log.secondName, "Your Second Name", 2);
    checkRegisterValue(&log.username, "Username", 4);
    checkRegisterValue(&log.password, "Password", 7);
    sprintf(log.allValue, "%s:%s:%s:%s\n", log.username, log.password, log.firstName, log.secondName);
    FILE * Acc;
    Acc = fopen("Accounts.txt", "r");
    if(Acc == NULL)// if the file will not be found
        {
            Acc = fopen("Accounts.txt", "w"); // create a new file
            fprintf(Acc, "%s", log.allValue);
            fclose(Acc);
        }
    else
        {
            Acc = fopen("Accounts.txt", "a");// append the file
            fprintf(Acc, "%s", log.allValue);
            fclose(Acc);
        }
    pressEnterM("\n\t\t\t\t\t  Your account has been successfully created\n");
    strcpy(username, log.username); // copy a username to a pointer
    *key = 2;
}

