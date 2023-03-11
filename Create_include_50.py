#import glob
import os
import shutil
#import re
#import time
labels = ['Bird','Black','Car','Dog','Fall','Father','Good Morning', 'Red','Summer','White','loud','quiet','happy','long','short','big large', 'small little','hot', 'new','dry','good','Cow','Hat', 'T-Shirt', 'Shoes', 'Monday', 'Year', 'Time', 'Fan', 'Cell phone', 'Hello', 'Thank you', 'Window', 'Pen', 'Paint', 'Teacher', 'Priest', 'train ticket', 'Brother', 'Boy', ' Girl', ' Bank', 'I', 'it','you', 'Election', 'Death', 'Court', 'House', 'Store or Shop']
categories = [ '.\Adjectives', '.\Animals','.\Clothes','.\Colours','.\Days_and_Time','.\Electronics','.\Greetings','.\Home','.\Jobs','.\Means_of_Transportation','.\People',',\Places','.\Pronouns','.\Seasons',',\Society']
# Delete words not in labels
# if root in label or in categories skip else delete files, delete root.
#os.remove("filename.txt")
#os.rmdir("")


word_count = len(labels)

def check(dirname):
    for word in labels:
        if(word in dirname):
            return True
    return False
#It will print words not in Include 50 and these you are going to delete. comment line 26, uncomment line 27,28,29 to delete. I have pasted the non Include 50 labels in Include readme if interested.
for root,dirnames,filenames in os.walk('.'):
    if(len(filenames)==0):
        for dir in dirnames:
            if(check(dir) == False):
                print(dir)
                #file_path = os.path.join(root,dir)
                #if os.path.exists(file_path):
                    #shutil.rmtree(file_path)
    
#figure out regex   
    #if(root not in categories and root!='.'):
#        print(root)
#       print(dirnames)
#        print(filenames)
#    time.sleep(4)

#get a gigantic list from iglob and remove not in list.
#for root, dirnames, filenames in os.walk('.'):
#    for filename in filenames:
#        print(os.path.join(root, filename))
