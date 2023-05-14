#Importing the module
import operations as o
#User input function
def User_Input():
    pc_no = input("Enter the PC number: ")
    operating_system_installed = input("Enter the operating system is install or not: ")
    status = input("Enter the status which is running or not: ")

    return {"pc_no" : pc_no, "operating_system_installed" : operating_system_installed, "status": status}

def MenuBar():
    print("\t\t\t\t\t\t****************  Welcome to Computer Lab Management System  ****************")
    while (True):
        opt = input("Please Enter the Key('m') to get Menubar : ")
        if opt == "m":
            print("1.ADD COMPUTERS")
            print("2.REMOVE COMPUTERS")
            print("3.SEARCH COMPUTERS")
            print("4.UPDATE COMPUTERS")
            print("5.SHOW THE LIST OF ALL COMPUTERS")
            print("6.SHOW THE PARTICULAR COMPUTERS DETAILS")
            print("0.QUIT")
            print("\n")
        elif opt == "1":
            print("****ADD COMPUTER****")
            o.Add_Computer(User_Input())
            print("\n")
        elif opt == "2":
            print("****REMOVE COMPUTER****")
            pc_no = input("Enter the pc no to remove: ")
            o.Remove_Computer(pc_no)
            print("\n")
        elif opt == "3":
            print("****SEARCH COMPUTER****")
            pc_no = input("Enter the pc no to search computer: ")
            data = o.Search_Computer(pc_no)
            if data:
                print(data)
            else:
                print("no such pc is existed... You can add here")
                o.Add_Computer(User_Input())
            print("\n")
        elif opt == "4":
            print("****UPDATE COMPUTER****")
            o.Update_Computer(User_Input())
            print("\n")
        elif opt == "5":
            print("****ALL COMPUTERS****")
            print(o.Display_ALL_Computer())
            print("\n")
        elif opt == "6":
            print("****PARTICULAR COMPUTER DETAILS****")
            pc_no = input("Enter the pc no to see the details: ")
            print(o.Search_Computer(pc_no))
            print("\n")
        elif opt == "0":
            print("Exit")
            print("\n")
            break
        else:
            print("Invalid input, please try again!")
#Calling the function
MenuBar()