import json as J
import ast as A

#Read from file
def ReadFromFile():
    try:
        with open('hello.txt') as file:
            return file.readline()
    except Exception as e:
        print(e.__class__, "The file is not found")

#Write in the file
def WriteInFile(content):
    try:
        contents = J.dumps(content)
        with open("hello.txt", "w") as file:
            file.write(contents)
    except Exception as e:
        print(e.__class__, "The file is not found")

# Display all computers
def Display_ALL_Computer():
    labs = ReadFromFile()
    my_labs = A.literal_eval(labs)
    return my_labs

# Searching the computer
def Search_Computer(pc_no):
    computers = Display_ALL_Computer()
    for computer in computers:
        if computer['pc_no'] == pc_no:
            return computer

#Adding computers
def Add_Computer(computer):
    # checking  the PC number is same or not
    if Search_Computer(computer['pc_no']):
        print("Sorry, The PC Number is Already Existed!")
    else:
        data = Display_ALL_Computer()
        data.append(computer)
        WriteInFile(data)
        print("Successfully, The PC is Added.")

# Update the computer information
def Update_Computer(computer_to_update):
    computers = Display_ALL_Computer()
    if Search_Computer(computer_to_update['pc_no']):
        inc = 0
        for computer in computers:
            if computer['pc_no'] == computer_to_update['pc_no']:
                break
            inc += 1
        computers[inc] = computer_to_update
        WriteInFile(computers)
        print("Successfully, Computer is Updated. ")
    else:
        print("The PC is not Existed!")

# Remove the computer's details
def Remove_Computer(pc_no):
    computers = Display_ALL_Computer()
    if Search_Computer(pc_no):
        inc = 0
        for computer in computers:
            if computer['pc_no'] == pc_no:
                break
            inc =+1
        del computers[inc]
        WriteInFile(computers)
        print("Successfully, Computer is Removed!")
    else:
        print("The PC is not Existed!")







