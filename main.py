import sys

print ("Hanyu Shuiping Kaoshi Level 6 (Advanced Chinese) \n")

display_choice=raw_input("Would you like to view words in characters or in pinyin? Press 1 for characters or 2 for pinyin. Press any other key to exit. \n")
if display_choice=="1":
    import characters
    characters.main()
elif display_choice=="2":
    import pinyin
    pinyin.main()
else:
    print "Goodbye!"
    sys.exit()
