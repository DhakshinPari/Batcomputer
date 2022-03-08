import time

print('''Welcome to the Batcave!

''')
pass_word = input('What is the Password?: ')

if pass_word == "Iron Man sucks" :
    print('''


Thank you!''')
    time.sleep(5)
    print('''








































Welcome home, sir!''')
    time.sleep(3)
    print('''


Initializing Batcave operating system...''')
    time.sleep(2)
    print('''


                    ***********************
               *********************************
           *******   *     *       *    *    *******
        *******   ***      **     **     ***   *******
      ******   *****       *********      *****    *****
    ******  ********       *********       ******    *****
   ****   **********       *********       *********   *****
  ****  **************    ***********     ************   ****
 ****  *************************************************  ****
****  ***************************************************  ****
****  ****************************************************  ****
****  ****************************************************  ****
 ****  ***************************************************  ****
  ****  *******     ****  ***********  ****     *********  ****
   ****   *****      *      *******      *      ********  ****
    *****   ****             *****             ******   *****
      *****   **              ***              **    ******
       ******   *              *              *   *******
         *******                                *******
            ********                         *******
               *********************************
                    ***********************


                    ''')
    time.sleep(2)
    print("What's up, Batman?")
    time.sleep(2)
    print('''


Questions?


Try:

News
Who saved the city?
Update
Dinner
Alfred
Arkham
Bank Balance

''')
#    for _ in 100:
question_answer = input('Any Questions Sir?: ')
#Update on personal events.
if question_answer == "Update" :
        print('You have four pieces of mail...')
        time.sleep(2)
        print("You have this week's Pennysaver,two bills,and a coupon for Bed Bath and Beyond.")
        time.sleep(2)
        print('It expires in two weeks.')
        time.sleep(2)
        print("But I've heard that some stores will honor them past the expiry date.")
#Update on what Alfred is doing.
elif question_answer == "Alfred" :
        print("Alfred is on the 17th floor, grouting tiles in the second bathroom")
        time.sleep(2)
        print("of the fifth master bedroom.")
#Update on what is for dinner.
elif question_answer == "Dinner" :
        time.sleep(2)
        print("Alfred left your lobster thermidor in the fridge.")
#News
elif question_answer == "News":
        time.sleep(2)
        print("First, Superman is getting an award you deserve.")
#self appreciation
elif question_answer == "Who saved the city?":
        time.sleep(1)
        print("You saved the city sir!")
#Arkham
elif question_answer == "Arkham":
        time.sleep(2)
        print("Currently Arkham is at full capacity, after you saved the city.")
#Bank Balance
elif question_answer == "Bank Balance":
        time.sleep(1)
        print('''
Your Bank Balance is...
        ''')
        time.sleep(3)
        print("$14,544,562,790,316 USD")
#Shutdown of bat computer.
elif question_answer == "shutdown":
    time.sleep(3)
    print("Good Bye!")

#First ifs B condiiton
else:
    print("Get out Superman!")
    
