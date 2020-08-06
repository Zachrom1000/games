
def codeview():  
  print("Enter your desired code ID:")
  desiredid = input()
  f=open("codeprog.py","w+")
  f.write("def test():\n")
  f.write("   import datetime\n")
  f.write("   from codes import "+ "code"+(desiredid)+"\n")
  f.write("   from codes import "+ "codedate"+(desiredid)+"\n")
  f.write("   from codes import "+ "codetime"+(desiredid)+"\n")
  f.write("   print('***ID: " + (desiredid) + "*** TIME: ' + (codetime" + (desiredid) + ") + '*** DATE:' + (codedate" + (desiredid) + ") + '***')")
  f.close
  