def codeview():  
  print("Enter your desired code ID:")
  desiredid = input()
  f=open("code"+(desiredid)+".py","w+")
  f.write("def test():\n")
  f.write("   from codes import "+ "code"+(desiredid)+"\n")
  f.write("   from codes import "+ "codedate"+(desiredid)+"\n")
  f.write("   from codes import "+ "codetime"+(desiredid)+"\n")
  f.write("   print(""***ID: " + (desiredid) + "***TIME:")
  f.close