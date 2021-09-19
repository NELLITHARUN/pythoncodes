 #file to read and write multable 
f=open("15mulfile.txt","w")
tblnumber=int(input("Enter your tbl_number:"))
for aiNum in range(1,11):
  f.write(f"{tblnumber} x {aiNum} = {tblnumber*aiNum} \n")
f.close()

file=open("15mulfile.txt","r")
print(file.read())
file1=open("15mulfile.txt","a")