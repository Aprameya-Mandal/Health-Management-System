def gettime():
    import datetime
    return datetime.datetime.now()


def getdata(name, doe):
    if name == "Harry":
        if doe == "diet":
            f = open("./Harry_diet.txt")
            content = f.read()
            if content == '':
                print("There is nothing in the specific file...")
            else:
                print(content)
            f.close()
        else:
            f = open("./Harry_exercise.txt")
            content = f.read()
            if content == '':
                print("There is nothing in the specific file...")
            else:
                print(content)
            f.close()
    elif name == "Rohan":
        if doe == "diet":
            f = open("./Rohan_diet.txt")
            content = f.read()
            if content == '':
                print("There is nothing in the specific file...")
            else:
                print(content)
            f.close()
        else:
            f = open("./Rohan_exercise.txt")
            content = f.read()
            if content == '':
                print("There is nothing in the specific file...")
            else:
                print(content)
            f.close()
    elif name == "Hammad":
        if doe == "diet":
            f = open("./Hammad_diet.txt")
            content = f.read()
            if content == '':
                print("There is nothing in the specific file...")
            else:
                print(content)
            f.close()
        else:
            f = open("./Hammad_exercise.txt")
            content = f.read()
            if content == '':
                print("There is nothing in the specific file...")
            else:
                print(content)
            f.close()


def setdata(name, doe, data):
    if name == "Harry":
        if doe == "diet":
            f = open("./Harry_diet.txt", "a")
            f.write("[" + str(gettime()) + "] " + data + ', ')
            f.close()
        else:
            f = open("./Harry_exercise.txt", "a")
            f.write("[" + str(gettime()) + "] " + data + ', ')
            f.close()
    elif name == "Rohan":
        if doe == "diet":
            f = open("./Rohan_diet.txt", "a")
            f.write("[" + str(gettime()) + "] " + data + ', ')
            f.close()
        else:
            f = open("./Rohan_exercise.txt", "a")
            f.write("[" + str(gettime()) + "] " + data + ', ')
            f.close()
    elif name == "Hammad":
        if doe == "diet":
            f = open("./Hammad_diet.txt", "a")
            f.write("[" + str(gettime()) + "] " + data + ', ')
            f.close()
        else:
            f = open("./Hammad_exercise.txt", "a")
            f.write("[" + str(gettime()) + "] " + data + ', ')
            f.close()
    print("Your data have successfully written in the specific file...")


def main():
    print("Welcome to the health management system")
    print("This system only works for 3 clients:")
    print("1: Harry\t2: Rohan\t3: Hammad")
    print("What do you want to do?")
    print("Enter 1 for locking someone's diet or exercise")
    print("Enter 2 for retrieving someone's diet or exercise")
    try:
        rol = int(input())
        if rol == 1:
            print("For who you want to lock?")
            print("Press:")
            print("1 for Harry\t2 for Rohan\tand 3 for Hammad")
            person = int(input())
            if person == 1:
                print("What do you want to lock harry's diet or exercise??")
                print("Press 1 for locking the diet")
                print("Press 2 for locking the exercise")
                doe = int(input())
                if doe == 1:
                    print("What do you want to lock?(Write only one item and no comma and space is allowed)")
                    data = input()
                    if ' ' in data or ',' in data:
                        print("Error! No commas and spaces allowed...")
                    else:
                        setdata("Harry", "diet", data)
                    pass
                elif doe == 2:
                    print("What do you want to lock?(Write only one item and no comma and space is allowed)")
                    data = input()
                    if ' ' in data or ',' in data:
                        print("Error! No commas and spaces allowed...")
                    else:
                        setdata("Harry", "exercise", data)
                    pass
                else:
                    print("Error! Please rerun the program and press 1 or 2 at the third input segment...")
            elif person == 2:
                print("What do you want to lock Rohan's diet or exercise??")
                print("Press 1 for locking the diet")
                print("Press 2 for locking the exercise")
                doe = int(input())
                if doe == 1:
                    print("What do you want to lock?(Write only one item and no comma and space is allowed)")
                    data = input()
                    if ' ' in data or ',' in data:
                        print("Error! No commas and spaces allowed...")
                    else:
                        setdata("Rohan", "diet", data)
                    pass
                elif doe == 2:
                    print("What do you want to lock?(Write only one item and no comma and space is allowed)")
                    data = input()
                    if ' ' in data or ',' in data:
                        print("Error! No commas and spaces allowed...")
                    else:
                        setdata("Rohan", "exercise", data)
                    pass
                else:
                    print("Error! Please rerun the program and press 1 or 2 at the third input segment...")
            elif person == 3:
                print("What do you want to lock Hammad's diet or exercise??")
                print("Press 1 for locking the diet")
                print("Press 2 for locking the exercise")
                doe = int(input())
                if doe == 1:
                    print("What do you want to lock?(Write only one item and no comma and space is allowed)")
                    data = input()
                    if ' ' in data or ',' in data:
                        print("Error! No commas and spaces allowed...")
                    else:
                        setdata("Hammad", "diet", data)
                    pass
                elif doe == 2:
                    print("What do you want to lock?(Write only one item and no comma and space is allowed)")
                    data = input()
                    if ' ' in data or ',' in data:
                        print("Error! No commas and spaces allowed...")
                    else:
                        setdata("Hammad", "exercise", data)
                    pass
                else:
                    print("Error! Please rerun the program and press 1 or 2 at the third input segment...")
            else:
                print("Error! Please rerun the program and press 1 or 2 or 3 at the second input segment...")

        elif rol == 2:
            print("For who you want to retrieve?")
            print("Press:")
            print("1 for Harry\t2 for Rohan\tand 3 for Hammad")
            person = int(input())
            if person == 1:
                print("What do you want to retrieve? Harry's diet or exercise")
                print("Press 1 for diet and 2 for exercise...")
                doe = int(input())
                if doe == 1:
                    getdata("Harry", "diet")
                elif doe == 2:
                    getdata("Harry", "exercise")
                else:
                    print("Error! Please rerun the program and press 1 or 2 at the third segment...")

            elif person == 2:
                print("What do you want to retrieve? Rohan's diet or exercise")
                print("Press 1 for diet and 2 for exercise...")
                doe = int(input())
                if doe == 1:
                    getdata("Rohan", "diet")
                elif doe == 2:
                    getdata("Rohan", "exercise")
                else:
                    print("Error! Please rerun the program and press 1 or 2 at the third segment...")

            elif person == 3:
                print("What do you want to retrieve? Hammad's diet or exercise")
                print("Press 1 for diet and 2 for exercise...")
                doe = int(input())
                if doe == 1:
                    getdata("Hammad", "diet")
                elif doe == 2:
                    getdata("Hammad", "exercise")
                else:
                    print("Error! Please rerun the program and press 1 or 2 at the third segment...")

            else:
                print("Error! Please rerun the program and press 1 or 2 or 3 at the second input segment...")
        else:
            print("Error! Please rerun the program and press 1 or 2 at the first input segment...")

    except Exception as e:
        print("Unfortunately an error occurred: ")
        print(e)


main()
