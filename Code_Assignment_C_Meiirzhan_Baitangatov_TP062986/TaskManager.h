struct taskLine
{
    int check;
    char line[1000];
};

struct logWithNum
{
    int Num;
    char tempUsername[30];
};

void pressEnterM(char* error)
{
    printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    printf("%s\t", error);
    printf("\n\t\t\t\t\t\t\tPress enter to continue\n"); // wait the user input
    getch();
    printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}

int userMenu(char username[])
{
    int choice, accountNumber, totalLine;
    struct taskLine l;
    while(1){
        fflush(stdin);
        l.check = 0;
        totalLine = 0;
        printf("\t\t\t\t\t\t     Personal task management\n");
        printf("\t\t\t\t\t\t\tAdd a new Task [1]\n");
        printf("\t\t\t\t\t\t\tView all Tasks [2]\n");
        printf("\t\t\t\t\t\t\tModify a Task [3]\n");
        printf("\t\t\t\t\t\t\tRemove a Task [4]\n");
        printf("\t\t\t\t\t\t\tSort tasks [5]\n");
        printf("\t\t\t\t\t\t\tExit the program [6]\n--->");
        scanf("%d", &choice);
        switch(choice)
        {
        case 1:
            addNewTask(&username);
            break;
        case 2:
            accountNumber = 1;
            ViewAllTasks(&username, &accountNumber);
            break;
        case 3:
            accountNumber = 2;
            ViewAllTasks(&username, &accountNumber); // show the user all tasks
            if(accountNumber == 0) continue; // will continue if there are no tasks
            modifyWhichValue(&l.check, &l.line);
            if(l.check == 0) continue; // will continue if the user have entered 6(which is return back)
            totalLine = countLine();
            modifyTextFile(&username, &accountNumber, l.check, totalLine, &l.line);
            break;
        case 4:
            accountNumber = 3;
            ViewAllTasks(&username, &accountNumber); // show the user all tasks
            if(accountNumber == 0) continue; // will continue if there are no tasks
            l.check = 11;
            totalLine = countLine();
            modifyTextFile(&username, &accountNumber, l.check, totalLine, &l.line);
            pressEnterM("\t\t\t\t\t\t  Your task was successfully deleted");
            break;
        case 5:
            l.check = 12;
            accountNumber = 4;
            ViewAllTasks(&username, &accountNumber); // show the user all tasks
            if(accountNumber == 0) continue; // will continue if there are no tasks
            totalLine = countLine(); // get total lines of the text file
            sortBy(&username, totalLine);
            break;
        case 6:
            exit(EXIT_SUCCESS);
            break;
        default:
            pressEnterM("\n\t\t\t\t\t\t\t     Invalid value\n\a");
            fflush(stdin);
            continue;
        }
    }
    return 0;
}

void addNewTask(char *username[]) //
{
    struct task  //all values that users can input in the task file
    {
        char nameOfTask[100];
        char category[100];
        char status[50];
        char notes[1000];
        char dueTime[20];
    }taskN1;
    fflush(stdin);
    printf("\nEnter the category of your task: ");
    input(&taskN1.category, 100);
    fflush(stdin);
    printf("\nEnter name of your task: ");
    input(&taskN1.nameOfTask, 100);
    fflush(stdin);
    printf("\nAdd any notes if you want: ");
    input(&taskN1.notes, 1000);
    fflush(stdin);
    printf("\nEnter status of your task: ");
    input(&taskN1.status, 50);
    fflush(stdin);
    getDate(&taskN1.dueTime); // adding everything in one line
    FILE * wr;
    wr = fopen("taskFile.txt", "r");
    if(wr == NULL) // if the file does not exist
        {
            wr = fopen("taskFile.txt", "w"); // will create a file
            fprintf(wr, "%s\n%s\n%s\n%s\n%s\n%s\n", *username, taskN1.category, taskN1.nameOfTask, taskN1.dueTime, taskN1.status, taskN1.notes); // adding everything in one line
            fclose(wr);
        }
    else
        {
            wr = fopen("taskFile.txt", "a"); // if the file exists will append the text file
            fprintf(wr, "%s\n%s\n%s\n%s\n%s\n%s\n", *username, taskN1.category, taskN1.nameOfTask, taskN1.dueTime, taskN1.status, taskN1.notes);
            fclose(wr);
        }
    pressEnterM("\t\t\t\t\t\t\tYour Task was successfully added\n");
}

int ViewAllTasks(char *username[], int *accountNumber)
{
    struct taskLine l;
    struct logWithNum lWN;
    int usernameStopCount = 0, checkPoint = 0, taskNumber = 1;
    printf("\n\n");
    lWN.Num = 0;
    FILE * rd;
    rd = fopen("taskFile.txt", "r");
    if(rd == NULL) // check if the text file exists or not
        {
            pressEnterM("\n\t\t\t\t\t\t\tNo tasks were written\n\a");
            *accountNumber = 0;
            fclose(rd);
            return 0;
        }
    while((fgets(l.line, 1000, rd)) != NULL)
        {
            if(lWN.Num != usernameStopCount && checkPoint > 0) // will print values if a username similar
                {
                    switch(lWN.Num)
                    {
                case 1:
                    printf("\t\t\t\t\t\t\tCategory: %s", l.line);
                    break;
                case 2:
                    printf("\t\t\t\t\t\t\tTask Name: %s", l.line);
                    break;
                case 3:
                    printf("\t\t\t\t\t\t\tDue Date: %s", l.line);
                    break;
                case 4:
                    printf("\t\t\t\t\t\t\tStatus: %s", l.line);
                    break;
                case 5:
                    printf("\t\t\t\t\t\t\tNotes: %s\n", l.line);
                    break;
                    }
                }
            else if(lWN.Num == usernameStopCount)
            {
                usernameStopCount = 6; // stop point to check if a username similarity
                lWN.Num = 0; // set lWN.Num to zero to reach to usernameStopCount value
                strcpy(lWN.tempUsername, l.line);
                lWN.tempUsername[strlen(lWN.tempUsername) - 1] = '\0'; // to get rid of '\n' sign
                if(strcmp(lWN.tempUsername, *username) == 0)
                    {
                        printf("\t\t\t\t\t\t\tTask number is %d;\n", taskNumber);
                        printf("\t\t\t\t\t\t\tUsername: %s\n", lWN.tempUsername);
                        taskNumber++; //check if there is a task
                        checkPoint++; // will print the task
                    }
                else checkPoint = 0; // will not print the task
            }
            lWN.Num++;
        }
    fclose(rd);
    if(taskNumber == 1) //
        {
            pressEnterM("\t\t\t\t\t\t\tYou do not have any tasks\a\n");
            *accountNumber = 0;
            return 0;
        }
    if(*accountNumber == 2 || *accountNumber == 3) // ask the user to choose a task that he or she wants to update or delete
        {
        while(1)
            {
            if(*accountNumber == 2)
                {
                    printf("\nChoose the task that you want to modify: ");
                }
            else if(*accountNumber == 3)
                {
                    printf("\nChoose the task that you want to delete: ");
                }
            fflush(stdin);
            scanf("%d", &l.check);
            if(l.check > (taskNumber-1) || l.check <= 0) // if the user input more than tasks it will ask again
                {
                    printf("\n\t\t\t\t\t\t\tEnter correct value\n\a");
                    continue;
                }
            break;
            }
        }
    else
    {
        printf("\t\t\t\t\t\t\tPress enter to continue\n\n\n\n\n\n\n\n");
        getch();
        return 0;
    }
    *accountNumber = l.check; // pass l.check to a pointer
    return 0;
}

int countLine()// will count total lines
{
    FILE *countLine;
    struct taskLine l;
    countLine = fopen("taskFile.txt", "r");
    l.check = 0;
    while((fgets(l.line, 1000, countLine)) != NULL) l.check++;
    fclose(countLine);
    return l.check/6; // one task has 6 lines in the text file, so I divided it into 6 to get the amount of tasks
}

void getDate(char timeDue[]) // take the year month and day from the user
{
    char totalTime[20];
    struct tm timef;
    while(1)
    {
        printf("\nEnter the due year of the task: ");
        scanf("%d", &timef.tm_year);
        if(timef.tm_year >= 2022 && timef.tm_year <= 3000) break;
        pressEnterM("\n\a\t\t\t\t\t\t\t  Enter correct year\n");
        fflush(stdin);
        continue;
    }
    while(1)
    {
        fflush(stdin);
        printf("\nEnter the due month of the task: ");
        scanf("%d", &timef.tm_mon);
        if(timef.tm_mon <= 12 && timef.tm_mon >= 1) break;
        pressEnterM("\n\a\t\t\t\t\t\t\t  Enter correct month\n");
        continue;
    }
    while(1)
    {
        fflush(stdin);
        printf("\nEnter the due day of the task: ");
        scanf("%d", &timef.tm_mday);
        if(timef.tm_mday > 31 || timef.tm_mday < 1)
            {
                pressEnterM("\n\a\t\t\t\t\t\t\t   Enter correct day\n\a");
                continue;
            }
        else if(timef.tm_mday > 30 || timef.tm_mday < 1)
            {
                if(timef.tm_mon == 4 || timef.tm_mon == 6 || timef.tm_mon == 9 || timef.tm_mon == 11)
                {
                    pressEnterM("\n\a\t\t\t\t\t\t\t   Enter correct day\n");
                    continue;
                }
            }
        else if((((timef.tm_year % 4) != 0 && timef.tm_mday > 28) && timef.tm_mon == 2) || (timef.tm_mday > 29 && timef.tm_mon == 2))
            // if February day more than 28 and it is not lean years
            {
                pressEnterM("\n\a\t\t\t\t\t\t\t   Enter correct day\a\n");
                continue;
            }
        break;
    }
    printf("\n");
    sprintf(totalTime, "%d/%d/%d", timef.tm_mday, timef.tm_mon, timef.tm_year); // get all date into one array
    strcpy(timeDue, totalTime); // pass to pointer
}

int input(char value[], int length) // input function helps to take input even with space
{
    int character, count = 0;
    while(1)
    {
        while((character = getchar()) != '\n') // will get characters until the user will enter \n
            {
                if(count < length)
                value[count++] = character;
            }
        if(count == 0) // if the user will not enter nothing it will continue to wait for input
        {
            continue;
        }
        else break;
    }
    value[count] = '\0'; // in order to close an array
    for(int i = strlen(value)-1; i != 0; i--) // to delete space after text
        {
        if(value[i] == ' ')
            value[i] = '\0';
        else break;
        }
    return 0;
}

int modifyWhichValue(int* value, char changeText[]) // ask the user which values to modify
{
    struct taskLine l;
    while(1)
    {
        fflush(stdin);
        printf("\n\n\n\n\n\n\n\n");
        printf("\nTo update category of the task enter [1]");
        printf("\nTo update the task name enter [2]");
        printf("\nTo update due date of the task enter [3]");
        printf("\nTo update status of the task enter [4]");
        printf("\nTo update notes of the task enter [5]");
        printf("\nTo return back enter [6]");
        printf("\n--->");
        scanf("%d", &l.check);
        switch(l.check)
        {
            case 1:
                printf("\nEnter new category: ");
                fflush(stdin);
                input(&l.line, 100);
                break;
            case 2:
                printf("\nEnter a new name for the task: ");
                fflush(stdin);
                input(&l.line, 100);
                break;
            case 3:
                fflush(stdin);
                getDate(&l.line);
                break;
            case 4:
                printf("\nEnter new status of the task: ");
                fflush(stdin);
                input(&l.line, 50);
                break;
            case 5:
                printf("\nEnter new notes: ");
                fflush(stdin);
                input(&l.line, 1000);
                break;
            case 6:
                *value = 0;
                return 0;
            default:
                pressEnterM("\t\t\t\t\t\t\tInvalid value!\a\n");
                fflush(stdin);
                continue;
        }
        break;
    }
    *value = l.check;
    strcpy(changeText, l.line); // pass to pointers
    return 0;
}

int modifyTextFile(char* username[], int* accountLine, int row, int totalLine, char* changeTextFile)
{
    struct taskLine l;
    struct logWithNum lWN;
    char allLines[totalLine][5][100],/*To store all file's values*/ notes[totalLine][1000];
    int countAccountLine = 0, skipOrDeletePoint = 0;
    l.check = 0;
    lWN.Num = 0;
    FILE *rd;
    rd = fopen("taskFile.txt", "r");
    while((fgets(l.line, 1000, rd)) != NULL)
        {
        if (skipOrDeletePoint == 1)
            {
            if(lWN.Num != 6)
                {
                lWN.Num++;
                continue;
                }
            else
            {
                lWN.Num = 0;
                skipOrDeletePoint = 0;
            }
            }
        if(lWN.Num == 0){
            strcpy(lWN.tempUsername, l.line);
            lWN.tempUsername[strlen(lWN.tempUsername) - 1] = 0;
            if(strcmp(*username, lWN.tempUsername) == 0) l.check++; //To count same account tasks
            if(row == 11 && *accountLine == l.check) //TO delete account we skip 5 lines
                {
                totalLine--;
                l.check++;
                skipOrDeletePoint = 1;
                }
            else
                {
                skipOrDeletePoint = 0;
                strcat(lWN.tempUsername, "\n");
                strcpy(allLines[countAccountLine][0], lWN.tempUsername);
                }
        }
        else if(lWN.Num > 0 && lWN.Num <= 5)
            {
            if(row == lWN.Num && *accountLine == l.check)
                {
                strcat(changeTextFile, "\n");
                if(lWN.Num == 5)
                {
                strcpy(notes[countAccountLine], changeTextFile); // to change notes
                }
                else
                {
                strcpy(allLines[countAccountLine][lWN.Num], changeTextFile); // to change the array
                l.check++;
                }
                }
            else if(lWN.Num == 5)
                strcpy(notes[countAccountLine], l.line); // copy line to the notes
            else
                strcpy(allLines[countAccountLine][lWN.Num], l.line); // copy line to the array
            if(lWN.Num == 5)// will start count again
                {
                countAccountLine++;
                lWN.Num = 0;
                continue;
                }
            }
        lWN.Num++;
        }
    fclose(rd);
    FILE * wrd;
    wrd = fopen("taskFile.txt", "w");
    for(int l = 0; totalLine != l; l++){
        fprintf(wrd, "%s%s%s%s%s%s", allLines[l][0], allLines[l][1], allLines[l][2], allLines[l][3], allLines[l][4], notes[l]);
        }
    fclose(wrd);
    return 0;
}

int lowerCase(char* value, char* value1, int len)//compare character base on the ASCII value of the lowercase alphabet
{
    for(int i = 0; i != len; i++)
        {
            if(tolower(value[i]) < tolower(value1[i]))
                return 0;
            else if(tolower(value[i]) > tolower(value1[i])){
                return 1;
            }
            else if(tolower(value[i]) == tolower(value1[i]))
                continue;
        }
    return 0;
}

void swapValue(char* min, char* first) // in order to swap two values
{
    char temp[1000];
    strcpy(temp, min);
    strcpy(min, first);
    strcpy(first, temp);
}

void swapNum(int* min, int* first) // in order to swap two values
{
    int temp;
    temp = *min;
    *min = *first;
    *first = temp;
}


void sortBy(char* username[], int totalLine)
{
    struct taskLine l;
    int count = 1, accCount = 0, sort, intMin = 0, copyTime[totalLine][4], opp;
    char copyArray[totalLine][6][1000];
    while(1)
        {
        printf("\t\t\t\t\t\t\tEnter [1] to sort by category;\n");
        printf("\t\t\t\t\t\t\tEnter [2] to sort by task names;\n");
        printf("\t\t\t\t\t\t\tEnter [3] to sort by Due Date;\n");
        printf("\t\t\t\t\t\t\tEnter [4] to sort by status;\n--->");
        scanf("%d", &sort);
        if(sort>4 || sort < 1)
            {
            pressEnterM("\n\t\t\t\t\t\t\t     Invalid value\n\a");
            fflush(stdin);
            continue;
            }
        break;
        }
    while(1)
        {
        printf("\n\t\t\t\t\t\t\tTo choose Ascending order enter [1]\n");
        printf("\t\t\t\t\t\t\tTo choose Descending Order enter [2]\n--->");
        scanf("%d", &opp);
        if(opp < 1 || opp > 2)
            {
            pressEnterM("\n\t\t\t\t\t\t\t     Invalid value\n\a");
            fflush(stdin);
            continue;
            }
        break;
        }
    FILE * rd;
    rd = fopen("taskFile.txt", "r");
    if(rd == NULL) // check if the text file exists or not
        {
            pressEnterM("\n\t\t\t\t\t\t\t No tasks were written\n\a");
            fclose(rd);
            return 0;
        }
    while((fgets(l.line, 1000, rd) != NULL))
        {
            if(l.check==1) // skip tasks that do not has similar username
                {
                if(count == 6)
                    {
                        count = 1;
                        l.check = 0;
                    }
                else
                    count++;
                continue;
                }
            switch(count)
            {
            case 1:
                l.line[strlen(l.line) - 1] = 0; // to get rid of '\n'
                if(strcmp(*username, l.line) != 0)
                    {
                    l.check = 1;
                    count++;
                    continue;
                    }
                sprintf(copyArray[accCount][0], "%s\n", l.line);
                break;
            case 2:
                strcpy(copyArray[accCount][1], l.line);
                break;
            case 3:
                strcpy(copyArray[accCount][2], l.line);
                break;
            case 4:
                if(sort == 3)
                    {
                        char *p = strtok(l.line, "/");
                        copyTime[accCount][0] = atoi(p);
                        p = strtok(NULL, "/");
                        copyTime[accCount][1] = atoi(p);
                        p = strtok(NULL, "/");
                        copyTime[accCount][2] = atoi(p);
                        copyTime[accCount][3] = accCount;
                        sprintf(copyArray[accCount][3], "%d/%d/%d\n", copyTime[accCount][0], copyTime[accCount][1], copyTime[accCount][2]);
                    }
                else
                    strcpy(copyArray[accCount][3], l.line);
                break;
            case 5:
                strcpy(copyArray[accCount][4], l.line);
                break;
            case 6:
                strcpy(copyArray[accCount][5], l.line);
                count = 0;
                accCount++;
            }
            count++;
        }
    if(opp == 1)
        printf("\nAscending Order: \n");
    else
        printf("\nDescending Order: \n");
    if(sort != 3)
    {
        int min_value;
        for(int x = 0; x < accCount - 1; x++) // selection sort
            {
            min_value = x;
            for(int y = x+1; y < accCount; y++)
                {
                if(lowerCase(copyArray[min_value][sort], copyArray[y][sort], strlen(copyArray[min_value][sort])) == 1)
                        min_value = y;
                }
                for(int fullLine = 0; fullLine < 6; fullLine++){
                    swapValue(&copyArray[min_value][fullLine], &copyArray[x][fullLine]);
                }
            }
        if(opp == 1)
            {
            while(intMin != accCount)
                {//print the tasks
                printf("\t\t\t\t\t\t\tUserName: %s\t\t\t\t\t\t\tCategory: %s\t\t\t\t\t\t\tTask Name: %s\t\t\t\t\t\t\tDue Date: %s\t\t\t\t\t\t\tStatus: %s\t\t\t\t\t\t\tNotes: %s",
                copyArray[intMin][0], copyArray[intMin][1], copyArray[intMin][2], copyArray[intMin][3], copyArray[intMin][4], copyArray[intMin][5]);
                intMin++;
                }
            }
        else if(opp == 2)
            {
            intMin = accCount-1;
            while(intMin != -1)
                {   //print the tasks
                printf("\t\t\t\t\t\t\tUserName: %s\t\t\t\t\t\t\tCategory: %s\t\t\t\t\t\t\tTask Name: %s\t\t\t\t\t\t\tDue Date: %s\t\t\t\t\t\t\tStatus: %s\t\t\t\t\t\t\tNotes: %s",
                copyArray[intMin][0], copyArray[intMin][1], copyArray[intMin][2], copyArray[intMin][3], copyArray[intMin][4], copyArray[intMin][5]);
                intMin--;
            }
            }
    }
    else
    {
        int min_index; // selection sort
        for(int z = 0; z != accCount; z++)
            {
                min_index = z;
            for(int v = z+1; v != accCount; v++)
                {
                    if(opp == 1){
                        if(copyTime[min_index][2] > copyTime[v][2])
                            min_index = v;
                        else if(copyTime[min_index][2] == copyTime[v][2] && ((copyTime[min_index][1] == copyTime[v][1] && copyTime[min_index][0] > copyTime[v][0]) || copyTime[min_index][1] > copyTime[v][1]))
                            min_index = v;
                    }
                    else if(opp == 2){
                        if(copyTime[min_index][2] < copyTime[v][2])
                            min_index = v;
                        else if(copyTime[min_index][2] == copyTime[v][2] && ((copyTime[min_index][1] == copyTime[v][1] && copyTime[min_index][0] < copyTime[v][0]) || copyTime[min_index][1] < copyTime[v][1]))
                            min_index = v;
                    }
                }
                for(int b = 0; b != 4; b++)
                    {
                    swapNum(&copyTime[min_index][b], &copyTime[z][b]); // swap integer array
                    }
                printf("\t\t\t\t\t\t\tUserName: %s\t\t\t\t\t\t\tCategory: %s\t\t\t\t\t\t\tTask Name: %s", copyArray[z][0],
                      copyArray[z][1], copyArray[z][2]);
                printf("\t\t\t\t\t\t\tDue Date: %d/%d/%d\n\t\t\t\t\t\t\tStatus: %s\t\t\t\t\t\t\tNotes: %s", copyTime[z][0],
                copyTime[z][1], copyTime[z][2], copyArray[z][4], copyArray[z][5]);  // print sorted date
            }
    }
    printf("\n\t\t\t\t\t\t\tPress enter to continue");
    getch();
    printf("\n\n\n\n\n\n\n\n\n\n\n\n");
    fclose(rd);
}
