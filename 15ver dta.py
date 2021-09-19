def getMcq():
        # file = open("vetcal dta.txt","w")
        mcq1=[]
        # user2_input = 
        mcq1.append(input("Please Type your Question:-"))
        # user2_optionA = 
        mcq1.append(input("Type your Option A:-"))
        # user2_optionB= 
        mcq1.append(input("Type your Option B:-"))
        # user2_optionC = 
        mcq1.append(input("Type your Option C:-"))
        # user2_optionD= 
        mcq1.append(input("Type your Option D:-"))
        # user2_answer = 
        mcq1.append(input("Type your answer:-"))
     # file.write (user2_input, user2_optionA , user2_optionB ,user2_optionC ,user2_optionD , user2_answer)

        # file.close()
        return mcq1

 
def sendMcq(mcqs):
    file = open("vetcal dta.txt","a")
    file.write (f"{mcqs[0]}, {mcqs[1]},{mcqs[2]},{mcqs[3]},{mcqs[4]},{mcqs[5]}\n")
    file.close()

# # sendMcq(getMcq())

def showonemcq(mcq):
       
       print(f"qn:{mcq[0]}")
       print(f"a.  {mcq[1]}")
       print(f"b.  {mcq[2]}") 
       print(f"c.  {mcq[3]}")
       print(f"d.  {mcq[4]}")
       print(f"ans:{mcq[5]}")
 
Questions = open("vetcal dta.txt","r+")
file = Questions.readlines()
Questions.close()
storemcqs= []
for line in file :
   storemcqs.append(line.split(","))
showonemcq(storemcqs)




# f = open("vetcal dta.txt", "r")
# content = f.read()
# content_list = content.splitlines()

# print(content_list)
# f.close()