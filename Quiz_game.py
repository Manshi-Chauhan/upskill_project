import random
import time 
print("Welcome to the Quiz Game!")
print("---------------------------")
questions=[
    {"Ques":"which is the capital of India?","Ans":"New Delhi"},
    {"Ques":"The headquarters of the World Bank is in:","Ans":"Washington D.C."},
    {"Ques":"Which is the national Anthem?","Ans":"Jana Gana Mana"},
    {"Ques":"GST was implemented in India in:","Ans":"2017"},
    {"Ques":"Who was the founder of the Maurya Empire?","Ans":"Chandragupta Maurya"},
    {"Ques":"Who is known as the Father of the Indian Constitution?","Ans":"B. R. Ambedkar"},
    {"Ques":"What gas do plants absorb from the atmosphere during photosynthesis?","Ans":"Carbon dioxide (CO₂)"},
    {"Ques":"What is the currency of Japan?","Ans":"Japanese Yen"},
    {"Ques":"Which is the longest river in the world?","Ans":"Nile River"},
    {"Ques":"Which is the highest mountain peak in the world?","Ans":"Mount Everest"},
    {"Ques":"Who appoints the Governor of an Indian state?","Ans":"President of India"},
    {"Ques":"Who was the first Mughal Emperor of India?","Ans":"Babur"},
    {"Ques":"The Battle of Plassey was fought in:","Ans":"1757"},
    {"Ques":"Who was known as the Iron Man of India?","Ans":"Vallabhbhai Patel"},
    {"Ques":"The capital of Australia is:","Ans":"Canberra"},
    {"Ques":"The Tropic of Cancer passes through how many Indian states?","Ans":"8"},
    {"Ques":"How many Fundamental Rights are there currently in India?","Ans":"6"},
    {"Ques":"RBI was established in:","Ans":"1935"},
    ]
no_of_ques=5
score=0
selectedQues=random.sample(questions,k=no_of_ques)
startTime=time.time()

for ques in selectedQues:
    print(ques["Ques"])
    Answer=input("Enter Your Answer...")
    if ques["Ans"].lower() == Answer.lower():
        print("Wow!, Correct Answer,You score 1 point...")
        score+=1
    else:
        print("Incorrect answer")
endTime=time.time()
print("Score:",score,"/",no_of_ques)
print("Time Taken:",round(endTime-startTime,2),"Sec")