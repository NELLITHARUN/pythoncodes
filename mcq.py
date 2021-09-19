def MCQ(question,optionA,optionB,optionC,optionD,answer):
   print(f"{question}")
   print(f"\t{optionA}")
   print(f"\t{optionB}")
   print(f"\t{optionC}")                                             
   print(f"\t{optionD}")
   

   userAnswer=input("Please type the correct option..")
   
   
   userAnswer=userAnswer.strip().upper()
   if userAnswer==answer: 
     print(f"correct! {userAnswer} is the right answer")
   else:
     print(f"Incorrect {userAnswer} is the wrong answer")
MCQ("Which one of the following is not a state in India? ","A.Maharashtra ","B.Tamilnadu","C.Hyderabad","D.Bihar","C")
MCQ("Which one of the following is a state in India? ","A.Maharashtra ","B.Tamilnadu","C.Hyderabad","D.Bihar","C")