print("==+++++++++++++++++++++++++++++Kaun Banega Lakhpati💵++++++++++++++++++++++++++++++++++==")

questions=[["Which language is used to create fb?","Pyhton","French","Php","None",4],
           ["Which city is the capital of india?","Delhi","Mumbai","Karnataka","Banglore",1],
           ["How many months are there in  a year?","Ten","Twelve","Eight","Nine",2],
           ["How many days are there in a week?","Ten","Seven","Eight","Nine",2],
           ["Which planet is known as the Red Planet?","Venus","Mars","Earth","Jupiter",2]]

levels=[5000,10000,50000,100000,700000]
money=0

for i in range(len(questions)):
    question=questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(questions[i][0])
    print(f"i. {question[1]}                       ii. {question[2]}  ")
    print(f"iii. {question[3]}                      iv. {question[4]}")    

    reply=int(input("Enter your answer (1-4) and 0 to quit :"))
    if reply==0:
        money=levels[i-1]
        break

    if(reply==question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if reply==0:
            money=levels[i-1]
            break
        if i==2:
            money=50000
        elif i==4:
            money=700000
        

    else:
        print("Wrong ans!")
        break

print("Your winnings is",money)    


