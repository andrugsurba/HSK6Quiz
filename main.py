import characters
import pinyin

print ("Hanyu Shuiping Kaoshi Level 6 (Advanced Chinese) \n")

def display_choice():
    display_choice=int(raw_input("Would you like to view words in characters or in pinyin? Press 1 for characters or 2 for pinyin. Press any other key to exit. \n"))
    if display_choice==1:
        characters.main()
    elif display_choice==2:
        pinyin.main()
        
    else:
         print "Goodbye!"

display_choice()
