import random

iNumberofQuestion=0
iScorePerRightAnswer=5
iScorePerWrongAnswer=-0.25
iTotalScore=0

def printUserInput(asMessage):
    while True:
        sInput=input(asMessage)
        sInput=sInput.strip().upper()
        if sInput not in["A","B","C","D"]:
            print(f"{sInput} is can not understand.Please Try again!")
        else:
           break    
    return sInput

def getNumQsFromuser(asMessage):
    while True:
        sInput=input(asMessage)
        sInput=sInput.strip()
        if not sInput.isnumeric():
            print(f"{sInput} is not number")
        else :
            break
    return int(sInput)    

def askQuestion(question,optionA,optionB,optionC,optionD,answer):
   print(f"{question}")
   print(f"\tA.{optionA}")
   print(f"\tB.{optionB}")
   print(f"\tC.{optionC}")                                             
   print(f"\tD.{optionD}")

   userAnswer=printUserInput("Please type the correct option..")
   userAnswer=userAnswer.strip().upper()
#    print(f" correct ans is  {answer}")
   if (userAnswer==answer.strip()):
    print(f"correct! {userAnswer} is the right answer")
    return iScorePerRightAnswer
   else:    
    print(f"Incorrect {userAnswer} is the wrong answer")
   return iScorePerWrongAnswer
        
fileReader= open("15mulq&a.txt","r")

ListofALLQuestions=[]

for line in fileReader:
    listLineQ=line.split(",")
    
    ListofALLQuestions.append(listLineQ)
fileReader.close()
random.shuffle(ListofALLQuestions)
Username=input("what is your name?:")
iNumofQsUserwants=getNumQsFromuser("how Many Questions do you Want to answer?:")

filewriter=open(f"{Username.strip()}-2021-09-18.txt","w")

for line in ListofALLQuestions:
    iNumberofQuestion +=1
    if (iNumberofQuestion > iNumofQsUserwants):
        break
    else:
        printText=f"Question:{line[0]}\n\tA. {line[1]}\n\tB.{line[2]}\n\tc.{line[3]}\n\tD.{line[4]}"
        filewriter.write(f"{printText}\n")
        iRtn=askQuestion(line[0],line[1],line[2],line[3],line[4],line[5])
        if(iRtn==iScorePerWrongAnswer):
          filewriter.write(f"sorry you have an incorrect answer.correct answer is {line[5]}\n")
        else:
            filewriter.write(f"{line[5].strip()} is correct answer\n")
        iTotalScore=iTotalScore +iRtn
# for line in Quiz:
#     Quiz = line.split(",")
#     ireturn=MCQ(f"{Quiz[0]}",f" A.{Quiz[1]}",f"B.{Quiz[2]}",f"C.{Quiz[3]}",f"D.{Quiz[4]}",f"{Quiz[5]}")
#     iNumberofQuestion+=1
#     iTotalScore=iTotalScore+ireturn

# random.shuffle(filehandler)
# iaskQuestion=getuserInput("How many questions do you want")


print(f"Your score is{iTotalScore}/{iNumofQsUserwants*iScorePerRightAnswer}")


  
