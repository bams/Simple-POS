#Jace Medlin
#CIS-120
#5-18-17

import webbrowser
import organizer
import Receipt

STORE_NAME = "Froggy's Books n Stuff"

books = organizer.organize('books.txt')

cds = organizer.organize("cds.txt")

movies = organizer.organize("movies.txt")

games = organizer.organize("games.txt")

#compact array to set temporary arrays
mediaArray = [books,cds,movies,games]
actionArray = ["sale","addition","deletion"]
MEDIA_LIST = (('book','album','movie','game'),('author','band/artist','director'))

def errorCheck(callVar): #The best function ever. It error-checks my prompt so I don't have to write it out over and over again
    while True:
        try:
            returnVar = input(callVar)
            return returnVar
        except:
            ValueError
            print("Please enter a number.")

def elseFunc(): #Probably unnecessary, but I like it. It just prints that statement below.
    print"\nPlease choose one of the options given.\n"

def listQ(mediaType): #So you can see the current list while adding media
    while True:
        seeList = errorCheck("Would you like to see the current list?\n1. Yes\n2. No\n")
        if seeList == 1:
            listOut(mediaType)
            return
        elif seeList == 2:
            return 
        else:
            elseFunc()

def listOut(mediaList): #For a full list
    i = 0
    print("Here is the available list:\n")
    if (mediaList == 0) or mediaList == 1:
        for i in range (len(mediaArray[mediaList])):
            print(str(i+1) + ". " + str(mediaArray[mediaList][i][0]) + " by " + str(mediaArray[mediaList][i][1]) + " - $%.2f" %float(mediaArray[mediaList][i][2]))
    elif mediaList == 2:
        for i in range(len(movies)):
            print(str(i+1) + ". " + str(movies[i][0]) + " directed by " + str(movies[i][1]) + " - $%.2f" %float(movies[i][2]))
    else:
        for i in range(len(games)):
            print(str(i+1) + ". " + str(games[i][0]) + " - $%.2f" %float(games[i][1]))

def singleTitleList(mediaType,titleToList): #For a single title
    if mediaType == books or mediaType == cds:
        print(str(titleToList[0]) + " by " + str(titleToList[1]) + " - $%.2f\n" %float(titleToList[2]))
    elif mediaType == movies:
        print(str(titleToList[0]) + " directed by " + str(titleToList[1]) + " - $%.2f\n" %float(titleToList[2]))
    else:
        print(str(titleToList[0]) + ' - $%.2f' %float(titleToList[1])) 

def cont(action):
    while True:
        keepGoing = errorCheck("\nWould you like to make another " + actionArray[action] + "?\n1. Yes\n2. No\n")
            
        if keepGoing == 1:
            return 1
        elif keepGoing == 2:
            return 0
        else:
            elseFunc()

def cartFunc(cart,total,printTotal):
    print "Your cart:"
    counter = 1
    for i in cart:
        if len(i) < 5:
            print(str(counter) + ". " + i[0] + " - $%.2f" %i[1])
        else:
            print(str(counter) + ". " + i[0] + " - $%.2f" %i[2])
        counter += 1
    if printTotal == 1:
        print ("\nYour current total is: $%.2f\n"%total)

def sample(mediaType):
    while True:
        listOut(mediaType)
        print("%i. Go Back" %(len(mediaArray[mediaType])+1))
        mediaVar = errorCheck("\nWhich would you like to look at?\n")
        mediaVar -= 1
        if mediaVar < len(mediaArray[mediaType]) and mediaVar >= 0:
            while True:
                example = errorCheck("Would you like a:\n1. Description\n2. Sample\n3. Go back\n")
                if mediaType == 3:
                    if example == 1:
                        if games[mediaVar][3] == ("No Description Available"):
                            print ["\n[No Description Available]"]
                        else:
                            webbrowser.open((games[mediaVar][2]).strip())
                        
                    elif example == 2:
                        if games[mediaVar][3] == ("No Sample Available"):
                            print ("\n[No Sample Available]")
                        else:
                            webbrowser.open((games[mediaVar][3]).strip())
                    elif example == 3:
                        break
                    else:
                        elseFunc()
                else:
                    if example == 1:
                        if mediaArray[mediaType][mediaVar][3] == ("No Description Available"):
                            print("\n[No Description Available]")
                        else:
                            webbrowser.open((mediaArray[mediaType][mediaVar][3]).strip())
                    elif example == 2:
                        if mediaArray[mediaType][mediaVar][4] == ("No Sample Available"):
                            print ("\n[No Sample Available]")
                        else:
                            webbrowser.open((mediaArray[mediaType][mediaVar][4]).strip())
                    elif example == 3:
                        break
                    else:
                        elseFunc()
        elif mediaVar+1 == (len(mediaArray[mediaType])+1):
            return
        else:
            elseFunc()

def replacer(media,tempMediaArray): #Re-appends media to correct location in inventory if cancelling purchase
    counter = 0
    for i in tempMediaArray: # i is books,cds,etc.
        for i2 in i: # i2 is a specific book,cd,etc
            if media == i2:
                mediaArray[counter].append(media)
        counter += 1 # To find the correct type of media to append to
    sorter(1)

def sorter(default):
    sortByWhat = 0
    if default == 0:
        sortByWhat = errorCheck("What would you like to sort by?\n1. Title\n2. Creator\n3. Price\n") - 1
    for i in mediaArray: #i is first level(books,cds,etc.)
        while True:
            keepGoing = 0
            for i2 in range(len(i)-1):#i2 is location of each title in list
                if i == games and sortByWhat == 1:
                    if i[i2][0] > i[i2+1][0]:
                        i[i2],i[i2+1] = i[i2+1],i[i2]
                        keepGoing = 1
                else:
                    if i[i2][sortByWhat] > i[i2+1][sortByWhat]:
                        i[i2],i[i2+1] = i[i2+1],i[i2]
                        keepGoing = 1
            if keepGoing == 0:
                break                            

def sendToReorganizer():
    organizer.reorganize('books.txt',books) #Writes lists back to txt file
    organizer.reorganize('cds.txt',cds)
    organizer.reorganize('movies.txt',movies)
    organizer.reorganize('games.txt',games)
############################################# Main ########################################
def main(): 
    keepGoing = 1
    print "---Welcome to " + STORE_NAME + " ---\n"
    print "We sell games, books, movies, and cds."
    while keepGoing == 1:
        goto = errorCheck("\nWould you like to:\n1. Browse\n2. Make a Sale \n3. Add to Inventory\n4. Delete from Inventory\n5. Exit\n")
        
        if goto ==1:
            browse(1)
        elif goto == 2:
            buy(1)
        elif goto == 3:
            add(1)
        elif goto == 4:
            delete(1)
        elif goto == 5:
            keepGoing = 0
        else:
            elseFunc()
            
    sorter(1)
    sendToReorganizer()
    print ("\nThank you for shopping at Froggy's Books and Games and Stuff!\n")
    raw_input("Press enter to exit.")

def browse(stillBrowsing):
    while stillBrowsing == 1:
        mediaType = errorCheck("\nWhich would you like to look at today?\n1. Books\n2. CDs\n3. Movies\n4. Games\n5. Go Back\n")-1
        
        if mediaType < 4 and mediaType >= 0:
            if mediaArray[mediaType] > 0:
                sample(mediaType)
        elif mediaType == 4:
            return
        else:
            elseFunc()

def buy(anotherSale):

    while anotherSale == 1:
        total = 0.0
        cart = []
        tempGames = []
        tempMovies = []
        tempCds = []
        tempBooks = []
        tempMediaArray = [tempBooks,tempCds,tempMovies,tempGames]
        while True:
            mediaType = errorCheck("Which are you selling?\n1. Books\n2. CDs\n3. Movies\n4. Games\n5. Finish\n") - 1
            if mediaType < 4 and mediaType >= 0:
                tempMedia = mediaArray[mediaType]#tempMedia becomes a temp array as books,cds,movies,or games based on user input

                if len(tempMedia) == 0:#keeps message from repeating if nothing left in list
                    break
                listOut(mediaType)#prints media list
                print("%i. Go back\n" %(len(tempMedia)+1)) #prints a "go back" button
                purchase = errorCheck("Which are you selling?\n")-1
                        
                if purchase < len(tempMedia) and purchase >= 0:
                    cart.append(tempMedia[purchase])
                    if tempMedia == games:
                        total += float(tempMedia[purchase][1])
                        tempGames.append(games[purchase])
                    else:
                        total += float(tempMedia[purchase][2])
                        if tempMedia == books:
                            tempBooks.append(books[purchase])
                        elif tempMedia == cds:
                            tempCds.append(cds[purchase])
                        else:
                            tempMovies.append(movies[purchase])

                    cartFunc(cart,total,1)
                        
                    del(tempMedia[purchase])                   
                        
                elif purchase == len(tempMedia):
                    pass
                else:
                    elseFunc()
                
            elif mediaType == 4:
                while True:
                    cartFunc(cart,total,1)
                    correct = errorCheck("Would you like to:\n1. Proceed with Purchase\n2. Remove an Item\n3. Cancel Purchase\n") - 1
                    
                    if correct == 0:
                        Receipt.printReceipt(cart,total)
                        print("Thank you for your purchase!\n")
                        break
                    elif correct == 1:
                        while len(cart) > 0:
                            cartFunc(cart,total,0)
                            print("%i. Go Back\n" %(len(cart)+1))
                            cartRemove = input("Which would you like to remove?\n") - 1
                            if cartRemove < len(cart):
                                replacer(cart[cartRemove],tempMediaArray)
                                del(cart[cartRemove])
                            elif cartRemove == len(cart):
                                break
                            else:
                                elseFunc()
                    elif correct == 2:
                        for i in cart:
                            replacer(i,tempMediaArray)
                        break
                    else:
                        elseFunc()      
                break
            else:
                elseFunc()
            
        anotherSale = cont(0)

def add(anotherChange):
    while anotherChange == 1:
        mediaType = errorCheck("\nWhich item are you adding to the inventory?\n1. Books\n2. CDs \n3. Movies \n4. Games\n5. Go Back\n")-1

        if mediaType < 4 and mediaType >= 0:
            listQ(mediaType)
            title = raw_input("What is the title of the " + MEDIA_LIST[0][mediaType] + " that you would like to add?\n")
            if mediaType < 3 and mediaType >= 0:
                creator = raw_input("What is the name of its " + MEDIA_LIST[1][mediaType] + "?\n")
            while True:
                addDef = errorCheck("Would you like to add a url link to a description?\n1. Yes\n2. No\n")
                if addDef == 1:
                    description = raw_input("Please paste a url link to the description: ")
                    break
                elif addDef == 2:
                    description = ("No Description Available")
                    break
                else:
                    elseFunc()
            while True:
                addSamp = errorCheck("\nDo you have a url sample of the " + MEDIA_LIST[0][mediaType] + " that you'd like to add?\n1. Yes\n2. No\n")
                if addSamp == 1:
                    sample = raw_input("Please paste your sample url: ")
                    print""
                    break
                elif addSamp == 2:
                    sample = ("No Sample Available")
                    break
                else:
                    elseFunc()
            price = float(errorCheck("What is the price of this " + MEDIA_LIST[0][mediaType] + "?\n"))
            if mediaType == 3:
                newMedia = [title,price,description,sample]
            else:
                newMedia = [title,creator,price,description,sample]
            while True:
                singleTitleList(mediaArray[mediaType],newMedia)
                isCorrect = errorCheck("Does this look right?\n1. Yes\n2. No\n")-1
                if isCorrect == 0:                
                    mediaArray[mediaType].append(newMedia)
                    break
                if isCorrect == 1:
                    break
                else:
                    elseFunc()
            
        elif mediaType == 4:
            return
        else:
            elseFunc()
        sorter(1)
        anotherChange = cont(1)
    
def delete(anotherChange):
    while anotherChange == 1:
        chosen = 0
        while chosen == 0:
            mediaType = errorCheck("\nWhich item are you deleting from the inventory?\n1. Books \n2. CDs \n3. Movies \n4. Games\n5. Go Back\n")-1

            if mediaType < 4 and mediaType >= 0:
                while True:
                    listOut(mediaType)
                    print("%i Go Back\n" %int(len(mediaArray[mediaType])+1))
                    whichMedia = errorCheck("Which would you like to delete?\n")-1
                    if whichMedia < len(mediaArray[mediaType]):
                        while True:
                            chosen = 1
                            forSure = errorCheck("Are you sure you want to delete " + mediaArray[mediaType][whichMedia][0] + "?\n1. Yes\n2. No\n") - 1
                            if forSure == 0:                                                
                                del mediaArray[mediaType][whichMedia]
                                break
                            elif forSure == 1:
                                break
                            else:
                                elseFunc()                            
                        break
                    elif whichMedia == len(mediaArray[mediaType]):
                        break
                    else:
                        elseFunc()
                    
            elif mediaType == 4:
                return
            else:
                elseFunc()
        anotherChange = cont(2)

main()
