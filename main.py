#create program for student manage in schooln
db = {}
while True:
    print("#" * 30)
    print("welcome to student managment sysyem ")
    print("input [new] for add student")
    print("input [check] for view student")
    print("input [detete] for delete record")
    print("input [exit] for end program")
    print("#" * 30)
    action = input()
    if action == "new":
        while True:
            rollno = input("enter roll no of student : ")
            name = input("enter full name of student : ")
            db[rollno] = name
            print("succsessfully saved")
            print("#" * 30)
            print("press enter to continue \n press [home] for main page")
            action = input()
            if action == "home":
                break
    elif action == "check":
        while True:
            rollno = input("enter roll no to check data : ")
            if rollno not in db:
                print("this roll no is note resistred in our system")
                print("#" * 30)
            else:
                print("name of student : ", db[rollno])
                print("#" * 30)
            print("press enter to check new \n input[home] for main page")
            action = input()
            if action == "home":
                break
    elif action == "delete":
        while True:
            rollno = input("enter roll no for delete data : ")
            if rollno not in db:
                print("enter valid number ")
                print("#" * 30)
            else:
                db.pop(rollno)
                print("deleted number : ", rollno)
                print("#" * 30)
            print("press enter for new \n input [home] for main page ")
            action = input()
            if action == "home":
                break
    elif action == "exit":
        print("bye")
        break
