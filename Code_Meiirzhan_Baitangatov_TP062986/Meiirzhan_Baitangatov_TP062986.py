#Meiirzhan Baitangatov
#TP062986
import sys, datetime

def checkFile():#create text file if the files don't exist
    while True:
        try:
            b = open("Admin.txt", "r")
        except:
            with open("Admin.txt", "w") as f:
                f.write("")
        try:
            a = open("CurrentAccountDetails.txt", "r")
        except:
            with open("CurrentAccountDetails.txt", "w") as f:
                f.write("")
        try:
            c = open("SavingAccountDetails.txt", "r")
        except:
            with open("SavingAccountDetails.txt", "w") as f:
                f.write("")
        try:
            d = open("showCheckForAll.txt", "r")
        except:
            with open("showCheckForAll.txt", "w") as f:
                f.write("")
        try:
            s = open("SuperUser.txt", "r")
        except:
            with open("SuperUser.txt", "w") as f:
                f.write("SuperGuest 7777777")
        return mainMenu()

def pressEnter(text):#Design function. Ask user press enter before doing something
    print("\n" * 12)
    print(text.center(118))
    print("PRESS >>>ENTER<<< TO CONTINUE".center(118))
    print("\n" * 12)
    input()

def pressEnterForOne():#design function
    print("PRESS >>>ENTER<<< TO CONTINUE".center(118))
    input()

def mainMenu(): #MAIN MENU#
    print("\n" * 6)
    print(">>>WELCOME TO THE SUPER BANK APPLICATION<<<\n".center(118))
    print(('-' * 43).center(118) + '\n')
    print("Choose the operation from the given options".center(118) + '\n')
    print(('-' * 43).center(118) + '\n')
    print("\n" * 4)
    print("User: Guest\n")
    print("--->Enter [1] to register" + "Enter [5] to leave<---".rjust(97, ' ') + "\n")
    print("--->Enter [2] to log in" + "Enter [4] to make a deposit<---".rjust(98, ' ') + "\n")
    print("--->Enter [3] to withdraw money\n")
    number = str(input("--->"))
    return chooseMove(number)

def chooseMove(take_way):#take a choice from a user#
    if take_way == "1":
        print("\n" * 7)
        print(('_' * 50).center(115) + '\n')
        print("NOTICE!!!".center(116))
        print(('-' * 50).center(115) + '\n')
        print("To create current account you need to pay RM500".center(118))
        print(('-' * 50).center(115) + '\n')
        print("To create saving account you need to pay RM100".center(118))
        print(('-' * 50).center(115) + '\n')
        print("Please choose which account you want to create".center(118))
        print(('-' * 50).center(115) + '\n')
        print("\n" * 7)
        print("--->To create current account enter [1]\n\n--->To create saving account enter [2]\n\n--->To return to main menu please enter [3]\n")
        chooseAcc = str(input("--->"))
        print("\n" * 27)
        if chooseAcc == "1":
            return registerCheck("CurrentAccountDetails.txt", "current")
        if chooseAcc == "2":
            return registerCheck("SavingAccountDetails.txt", "saving")
        elif chooseAcc == "3":
            return mainMenu()
        else:
            pressEnter("Please enter number from given options (1-3)")
            return chooseMove("1")
    elif take_way == "2":
        return loginAccount()
    elif take_way == "3":
        pressEnter("Please log in for withdrawing")
        return loginAccount()
    elif take_way == "4":
        pressEnter("Please log in first")
        return loginAccount()
    elif take_way == "5":
        sys.exit()
    else:
        pressEnter("Please enter number from given options (1-5)")
        return mainMenu()

def addCheck(savingOrCurrent, log, withdrawOrPut, mm, moneydp, minOrPlus):#add a bank receipt
    x = datetime.datetime.today()
    date = x.strftime("%x") #form of date
    time = x.strftime("%X") #form of date
    x = x.strftime("%x %X")
    f = open(chooseTextFile(savingOrCurrent), "r").readlines()
    for i in f:
        i = i.split(" ")
        if i[0] == log:
            login = i[0]
            nameOne = i[2]
            nameTwo = i[3]
            money = i[6]
    deep= open("showCheckForAll.txt", "r")
    g = deep.readlines()
    money = money[:-1]
    note=[]
    found=0
    mm1=mm[:-1]
    for b in g:
        if len(g)==0:
            break
        b = b[:-1].split(" ")
        if b[0] == log:
            found+=1
            b=" ".join(b)
            b = b.strip('\n') + printf("%d%s:%s:%s:%s\n", don.check, don.compName, don.name, don.itemName, don.amountOfitems);" " + str(x) + " " + withdrawOrPut + " " + f"{mm1}({minOrPlus}{moneydp})" + " " + money.strip("\n")
            b=b.split(" ")
        note.append(b)
    if found!=0:
        with open("showCheckForAll.txt", "w") as wr:
            for i in note:
                i=" ".join(i)+"\n"
                wr.write(i)
            wr.close()
    if found==0: #if no items inside showCheckForAll
        d= open("showCheckForAll.txt", "a")
        d.seek(0)
        d.write(login + " " + str(x) + " " + withdrawOrPut + " " + f"{mm1}({minOrPlus}{moneydp})" + " " + money.rstrip('\n')+"\n")
        d.close()
    deep.close()
    showOneCheck(nameOne, nameTwo, date, time, money, withdrawOrPut, moneydp, mm1, minOrPlus)
    print("\n--Press [Enter] to continue--")
    input()
    return mainMenu()

def findCheck(login):#Show transactions of a user (special period time)
    #First input of date#
    print("--->Enter date of transaction that you want to check"+"\n")
    while True:
        try:
            yearStart = int(input("--->Enter year of start(EXAMPLE(21)): "))
            print("\n")
            if yearStart > 99 or yearStart < 21:
                pressEnter("Enter correct year")
                print("\n" * 26)
                continue
            else:
                break
        except:
            pressEnter("Please enter only numbers not a letters")
            print("\n" * 26)
    while True:
        try:
            monthStart = int(input("--->Enter month of start: "))
            print("\n")
            if monthStart < 1 or monthStart > 12:
                pressEnter("Enter correct month")
                print("\n" * 26)
                continue
            else:
                break
        except:
            pressEnter("Please enter only numbers not a letters")
            print("\n" * 26)
    while True:
        try:
            dayStart = int(input("--->Enter day of start: "))
            print("\n")
            if monthStart in [1,3,5,7,8,10,12]:
                if dayStart<1 or dayStart>31:
                    pressEnter("This day doesn't exist")
                    print("\n" * 26)
                    continue
                else:
                    break
            elif monthStart in [4,6,9,11]:
                if dayStart<1 or dayStart>30:
                    pressEnter("This day doesn't exist")
                    print("\n" * 26)
                    continue
                else:
                    break
            elif monthStart == 2:
                if dayStart<1 or dayStart>29:
                    pressEnter("This day doesn't exist")
                    print("\n" * 26)
                    continue
                else:
                    break
        except:
            pressEnter("Please enter only numbers not a letters")
            print("\n" * 26)
    while True:
        try:
            yearEnd = int(input("--->Enter year of end(EXAMPLE(21)): "))
            print("\n")
            if yearEnd > 99 or yearEnd < 21:
                pressEnter("Enter correct year")
                print("\n" * 26)
                continue
            elif yearEnd < yearStart:
                pressEnter("Year start cannot be more than year end")
                print("\n" * 26)
                continue
            else:
                break
        except:
            pressEnter("Please enter only numbers not a letters")
            print("\n" * 26)
    while True:
        try:
            monthEnd = int(input("--->Enter month of end: "))
            print("\n")
            if monthEnd < 1 or monthEnd > 12:
                pressEnter("Enter correct month")
                print("\n" * 26)
                continue
            if yearEnd == yearStart and monthStart > monthEnd:
                pressEnter("The date of start cannot be more than date of end")
                print("\n" * 26)
                continue
            else:
                break
        except:
            pressEnter("Enter only numbers not a letters")
            print("\n" * 26)
    while True:
        try:
            dayEnd = int(input("--->Enter day of end: "))
            print("\n")
            if monthEnd == monthStart and yearEnd == yearStart and dayStart > dayEnd:#check date of start and date of end#
                pressEnter("The date of start cannot be more than date of end")
                print("\n" * 26)
                continue
            elif monthEnd in [1,3,5,7,8,10,12]:
                if dayEnd<1 or dayEnd>31:
                    pressEnter("This day doesn't exist")
                    print("\n" * 26)
                    continue
                else:
                    break
            elif monthEnd in [4,6,9,11]:
                if dayEnd<1 or dayEnd>30:
                    pressEnter("This day doesn't exist")
                    print("\n" * 26)
                    continue
                else:
                    break
            elif monthEnd == 2:
                if dayEnd<1 or dayEnd>29:
                    pressEnter("This day doesn't exist")
                    print("\n" * 26)
                    continue
                else:
                    break
            else:
                pressEnter("Please enter only numbers not a letters")
                print("\n" * 26)
                continue
        except:
            pressEnter("ERROR")
            print("\n" * 26)
    yearStart = "20" + str(yearStart) #Convert date to compare with date into textfile#
    yearEnd = "20" + str(yearEnd)
    datStart = datetime.date(int(yearStart), monthStart, dayStart)
    datEnd = datetime.date(int(yearEnd), monthEnd, dayEnd)
    b = 0
    check= open("showCheckForAll.txt", "r").readlines()
    for i in check:
        i = i.split(" ")
        if i[0] == login:
            le = int(len(i))
            n = 1
            num = 1
            mi = 0
            pl = 0
            while True:
                fff = i[n]
                n += 1
                vv = i[n]
                gg = fff + " " + i[n]
                bbb = datetime.datetime.strptime(gg, '%x %X')
                if bbb.date() >= datStart and bbb.date()<=datEnd:#print the transactions of users in special date by using less, more and equal(>, <, =)#
                    b = 1 #To check transaction#
                    print(f"Check N{str(num)}".center(118)+"\n")
                    num += 1
                    print(f'Date: {fff}'.center(118)+"\n")
                    print(f'Time: {vv}'.center(118)+"\n")
                    n += 1
                    ddd = i[n]
                    n += 1
                    g = i[n]
                    g = g.replace("(", "") #replace to get a number
                    g = g.replace(")", "")
                    q = g.replace("+", " ")
                    mine = "+"
                    try:
                        m, mon = q.split(" ")
                    except:
                        q = g.replace("-", " ")
                        m, mon = q.split(" ")
                        mine = "-"
                    if mine == "-":
                        mi -=int(mon)
                    else:
                        pl += int(mon)
                    print(f"{ddd}: {i[n]}".center(118)+"\n")
                    n += 1
                    print(f"Account balance: {i[n]}".center(118)+"\n")
                    n += 1
                else:
                    n += 4
                if le == n:
                    print("Withdraw: "+str(mi))
                    print("Deposit: +"+str(pl))
                    total = mi + pl#- and - is plus, so i put +
                    print("Total: "+ str(total))
                    break
    if b == 0:
        pressEnter("There have never been any money transactions on this account")
        print("\n" * 26)
    if b != 0:
        print('Press "Enter" to continue')
        input()

def showOneCheck(nameOne, nameTwo, date, time, money, withdrawOrPut, moneydp, mm1, minOrPlus):#Show check after transaction
    print(f"User: {nameOne} {nameTwo}".center(118))
    gg = int(len(nameOne)) + int(len(nameTwo)) + 2
    print(("-"*gg).center(118))
    print(f"Date: {date}".center(118)+"\n")
    print(f"Time: {time}".center(118)+"\n")
    print(f"{withdrawOrPut}: {mm1}({minOrPlus}{moneydp})".center(118)+"\n")
    print(f"Account balance: {money}".center(118)+"\n")
    print(("-"*gg).center(118))
    pass

def showAllCheck(login, nameOne, nameTwo):#Show all transactions of a user
    b = 0
    check= open("showCheckForAll.txt", "r").readlines()
    for i in check:
        i = i.split(" ")
        if i[0] == login:
            b = 1
            le = int(len(i))
            n = 1
            num = 1
            while True: #Print all items inside file
                print(f"Check N{str(num)}".center(118)+"\n")
                num += 1
                print(f'Date: {i[n]}'.center(118)+"\n")
                n += 1
                print(f'Time: {i[n]}'.center(118)+"\n")
                n += 1
                ddd = i[n]
                n += 1
                print(f"{ddd}: {i[n]}".center(118)+"\n")
                n += 1
                print(f"Account balance: {i[n]}".center(118)+"\n")
                n += 1
                if le == n: #Break the loop
                    break
            break
    if b == 0:
        pressEnter("There have never been any money transactions on this account")
        print("\n"*26)
    if b != 0:
        pressEnterForOne()
        print("\n"*26)

def loginAccount():##Login Into system
    print("\n" * 26)
    while True:
        login = str(input("Enter your ID: "))
        if len(login) < 1:
            pressEnter("Please enter your ID")
            print("\n" * 26)
            continue
        else:
            break
    print(" ")
    while True:
        password = str(input("Enter your password: "))
        if len(password) < 1:
            pressEnter("Please enter your ID")
            print("\n" * 26)
            continue
        else:
            break
    save = 0
    current = 0
    for l in open("SavingAccountDetails.txt","r").readlines(): #check each text file to get a similar password and ID
        userInfoSave = l.split(" ")
        save += 1
        if login == userInfoSave[0] and password == userInfoSave[1]:
            save -= 1
            print("\n" * 13)
            pressEnter("Log in successfully")
            print("\n" * 27)
            return accessUser("saving", save, password, login, userInfoSave[2], userInfoSave[3])
    for i in open("CurrentAccountDetails.txt","r").readlines():
        userInfoCurrent = i.split(" ")
        current += 1
        if login == userInfoCurrent[0] and password == userInfoCurrent[1]:
            current -= 1
            print("\n" * 13)
            pressEnter("Log in successfully")
            print("\n" * 27)
            return accessUser("current", current, password, login, userInfoCurrent[2], userInfoCurrent[3])
    for a in open("Admin.txt","r").readlines():
        adminInfo = a.split(" ")
        if login == adminInfo[0] and password == adminInfo[1]:
            print("\n" * 13)
            pressEnter("Log in successfully")
            print("\n" * 27)
            return adminMenu(adminInfo[2], adminInfo[3])
    for j in open("SuperUser.txt","r").readlines():
        superUserInfo = j.split(" ")
        if login == superUserInfo[0] and password == superUserInfo[1]:
            print("\n" * 13)
            pressEnter("Log in successfully")
            print("\n" * 27)
            return SuperUserMenu()
    pressEnter("The ID or password incorrect") # if nothing was found
    print("\n" * 26)
    return loginAccount()

def userAccountDetails(savingOrCurrent, indexx, password, log, name1, name2):#check and change data of a user
    nameOfUser(name1, name2) #each list for each item in the textfile#
    login = []
    password1 = []
    firstName = []
    secondName = []
    ID = []
    gender = []
    money = []
    ind = indexx
    if savingOrCurrent == "current":
        readFile = open('CurrentAccountDetails.txt', 'r')
    else:
        readFile = open('SavingAccountDetails.txt', 'r')
    for i in readFile:
        loginAdd, passwordAdd, firstNameAdd, secondNameAdd, IDadd, genderAdd, moneyAdd = i.split(" ")
        #append each list#
        ID.append(IDadd)
        login.append(loginAdd)
        password1.append(passwordAdd)
        firstName.append(firstNameAdd)
        secondName.append(secondNameAdd)
        gender.append(genderAdd)
        money.append(moneyAdd)
    readFile.close()
    print("--->ID: " + login[ind] + "\n") #get data of user by using index#
    print("--->Password: " + password1[ind]+ "\n")
    print("--->First Name: " + firstName[ind]+ "\n")
    print("--->Second Name: " + secondName[ind]+ "\n")
    print("--->Identity number: " + ID[ind]+ "\n")
    print("--->Gender: " + gender[ind] + "\n")
    print("--->Checking account: " + money[ind]+ "\n")
    print("\n"*3)
    print("--->To change ID enter [1]")
    print("--->To change password enter [2]")
    print("--->To see all transactions enter [3]")
    print("--->To return to access menu enter [4]")
    print("--->To leave the account enter [5]")
    try:
        choosen = int(input("--->"))
    except:
        print("try again")
        return userAccountDetails(savingOrCurrent, indexx, password, log, name1, name2)
    if choosen == 1:
        print("\n" * 26)
        while True:
            print("--->Enter your new ID")
            newLogin = str(input("--->"))
            print("--->Enter your new ID again")
            loginCheck = str(input("--->"))
            if newLogin != loginCheck:
                pressEnter("--->ID doesn't match")
                print("\n" * 26)
                continue
            elif checkName(newLogin) == True:
                pressEnter("This ID already taken")
                print("\n" * 26)
                continue
            elif len(newLogin) <= 4:
                pressEnter("--->ID too short")
                print("\n" * 26)
                continue
            else:
                changeLoginOrPassword(savingOrCurrent, newLogin, log, password)
                pressEnter('ID successfully changed')
                print("\n" * 26)
                break
        return mainMenu()
    elif choosen == 2:
        print("\n" * 26)
        while True:
            print("--->Enter your new password")
            passwordNew = str(input("--->"))
            print("--->Enter your new password again")
            passwordCheck = str(input("--->"))
            if passwordNew != passwordCheck:
                pressEnter("--->Passwords don't match")
                print("\n" * 26)
                continue
            elif len(passwordNew) <= 4:
                pressEnter("Password too short")
                print("\n" * 26)
                continue
            else:
                changeLoginOrPassword(savingOrCurrent, passwordNew, password, log)
                pressEnter('Password successfully changed')
                print("\n" * 26)
                break
        return mainMenu()
    elif choosen == 3:
        showAllCheck(log, firstName[ind], secondName[ind])
        return accessUser(savingOrCurrent, indexx, password, log, name1, name2)
    elif choosen == 4:
        return accessUser(savingOrCurrent, indexx, password, log, name1, name2)
    elif choosen == 5:
        return mainMenu()
    else:
        pressEnter("--->Enter one of the given numbers")
        return userAccountDetails(savingOrCurrent, indexx, password, log, name1, name2)

def putMoneyOnDeposite(saveOrCurrent, indexx, password, log, name1, name2):#deposit
    nameOfUser(name1, name2)
    n=0
    readFile = open(chooseTextFile(saveOrCurrent), 'r')
    text = readFile.readlines()
    index = indexx+1
    for i in text:
        i = i.split(" ")
        n += 1
        if index == n:
            mon = i[6]
            log = i[0]
            passw = i[1]
    while True:
        print("\n"*27)
        print(">>>DEPOSITE<<<".center(118))
        print("\n"*4)
        nameOfUser(name1, name2)
        print("\n")
        print("--->Checking account: " + i[6] + "\n")
        print("--->Enter [1] to deposit 100 RM" + "Enter [5] to deposit 300 RM<---".rjust(95, " ")+ "\n")
        print("--->Enter [2] to deposit 150 RM" + "Enter [6] to deposit 500 RM<---".rjust(95, " ")+ '\n')
        print("--->Enter [3] to deposit 200 RM" + "Enter [7] to deposit another amount<---".rjust(95, " ")+ "\n")
        print("--->Enter [4] to deposit 250 RM" + "Enter [8] to return to the user main menu<---".rjust(95, " ")+ "\n")
        print("\n")
        try:
            choose = int(input("--->"))
        except:
            print("try again")
            continue
        if choose == 1:
            if checkFullAmount(saveOrCurrent, mon, 100) == True:
                continue
            newMoney = int(mon) + 100
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "deposit", mon, 100, "+")
            break
        elif choose == 2:
            if checkFullAmount(saveOrCurrent, mon, 150) == True:
                continue
            newMoney = int(mon) + 150
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "deposit", mon, 150, "+")
            break
        elif choose == 3:
            if checkFullAmount(saveOrCurrent, mon, 200) == True:
                continue
            newMoney = int(mon) + 200
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "deposit", mon, 200, "+")
            break
        elif choose == 4:
            if checkFullAmount(saveOrCurrent, mon, 250) == True:
                continue
            newMoney = int(mon) + 250
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "deposit", mon, 250, "+")
            break
        elif choose == 5:
            if checkFullAmount(saveOrCurrent, mon, 300) == True:
                continue
            newMoney = int(mon) + 300
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "deposit", mon, 300, "+")
            break
        elif choose == 6:
            if checkFullAmount(saveOrCurrent, mon, 500) == True:
                continue
            newMoney = int(mon) + 500
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "deposit", mon, 500, "+")
            break
        elif choose == 7:
            depositMoney = int(input(("Enter how much money you want to deposit: ")))
            if checkFullAmount(saveOrCurrent, mon, depositMoney) == True:
                continue
            newMoney = depositMoney + int(mon)
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "deposit", mon, depositMoney, "+")
            pressEnter("The operation was successfully done")
            break
        elif choose == 8:
            return accessUser(saveOrCurrent, indexx, password, log, name1, name2)
        else:
            pressEnter("Please enter one of the given options")
            continue
    while True:
        print("To continue working with the account enter [1]".center(118)+ "\n")
        print("To leave enter [2]".center(118))
        try:
            chooseLeave = int(input())
        except:
            print("Try again")
            continue
        if chooseLeave == 1:
            return accessUser(saveOrCurrent, indexx, password, log, name1, name2)
        elif chooseLeave == 2:
            return mainMenu()
        else:
            pressEnter('"ERROR" try again')
            print("\n" * 26)
            continue

def checkFullAmount(saveOrCurrent, mon, putMoney):#Chech money depends on user account (current or saving)
    if saveOrCurrent == "current":
        checkMoney = 100000
    elif saveOrCurrent == "saving":
        checkMoney = 10000
    full = int(mon) + putMoney
    if full > checkMoney:
        left = checkMoney - int(mon)
        print("\n"*13)
        print(f"Your {saveOrCurrent} account can have {str(checkMoney)} RM".center(118))
        print(f"You can deposit only {left} RM".center(118))
        print("Press enter to continue".center(118))
        print("\n"*13)
        input()
        return True
    pass

def checkName(login):#Check the name inside each textfile by splitting each line and compare index 0 which is ID index
    for l in open("SavingAccountDetails.txt","r").readlines():
        userInfoSave = l.split(" ")
        if login == userInfoSave[0]:
            return True
    for i in open("CurrentAccountDetails.txt","r").readlines():
        userInfoCurrent = i.split(" ")
        if login == userInfoCurrent[0]:
            return True
    for a in open("Admin.txt","r").readlines():
        adminInfo = a.split(" ")
        if login == adminInfo[0]:
            return True
    for j in open("SuperUser.txt","r").readlines():
        superUserInfo = j.split(" ")
        if login == superUserInfo[0]:
            return True
    pass


def checkMoney(saveOrCurrent, money, moneyM):#current and saving must have at least 500 and 100 RG(respectively) in account#
    if saveOrCurrent == "current":
        checkMoney = 500
    elif saveOrCurrent == "saving":
        checkMoney = 100
    mon = int(money) - moneyM
    if int(mon) < checkMoney:
        print("\n"*13)
        print(f"You must have at least {str(checkMoney)} in your account".center(118))
        print("Press enter to continue".center(118))
        print("\n"*13)
        input()
        return True

def withdrawMoney(saveOrCurrent, indexx, password, log, name1, name2):
    n=0
    readFile = open(chooseTextFile(saveOrCurrent), 'r')
    text = readFile.readlines()
    index = indexx+1
    for i in text:
        i = i.split(" ")
        n += 1
        if index == n:
            mon = i[6]
            log = i[0]
            passw = i[1]
    while True:
        print("\n"*27)
        print(">>>WITHDROW<<<".center(118))
        print("\n"*4)
        nameOfUser(name1, name2)
        print("\n")
        print("--->Checking account: " + i[6]+"\n")
        print("--->Enter 1 to withdraw 100 RM" + "Enter 5 to withdraw 300 RM<---".rjust(92, " ")+"\n")
        print("--->Enter 2 to withdraw 150 RM" + "Enter 6 to withdraw 500 RM<---".rjust(92, " ")+"\n")
        print("--->Enter 3 to withdraw 200 RM" + "Enter 7 to withdraw another amount<---".rjust(92, " ")+ "\n")
        print("--->Enter 4 to withdraw 250 RM" + "Enter 8 to return back <---".rjust(92)+ "\n")
        print("\n")
        try:
            choose = int(input("--->"))
        except:
            print("try again")
            continue
        if choose == 1:
            if checkMoney(saveOrCurrent, mon, 100) == True:
                return withdrawMoney(saveOrCurrent, indexx, password, log, name1, name2)
            newMoney = int(mon) - 100
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "withdraw", mon, 100, "-")
            break
        elif choose == 2:
            if checkMoney(saveOrCurrent, mon, 150) == True:
                return withdrawMoney(saveOrCurrent, indexx, password, log, name1, name2)
            newMoney = int(mon) - 150
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "withdraw", mon, 150, "-")
            break
        elif choose == 3:
            if checkMoney(saveOrCurrent, mon, 200) == True:
                return withdrawMoney(saveOrCurrent, indexx, password, log, name1, name2)
            newMoney = int(mon) - 200
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "withdraw", mon, 200, "-")
            break
        elif choose == 4:
            if checkMoney(saveOrCurrent, mon, 250) == True:
                return withdrawMoney(saveOrCurrent, indexx, password, log, name1, name2)
            newMoney = int(mon) - 250
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "withdraw", mon, 250, "-")
            break
        elif choose == 5:
            if checkMoney(saveOrCurrent, mon, 300) == True:
                return withdrawMoney(saveOrCurrent, indexx, password, log, name1, name2)
            newMoney = int(mon) - 300
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "withdraw", mon, 300, "-")
            break
        elif choose == 8:
            return accessUser(saveOrCurrent, index, password, log, name1, name2)
        elif choose == 6:
            if checkMoney(saveOrCurrent, mon, 500) == True:
                return withdrawMoney(saveOrCurrent, indexx, password, log, name1, name2)
            newMoney = int(mon) - 500
            changeMoney(saveOrCurrent, log, passw, newMoney)
            addCheck(saveOrCurrent, log, "withdraw", mon, 500, "-")
            break
        elif choose == 7:
            while True:
                try:
                    withdr = int(input("Please enter how much money you want to withdraw: "))
                except:
                    print("try again")
                    continue
                change = withdr % 10  # if withdr have change as 1, and 5 RG
                if checkMoney(saveOrCurrent, mon, withdr) == True:
                    while True:
                        print("To continue enter [1]".center(118))
                        print("To return to main menu enter [2]".center(118))
                        try:
                            chooseReturn = int(input())
                        except:
                            print("try again")
                            continue
                        if chooseReturn == 1:
                            print("\n")
                            return withdrawMoney(saveOrCurrent, indexx, password, log, name1, name2)
                        elif chooseReturn == 2:
                            return accessUser(saveOrCurrent, indexx, password, log, name1, name2)
                        else:
                            pressEnter("Try again")
                            print("\n" * 26)
                            continue
                elif withdr < 50:
                    pressEnter("User must withdraw at least 50 RM")
                    print("\n" * 26)
                    continue
                if change >= 1:
                    g = False
                    giveOption = withdr - change # give a option to choose another amount
                    giveOptionHigh = giveOption + 10
                    if checkMoney(saveOrCurrent, mon, giveOptionHigh) == True: #check whether the option is for the money in the user's account to be not less than 500 or 100 RG
                        print(f"The terminal doesn't have low money such as {change}RM".center(118))
                        print(f"Maybe you want to withdraw {giveOption}".center(118)+"\n")
                        g = True
                    else:
                        print(f"The terminal doesn't have low money such as {change}RM".center(118))
                        print(f"Maybe you want to withdraw {giveOption} or {giveOptionHigh}".center(118)+"\n")
                    while True:
                        print(f"To return to the main menu enter [1]".center(118)+"\n")
                        print(f"To choose {giveOption} enter [2]".center(118)+"\n")
                        if g != True:
                            print(f"To choose {giveOptionHigh} enter [3]".center(118)+"\n")
                        print("\n"*4)
                        try:
                            chooseMoney = int(input("--->"))
                        except:
                            print("try again")
                            continue
                        if chooseMoney == 2:
                            withdr = giveOption
                            s = True
                            break
                        elif chooseMoney == 3 and g != True:
                            withdr = giveOptionHigh
                            s = True
                            break
                        elif chooseMoney == 1:
                            return accessUser(saveOrCurrent, indexx, password, log, name1, name2)
                        else:
                            pressEnter("Please choose one of the given options")
                            continue
                elif change == 0:
                    s = True
                if s == True:
                    break
                else:
                    pressEnter('"ERROR" Try again')
                    return withdrawMoney(saveOrCurrent, indexx, password, log, name1, name2)
        else:
            pressEnter('"ERROR" Try again')
            print("\n" * 27)
            continue
        break
    if s == True:
        m = int(mon) - withdr
        changeMoney(saveOrCurrent, log, passw, m)
        addCheck(saveOrCurrent, log, "withdraw", mon, withdr, "-")
    readFile.close()
    while True:
        print("--->To continue working with the account enter [1]")
        print("--->To leave enter [2]")
        try:
            chooseLeave = int(input("--->"))
        except:
            print("Try again")
            continue
        if chooseLeave == 1:
            return accessUser(saveOrCurrent, indexx, password, log, name1, name2)
        elif chooseLeave == 2:
            return mainMenu()
        else:
            pressEnter('"ERROR" try again')
            print("\n"*27)
            continue

def registerCheck(text, savingOrCurrent): #Register current and saving user#
    readFile = open(text, "r")
    re = readFile.readlines()
    b = len(re)
    while True:
        print("--->Please enter your name")
        userFirstName = input("--->")
        print("\n")
        if any(char.isdigit() for char in userFirstName):
            pressEnter("Please do not write digits or numbers in your name.")
            print("\n" * 27)
            continue
        elif len(userFirstName) < 2:
            continue
        break
    while True:
        print("--->Please enter your second name")
        userSecondName = str(input("--->"))
        print("\n")
        if any(char.isdigit() for char in userSecondName):
            pressEnter("Please do not write numbers in your name.")
            print("\n" * 27)
            continue
        if len(userSecondName) < 2:
            continue
        break
    print("The identity number must have 12 numbers!".center(118)+"\n")
    while True:
        ID = str(input("--->Please enter your identity number: "))
        if len(ID) != 12:
            pressEnter("The identity number must have 12 numbers!")
            print("\n" * 27)
            continue
        elif checkID(ID, savingOrCurrent) == True:
            pressEnter("This identity number already taken")
            print("\n" * 27)
            continue
        else:
            break
    print("\n" * 2)
    while True:
        print("Please choose gender".center(118))
        print(("-" * 21).center(118))
        print("If you are male enter [1]".center(118) +"\n\n" + "If you are female enter [2]".center(118))
        gender = str(input("--->"))
        if gender == "1":
            userGender = "male"
            break
        elif gender == "2":
            userGender = "female"
            break
        else:
            pressEnter("Please enter [1] or [2]")
            print("\n" * 27)
            continue
    print("\n" * 26)
    login = randomLogin(b, savingOrCurrent)
    passwordOne = randomPassword(ID, userFirstName, userSecondName)
    if savingOrCurrent == "current":
        money = "500"
    else:
        money = "100"
    with open(text, "a") as appendAccount:
        appendAccount.write(login + " " + passwordOne + " " + userFirstName + " " + userSecondName + " " + ID + " " + userGender + " " + str(money) + "\n")#'\n' help to start with a new line
    print("Your account successfully register".center(118))
    print(("-" * 36).center(118))
    print(f"It is your ID: {login}".center(118), "\n", f"It is your password: {passwordOne}".center(118))
    print("\n" * 13)
    pressEnterForOne()
    print("\n" * 13)
    return mainMenu()

def randomLogin(b, savingOrCurrent): #Give an ID depends on an index of a user#
    return str(14320658321+b)

def randomPassword(ID, name1, name2): #Give random password to a user by using identity number, first name, second name#
    g=""
    nam = name1
    nam2 = name2
    if len(nam) < 4 and len(nam2) < 4:
        while True:
            if len(nam) < 4:
                nam = nam + nam
            elif len(nam2) < 4:
                nam2 = nam2 + nam2
            elif len(nam)>=4 and len(nam2)>=4:
                break
    for i in range(0, 4, 1):
        g += ID[i] + nam[i] + nam2[i]
    return g

def checkID(newID, savingOrCurrent):#check identity number of a user
    g = open(chooseTextFile(savingOrCurrent),"r").readlines()
    if len(g) < 1:
        return False
    for l in g:
        userInfoSave = l.split(" ")
        if newID == userInfoSave[4]:
            return True
    return False

def accessUser(saveOrCurrent, index, password, log, name1, name2): #Main menu for current and saving account#
    print("\n"*27)
    print(f">>>{saveOrCurrent} MENU<<<".upper().center(118))
    print("\n" * 3)
    nameOfUser(name1, name2)
    print("\n" * 2)
    print("--->Enter 1 if you want to withdraw money\n")
    print("--->Enter 2 if you want to make a deposit\n")
    print(f"--->Enter 3 if you want to see your {saveOrCurrent} account iformation"+"\n")
    print("--->Enter 4 if you want to see special date of check\n")
    print("--->Enter 5 if you want to return to main menu\n")
    choose = str(input("--->"))
    if choose == "1":
        return withdrawMoney(saveOrCurrent, index, password, log, name1, name2)
    elif choose == "2":
        return putMoneyOnDeposite(saveOrCurrent, index, password, log, name1, name2)
    elif choose == "3":
        return userAccountDetails(saveOrCurrent, index, password, log, name1, name2)
    elif choose == "4":
        print("\n"*27)
        findCheck(log)
        return accessUser(saveOrCurrent, index, password, log, name1, name2)
    elif choose == "5":
        return mainMenu()
    else:
        pressEnter("Please enter one of the given numbers")
        return accessUser(saveOrCurrent, index, password, log, name1, name2)

def changeLoginOrPassword(savingOrCurrent, newLogOrPassword, logOrPassword, add): #change ID and password by using replace#
    f = open(chooseTextFile(savingOrCurrent), "r")
    d = f.readlines()
    changeAppend=[]
    q = 0
    for i in d:
        i=i[:-1].split(" ")
        if i[0] == logOrPassword and i[1] == add: #for changing ID. 'add' is password
            q = 1
            i = " ".join(i)
            i = i.replace(logOrPassword, newLogOrPassword)
            i = i.split(" ")
        elif i[1] == logOrPassword and i[0] == add: #for changing password. 'add' is ID
            i = " ".join(i)
            i = i.replace(logOrPassword, newLogOrPassword)
            i = i.split(" ")
        changeAppend.append(i)
    if q == 1: # if ID was changed, the ID inside 'showCheckForAll' file will be changed as well
        g = open("showCheckForAll.txt", "r")
        d = g.read()
        d = d.replace(logOrPassword, newLogOrPassword)
        with open("showCheckForAll.txt", "w") as s:
            s.write(d)
    with open(chooseTextFile(savingOrCurrent), "w") as write:
        for detail in changeAppend:
            detail=" ".join(detail)+"\n"
            write.write(detail)
        write.close()

def deleteAccount(savingOrCurrent, login, password):#delete bank account with transactions of a user by using continue#
    dddd = open(savingOrCurrent, "r")
    data = dddd.readlines()
    accountAppend=[]
    for d in data:
        d=d[:-1].split(" ")
        if login == d[0] and password == d[1]:#skip account which admin or superUser want to delete by using continue#
            continue
        else:
            accountAppend.append(d) #append into the list#
    with open(savingOrCurrent, "w") as write:
        for detail in accountAppend:
            detail=" ".join(detail)+"\n"
            write.write(detail)
        write.close()
    g = open("showCheckForAll.txt", "r+")
    dddddd = g.readlines()
    g.seek(0)
    for i in dddddd:
        b = i.split(" ")
        if b[0] != login:
            g.write(i)
    g.truncate()
    g.close()

def changeMoney(savingOrCurrent, login, password, newMoney):#change money of a user
    ddddd=open(chooseTextFile(savingOrCurrent), "r")
    data = ddddd.readlines()
    moneyAppend=[]
    for d in data:
        d=d[:-1].split(" ")
        if login == d[0] and password == d[1]:
            d[6]=str(newMoney)
        moneyAppend.append(d)
    ddddd.close()
    with open(chooseTextFile(savingOrCurrent), "w") as write:
        for detail in moneyAppend:
            detail=" ".join(detail)+"\n"
            write.write(detail)
        write.close()

def SuperUserMenu():#SuperUser menu
    while True:
        print("\n"*27)
        print("Hello, Super User".center(118))
        print("\n" * 4)
        print("------------------")
        print("--->To add admin enter [1]"+"\n")
        print("--->To show all admin enter [2]"+"\n")
        print("--->To check and change data of user enter [3]"+"\n")
        print("--->To log out enter [4]"+"\n")
        choose = input("--->")
        print("\n" * 27)
        if choose == "1":
            return createAdmin()
        elif choose == "2":
            return showAllAdmins()
        elif choose == "3":
            return showDate("super user", "SuperUser", "Super", "User")
        elif choose == "4":
            return mainMenu()
        else:
            pressEnter("Enter one of the given options")
            continue


def createAdmin():#create admin by using simple input and append textfile#
    while True:
        Name = input("Please enter name of the admin: ")
        print("\n")
        if any(char.isdigit() for char in Name):
            pressEnter("Please do not include digits and numbers in your name.")
            print("\n" * 27)
            continue
        elif len(Name) < 2:
            pressEnter("Try again")
            print("\n" * 27)
            continue
        break
    while True:
        secondName = input("Please enter second name of the admin: ")
        print("\n")
        if any(char.isdigit() for char in secondName):
            pressEnter("Please do not include numbers in your second name.")
            print("\n" * 27)
            continue
        elif len(secondName) < 2:
            pressEnter("Try again")
            print("\n" * 27)
            continue
        break
    while True:
        login = input("Please enter ID of the admin: ")
        print("\n")
        if checkName(login) == True:
            pressEnter("This ID already taken")
            print("\n"* 27)
            continue
        elif len(secondName) < 2:
            pressEnter("Try again")
            print("\n" * 27)
            continue
        break
    while True:
        password = input("Please enter password for admin: ")
        print("\n")
        if len(password) < 4:
            pressEnter("Password is too short")
            print("\n" * 27)
            continue
        break
    with open("Admin.txt", "a") as appendAccount:
        appendAccount.write(login + " " + password + " " + Name + " " + secondName + "\n")
    print(f"Your new admin ({Name} {secondName}) successfully register")
    pressEnterForOne()
    return SuperUserMenu()


def showAllAdmins():#show all admins by looping each line as a list
    n=0
    readFile = open('Admin.txt', 'r')
    text = readFile.readlines()
    for i in text:
        n += 1
        i = i.split(" ")
        print(f"Account number N{n}")
        print("-"*30)
        print("--->ID: " + i[0]+"\n")
        print("--->Password: " + i[1]+"\n")
        print("--->First Name: " + i[2]+"\n")
        print("--->Second Name: " + i[3]+"\n")
    readFile.close()
    while True:
        print("--->Enter [1] to return to super user menu"+"\n")
        print("--->Enter [2] to change data of admins")
        try:
            choose = int(input("--->"))
        except:
            print("try again")
            continue
        if choose == 1:
            return SuperUserMenu()
        elif choose == 2:
            while True:
                try:
                    chooseNumber = int(input("Please choose number of the user which you want to change: "))
                except:
                    print("try again")
                    continue
                if chooseNumber > len(text):
                    continue
                print("\n"*27)
                print("Please Enter [1] to change ID of admin")
                print("Please Enter [2] to change password of admin")
                print("Please Enter [3] to delete the admin")
                try:
                    chooseWay = int(input("--->"))
                except:
                    print("try again")
                    continue
                if chooseWay == 1 or chooseWay == 2 or chooseWay == 3:
                    findUserAdmin(chooseNumber, chooseWay)
                    if chooseWay == 1:
                        way = "The ID"
                    elif chooseWay == 2:
                        way = "The password"
                    elif chooseWay == 3:
                        pressEnter("the account was deleted successfully")
                        print("\n"*27)
                        return SuperUserMenu()
                    print("\n"*27)
                    print(f"{way} was changed successfully".center(118))
                    pressEnterForOne()
                    return SuperUserMenu()
                else:
                    pressEnter("Invalid value, Try again")
                    print("\n"*27)
                    continue
        else:
            pressEnter("Invalid value, Try again")
            print("\n"*27)
            continue


def findUserAdmin(f, passwordOrLogin):#change password or ID, and delete admin
    n=0
    readFile = open('Admin.txt', 'r')
    text = readFile.readlines()
    for i in text:
        n += 1
        i = i.split(" ")
        if f == n:
            print(f"Account number N{n}")
            print("-"*30)
            print("--->ID: " + i[0]+"\n")
            print("--->Password: " + i[1]+"\n")
            print("--->First Name: " + i[2]+"\n")
            print("--->Second Name: " + i[3]+"\n")
            while True:
                if passwordOrLogin == 1:
                    print(f"Please enter new ID for {i[2]} {i[3]}")
                    newLogin = input("--->")
                    if checkName(newLogin) == True:
                        pressEnter("This ID already taken")
                        print("\n"*27)
                        continue
                    if len(newLogin) < 4:
                        pressEnter("The ID too short")
                        print("\n"*27)
                        continue
                    return changeLoginOrPassword("Admin.txt", newLogin, i[0], i[1])
                if passwordOrLogin == 2:
                    print(f"Please enter new password for {i[2]} {i[3]}")
                    newPassword = input("--->")
                    if len(newPassword) < 4:
                        pressEnter("The ID too short")
                        print("\n"*27)
                        continue
                    return changeLoginOrPassword("Admin.txt", newPassword, i[1], i[0])
                if passwordOrLogin == 3:
                    return deleteAccount("Admin.txt", i[0], i[1])

def userFind(savingOrCurrent, f, passwordOrLogin, Return, nameAdmin, surNameAdmin):#check and change data of a user
    n=0
    if savingOrCurrent == "SavingAccountDetails.txt":
        ff = "saving"
    else:
        ff = "current"
    readFile = open(savingOrCurrent, "r")
    text = readFile.readlines()
    for i in text:
        n += 1
        i = i.split(" ")
        if f == n:
            print(f"Account number N{n}")
            print("-"*30)
            print("--->ID: " + i[0]+"\n")
            print("--->Password: " + i[1]+"\n")
            print("--->First Name: " + i[2]+"\n")
            print("--->Second Name: " + i[3]+"\n")
            print("--->identity number: " + i[4]+"\n")
            print("--->Gender: " + i[5]+"\n")
            print("--->Checking account: " + i[6]+"\n")
            name = i[2]
            secondName = i[3]
            while True:
                if passwordOrLogin == "1":
                    newLogin = input(f"Please enter new ID for {name} {secondName}: ")
                    if checkName(newLogin) == True:
                        pressEnter("This ID already taken")
                        print("\n"*27)
                        continue
                    if len(newLogin) < 4:
                        pressEnter("The ID too short")
                        print("\n"*27)
                        continue
                    changeLoginOrPassword(ff, newLogin, i[0], i[1])
                    break
                elif passwordOrLogin == "2":
                    newPassword = input(f"Please enter new password for {name} {secondName}: ")
                    if len(newPassword) < 4:
                        pressEnter("The password too short")
                        print("\n"*27)
                        continue
                    changeLoginOrPassword(ff, newPassword, i[1], i[0])
                    break
                elif passwordOrLogin == "3":
                    newMoney = int(input(f"Please enter new sum of money for {name} {secondName}: "))
                    if checkMoney(ff, newMoney, 0) == True or checkFullAmount(ff, newMoney, 0) == True:
                        pressEnter("ERROR")
                        print("\n"*27)
                        continue
                    changeMoney(ff, i[0], i[1], newMoney)
                    break
                elif passwordOrLogin == "4":
                    deleteAccount(savingOrCurrent, i[0], i[1])
                    break
                elif passwordOrLogin == "5":
                    showAllCheck(i[0], i[2], i[3])
                    break
                elif passwordOrLogin == "6":
                    findCheck(i[0])
                    break

def adminMenu(nameAdmin, surNameAdmin):#Admin menu#
    while True:
        print("\n"*13)
        print(f"Welcome {nameAdmin} {surNameAdmin}".center(118))
        print("\n"*3)
        print("--->To check and change data of users enter [1]")
        print("--->To leave from admin account enter [2]")
        try:
            choose = int(input())
        except:
            print("try again")
            continue
        if choose == 1:
            print("\n"*27)
            return showDate("admin", "Admin", nameAdmin, surNameAdmin)
        elif choose == 2:
            return mainMenu()
        else:
            pressEnter("Please choose one of the given options")
            print("\n"*27)
            continue

def showDate(whoUsing, Return, nameAdmin, surNameAdmin): #check and correct user information
    while True:
        nameOfUser(nameAdmin, surNameAdmin)
        print("\n"*3)
        print("--->To check and change data of current user enter [1]")
        print("--->To check and change data of saving user enter [2]")
        try:
            choose = int(input("-->"))
        except:
            print("try again")
            continue
        print("\n"*27)
        if choose == 1:
            savingOrCurrent = "CurrentAccountDetails.txt"
            ff = "current"
            current = "current account"
            saving = "the current account"
            break
        elif choose == 2:
            savingOrCurrent = "SavingAccountDetails.txt"
            ff = "saving"
            current = "saving account"
            saving = "the saving account"
            break
        else:
            pressEnter("Please choose one of the given options")
            print("\n"*27)
            continue
    n=0
    readFile = open(savingOrCurrent, 'r')
    text = readFile.readlines()
    for i in text:
        n += 1
        i = i.split(" ")
        print(f"Account number N{n}")
        print("-"*30)
        print("--->ID: " + i[0]+"\n")
        print("--->Password: " + i[1]+"\n")
        print("--->First Name: " + i[2]+"\n")
        print("--->Second Name: " + i[3]+"\n")
        print("--->Identity number: " + i[4]+"\n")
        print("--->Gender: " + i[5]+"\n")
        print("--->Checking account: " + i[6]+"\n")
    readFile.close()
    while True:
        print("\n"*3)
        print(f"--->Enter [1] to return to {whoUsing} menu"+"\n")
        print(f"--->Enter [2] to change data of {current}"+"\n")
        try:
            choose = int(input("--->"))
        except:
            print("try again")
            continue
        if choose == 1:
            if Return == "Admin":
                return adminMenu(nameAdmin, surNameAdmin)
            else:
                return SuperUserMenu()
        elif choose == 2:
            while True:
                nameOfUser(nameAdmin, surNameAdmin)
                print("\n"*3)
                try:
                    chooseNumber = int(input("--->Please choose number of the user: "))
                    if chooseNumber > len(text):
                        print("TRY AGAIN")
                        continue
                except:
                    print("Try agian")
                print("")
                print(f"Enter 1 to change ID of {saving}"+"\n")
                print(f"Enter 2 to change password of {saving}"+"\n")
                print(f"Enter 3 to change money of users of {saving}"+"\n")
                print(f"Enter 4 to delete {saving} account"+"\n")
                print(f"Enter 5 to check all transactions of users"+"\n")
                print(f"Enter 6 to check special date of user transactions"+"\n")
                chooseWay = input("-->")
                way = "b"
                if chooseWay == "1" or chooseWay == "2" or chooseWay == "3" or chooseWay == "4" or chooseWay == "5" or chooseWay == "6":#chooseWay refer to change password, ID and money. (delete account as well)#
                    userFind(savingOrCurrent, chooseNumber, chooseWay, Return, nameAdmin, surNameAdmin)
                    if chooseWay == "1":
                        way = "The ID"
                    elif chooseWay == "2":
                        way = "The password"
                    elif chooseWay == "3":
                        way = "The money"
                    elif chooseWay == "4":
                        pressEnter("The account was successfully deleted")
                        print("\n"* 27)
                        if Return == "Admin":
                            return adminMenu(nameAdmin, surNameAdmin)
                        else:
                            return SuperUserMenu()
                    elif chooseWay == "5" or chooseWay == "6":
                        if Return == "Admin":
                            print("\n"* 27)
                            return adminMenu(nameAdmin, surNameAdmin)
                        else:
                            print("\n"* 27)
                            return SuperUserMenu()
                    print("\n"* 13)
                    print(f"{way} of the user was changed successfully".center(118))
                    pressEnterForOne()
                    print("\n"* 13)
                    if Return == "Admin":
                        print("\n"* 27)
                        return adminMenu(nameAdmin, surNameAdmin)
                    else:
                        print("\n"* 27)
                        return SuperUserMenu()
                else:
                    pressEnter("Please try again")
                    print("\n"*27)
                    continue
        else:
            pressEnter("Please try again")
            print("\n"*27)
            continue

def nameOfUser(name, secondName):#Output name
    print(f"USER: {name} {secondName}".rjust(120, " ") + ("\n" * 2))

def chooseTextFile(savingOrCurrent):#Reference to the file
    if savingOrCurrent == "current":
        return "CurrentAccountDetails.txt"
    elif savingOrCurrent == "saving":
        return "SavingAccountDetails.txt"
    elif savingOrCurrent == "superAcc":
        return "SuperUser.txt"
    else:
        return "Admin.txt"

checkFile()
