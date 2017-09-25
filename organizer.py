'''
This whole thing took me forever. I was having trouble re-writing the lines back to the txt file without a bunch of unwanted characters.
Also, every time I did, there was an unnecessary amount of whitespace added every time, so the more you run the program, the more whitespace was in the inventory.
This could have theoretically reached an infinite amount of whitespace.
This made running urls and converting the prices back to float impossible.

The difficult thing about setting this up was trying to figure out where I had to take everything out at.
I finally figured out the special character (with some help from google/stackexchange, of course) removal and put it in organize().
However, I was still having trouble with my whitespace problem. That's when I had the idea for my stripper().
'''

import os #To load from a subdirectory
def organize(mediaInv): #For creating lists from a text file
    inventory = open(os.path.join('inventory',mediaInv),'r') #os.path.join loads a subdirectory
    mediaList = []
    for line in inventory: # This is obnoxious. It's to delete all the extra characters
        for char in '\']\n["':
            line= line.replace(char,'')#All the obnoxious characters I need to make sure are deleted from the list
            
        mediaList.append(line.split(','))
    inventory.close()
    mediaList = stripper(mediaList)
    return mediaList

def reorganize(mediaInv,mediaList): #To re-write the list to the text document once changes are made (adding, deleting, selling)
    inventory = open(os.path.join('inventory',mediaInv),'w')
    for line in mediaList:
        inventory.write(str(line) + '\n') #The '\n' lets the next line write to the next line. It's annoying
    inventory.close()          
    return

def stripper(mediaList): # strips off the unnecessary whitespace and converts prices to float
    for i in range(len(mediaList)): # mediaList contains(books,games,etc.)
        for i2 in range(len(mediaList[i])):#i contains (title,creator,price,etc.)
            mediaList[i][i2] = (mediaList[i][i2]).strip()
            if len(mediaList[i]) == 4 and i2 == 1: #because games doesn't have a creator spot
                mediaList[i][i2] = float(mediaList[i][i2])
            elif len(mediaList[i]) == 5 and i2 == 2: #because everything else does
                mediaList[i][i2] = float(mediaList[i][i2])
    return mediaList
