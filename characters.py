import random
import sys
from hskdict2 import hskdict

def main(): 

    wrong_answers=[]
    right_answers=[]

    missed_questions = False
    scored_points = False

    def exit_program():
        print "Goodbye!"
        sys.exit()
        #Exits program

    try:
        num_questions=int(raw_input("Choose a number of questions to display between 1 and 100. To exit, press 0. \n"))
        if num_questions == 0:
            exit_program()
    except ValueError:
        print "Please enter a valid number."
        num_questions=int(raw_input("Choose a number of questions to display between 1 and 100. To exit, press 0. \n"))

    count = 0   

    for key in (hskdict):
        while num_questions > count:
            if num_questions > 0 and num_questions <= 100:
                multiple_choices = random.sample(hskdict,3)
                #This displays the number of multiple choices
                correct_answer=random.choice(multiple_choices)
                #Selects correct answer
                current_question= hskdict[correct_answer]
                #Current question
                a, b, c = multiple_choices[0], multiple_choices[1], multiple_choices[2]
                #Assigned variables to key indexes
                
                print "*" +current_question
                print "\n \t (a)%s   (b)%s   (c)%s \n" %tuple(multiple_choices)
                #Formats the multiple choices with "a","b", and "c"

                user_answer=raw_input("Type your answer: \n" )


                if a == correct_answer:
                        if (user_answer== "a") or (user_answer == "A"):
                            print ("Right! \n")
                            right_answers.append(current_question)
                            #If "a" is right, it prints "Right", appends this to the right_answers list, and deletes the question so as not to repeat
                            del hskdict[a]

                        else:
                            print ("Wrong. \n")
                            print "\tThe answer is",correct_answer+".\n"
                            wrong_answers.append(current_question)
                            missed_questions = True
                            del hskdict[a]

                elif b == correct_answer:
                        if (user_answer== "b") or (user_answer == "B"):
                            print ("Right! \n")
                            right_answers.append(current_question)
                            scored_points = True
                            #If "b" is right, it prints "Right", appends this to the right_answers list, and deletes the question so as not to repeat
                            del hskdict[b]
                            
                        else:
                            print ("Wrong. \n")
                            print "\tThe answer is",correct_answer+".\n"
                            wrong_answers.append(current_question)
                            missed_questions = True
                            del hskdict[b]

                elif  c == correct_answer:
                        if (user_answer== "c") or (user_answer == "C"):
                            print ("Right! \n")
                            right_answers.append(current_question)
                            scored_points = True
                            del hskdict[c]
                            #If "c" is right, it prints "Right", appends this to the right_answers list, and deletes the question so as not to repeat

                        else:
                            print ("Wrong. \n")
                            print "\tThe answer is",correct_answer+".\n"
                            wrong_answers.append(current_question)
                            missed_questions = True
                            del hskdict[c]

                else:
                    print ("\tWrong. \n")
                    print "\tThe answer is",correct_answer+".\n"
                    wrong_answers.append(current_question)
                    missed_questions = True       

                print "Your score is",str(len(right_answers))+".\n"
                count = count + 1

            else:
                num_questions=int(raw_input("Choose a number of questions to display between 1 and 100. To exit, press 0. \n"))
        
        def quiz_result():
            total_score= (len(right_answers)/float(num_questions))*100
            
            print "\tYou scored",len(right_answers),"right out of",num_questions,"questions. Your grade is", "{0:.0f}%.".format(float(total_score))

            if total_score >=60:
                print "\tYou passed this test. \n"
                if total_score == 100:
                    print "\tYou aced it! Congratulations. \n"
            else:
                print "\tYou failed this test.\n"
                
        if num_questions >= 1:
            quiz_result()
        
        def restart():
            if num_questions >= 1:
                restart=raw_input("Would you like to play again? Press \"y\" for yes or \"n\" for no. \n")
                if restart == "y" or restart == "Y":
                    main()
                else:
                    exit_program()
                    
        if wrong_answers:       
            review = raw_input("Would you like to review the words you missed? Press \"y\" for yes or \"n\" for no. \n")
            if review == "y" or review == "Y":
                for wrong in wrong_answers:
                    print "\t*",wrong,"\n"
                restart()
            else:
                    restart()
                    
        else:
            restart()
            
if __name__ == '__main__':
    main()
