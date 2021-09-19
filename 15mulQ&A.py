# f= open("15mulq&a.txt","a")

# userInput=input(" Please Enter the  question :")
# useroptionA=input("option A :")
# useroptionB=input("option B:")
# UseroptionC=input("option c:")
# useroptionD=input("option D:")
# userAnswer=input("Answer:")
# f.write(f"{userInput},{useroptionA},{useroptionB},{UseroptionC},{useroptionD} ,{userAnswer}")
# path of this script
# directory = "C:\Users\madhuri\Desktop\tharun\vs code\python files"
# filepath = directory + input("Enter filename: ")
  

import datetime
current_date_and_time = datetime.datetime.now()
current_date_and_time_string = str(current_date_and_time)
extension = ".txt"

file_name =  current_date_and_time_string + input("Enter filename: ") + extension
file = open(file_name,"w")
print( datetime.datetime.now() )
file.close()


# f=open("15mulq&a.txt","r")
# print(f.read())
# f=open("15mulq&a.txt.txt","a")

# x = "15mulq&a.txt".split(",")

# print(f"qn. {x[0]}")
# print(f"a.  {x[1]}")
# print(f"b.  {x[2]}")
# print(f"c.  {x[3]}")
# print(f"d.  {x[4]}")
# print(f"ans.  {x[5]}")




#  f=open("15mulfile.txt","w")
#  tblnumber=int(input("Enter your tbl_number:"))
#  for aiNum in range(1,11):
#    f.write(f"{tblnumber} x {aiNum} = {tblnumber*aiNum} \n")
#  f.close()

