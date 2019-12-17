
#Form Tutor Management System
import sys #this allows you to use the sys.exit command to quit/logout of the application
import base64
import codegenerate
import codeview
def main():
    menu()
def menu():
    print("***************MAIN MENU*****************")
    #time.sleep(1)
    print()

    choice = input("""
                      A: Create New Code
                      B: Code Mangement System
                      C: Help/Information

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        codegenerate.start()
        menu()
    elif choice == "B" or choice =="b":
        codeview.codeview()
    elif choice == "C" or choice =="c":
        pass
        menu()
    elif choice=="Hidden" or choice=="hidden":
        pass
        menu()
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        semimenu()
def semimenu():
    print("***********PLEASE SELCECT ONE***********")
    print()

    choice = input("""
                      A: Create New Code
                      B: View Code Log
                      C: Add Code To Log
                      D: Help

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        codegenerate.codegenerate()
        semimenu()
    elif choice == "B" or choice =="b":
        codeview.desiredid()
    elif choice == "C" or choice =="c":
        pass
    elif choice=="D" or choice=="d":
       printcode()
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        semimenu()
    
#the program is initiated, so to speak, here
main()

