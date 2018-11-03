import os.path as pa
fname=input("enter file name with extension:")
bo=pa.exists(fname)
if bo:
      print(open(fname).read())
else:
      print("file not available")


