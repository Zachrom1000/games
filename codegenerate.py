def start():
  print("***************Code Creater**************")
  print()

  choice = input("""
                      A: Creating Code
                      B: How to use code
                      C: Information

                      Please enter your choice: """)
  if choice == "A" or choice == "a":
    codegenerate()
  elif choice == "B" or choice == "a":
    pass
  elif choice == "C" or choice == "c":
    pass
def exit():
  print("Type *back* to return to menu")
  if "back"==input():
    pass
  else:
    print("Type *back* to return to the menu")
    exit()
def codegenerate():
   import base64
   import time
   from datetime import datetime
   print("**************************************")
   print("***Idle Breakout Save Hack by Mooch***")
   print("**************************************")

   print("What level do you want to be on?")
   level = input()
   
   print("What amount of money would you like to have")
   money = input()

   print("How much gold do you want")
   gold = input()

   print("How many Black Boxes?")
   bb = input()

   print("How many skillpoints")
   sp = input()
# Begining of encoding process
   s = f"{level},{money},{gold},2,0,0,0,0,0,0,0,1,1,0,43595.78,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{bb},0,0,0,1,{sp},1,0,0"
   b = s.encode("UTF-8")
   e = base64.b64encode(b)
   print("Encoding....")
   time.sleep(4)
   code = e
   fin = True
   print("Enter desired code I.D. : ")
   id = input()
   print("Define a Name")
   name = input()
   date = datetime.date(datetime.now())
   time = datetime.time(datetime.now())
   str(date)
   str(time)
   complete = {"id": id , "data" : e , "date" : date , "time" : time , "name" : name}
   print("Your result is....")
   print(e)
   print(complete)
   f=open("codes.py","w+")
   f.write("code = " + str(complete))
   f.close
   print("\nCopy whats INSIDE the quotes\n")
   end = 1
   exit()
