import time
import random
transportation = "" #Möjliga värden är (buss, cykel eller gå)
lostWallet = False
flatTire = True
personToSitNextTo= "" # Möjliga värden är (alexander, albert, klara)
nameOfAvatar = "" #Vad heter Avataren
ageOfAvatar = "" #Hur gammal är Avataren
originOfAvatar = "" # Vart kommer Avataren ifrån
def main(): #Funktionen main är den funktion som kallar på alla andra funktioner för att få spelet att fungera
    startScreen()
    choice1Transportation()
    campusScreen()
    choice2WhereToSit()
    matteProv()
    lunchScreen()
    choice3WhatToEatForLunch()
    namnLek()
def menu(title,prompt,options):
    print(title)
    print()
    for x in options:
        print (f"{x}: {options[x]}")
    print()
    option = input(prompt)
    x=0
    while x==0:
        if option in options:
            x=1
        else:
            option = input(prompt)
   
    return option


def clear():
    print ("\n" * 40)
def gameOver():
    print("Game over")
    time.sleep(2)
    options = {"r":"Try Again", "q":"Quit"}
    choice=menu("Vad vill du göra?","Välj alternativ: ",options)
    if choice == "r":
        clear()
        startScreen()
    elif choice=="q":
        print("Tack för att du spelade ha en bra dag!")
    return None

def startScreen():
    print()
    print("Välkommen till reccesimulator")
    print()
    time.sleep(2)
    print("Som ny student vet man aldrig vad som väntar runt hörnet.")
    time.sleep(3)
    print("Därför ska du idag få ett smakprov på hur första dagen på universitetet kan gå till!!")
    time.sleep(3)
    return None
def choice1Transportation():
    global transportation
    global lostWallet
    options={"1":"gå", "2":"cykla", "3":"åka buss", "4": "ta bil"}

    print("Du ska börja dagen med att ta dig till skolan!")
    time.sleep(2)

    choice= menu("Du kan välja följande 4 sätt att ta dig till skolan:", "Välj alternativ:", options)

    x=1
    while x==1:
        if choice=="1":
            transportation= "gå"

        elif choice=="2":
            transportation= "cykel"

        elif choice=="3":
            transportation= "buss"
            lostWallet ==True

        elif choice=="4":
            transportation= "bil"
        else:
            choice=input("Välj alternativ:")

        if choice in options:
            print(f"Du har valt alternativ {choice}")
            print()
            time.sleep(1.5)
            print(f"kul att du valde att {options[choice]}!")
            if choice== "4":
                print()
                time.sleep(1.5)
                print("Oh nej! du krocka och dog!")
                time.sleep(1)
                print("gameover")
                GameOver()
                x=0
            else:
                print("grattis du tog dig till skolan!!")
                x=0
                
def campusScreen(): #Skriver ut några meningar när avatar precis kommit fram till campuset
    print("Du är äntligen framme vid ditt campus och börjar känna fjärilar i magen över att träffa dina nya klasskompisar!")
    time.sleep(4)
    print("Du tar fram mobilen och kollar vilket klassrum du ska vara i")
    time.sleep(4)
    print("Du öppnar sedan dörren till campuset och går in genom dörren och upp för trapporna till våning 2")
    time.sleep(4)
    print("Du ser att dörren till ditt klassrum är öppen och du går in genom den öppna dörren in till klassrummet!")
    time.sleep(4)
    return None
def createAvatar(): # Användaren skapar sin avatar genom att tilldela värden till de globala variablerna
    global nameOfAvatar
    global ageOfAvatar
    global originOfAvatar
    nameOfAvatar = input("Vad heter du? ")
    ageOfAvatar = input("Hur gammal är du? ")
    originOfAvatar = input("Vart kommer du ifrån? ")
    
    
def choice2WhereToSit(): # Spelaren får välja mellan att sitta bredvid tre olika personer. Den globala variabeln personToSitNextTo får värdet på personen spelaren väljer att sitta bredvid. 
    global personToSitNextTo
    persons={"1":"Sportfånen","2":"Nörden","3":"Punkaren"}
    print("Du ser att det finns tre lediga platser att välja på!")
    time.sleep(3)
    choice=menu("Du kan välja att sitta bredvid följande tre personer:","Välj alternativ: ", persons)
    x=1
    while x==1: #Ger globala strängen personToSitNextTo ett värde
        if choice == "1":
            personToSitNextTo="alexander"
            x=0
        elif choice =="2":
            personToSitNextTo = "albert"
            x=0
        elif choice == "3":
            personToSitNextTo = "klara"
            x=0
        else:
            choice = input("Välj alternativ: ")
            
    print(f"Du går fram till platsen bredvid {persons[choice]} och sätter dig på den tomma stolen bredvid personen")
    time.sleep(4)
    hej = input("Säg hej till personen! ").lower().replace(" ","") #Spelaren uppmanas att säga hej till personen de sätter sig bredvid
    while hej in ["hej, hej!"]:
        hej = input("Säg hej till personen! ").lower().replace(" ","") # Spelarens input lagras i "hej" och strängen omvandlas till bara små bokstäver samt tar bort samtliga mellanslag
    if personToSitNextTo == "alexander": #Beroende av värdet på personToSitNextTo presenterar sig personen
       print("Hej jag heter Alexander")
       time.sleep(3)
       print("Jag är 20 år gammal och älskar sport")
       time.sleep(3)
       print("Jag spelar just nu bara fotboll men har spelat hockey, åkt längdskidor, gått på simining, cyklat och orienterat")
       time.sleep(4)
       print("Hoppas vi ska köra mycket tävlingar idag så jag kan vinna!")
       time.sleep(3)
    elif personToSitNextTo == "albert":
        print("Hej jag heter Albert")
        time.sleep(3)
        print("Jag är 24 år gammal och älskar att räkna matte")
        time.sleep(3)
        print("Jag älskar att lära mig nya saker och på fritiden brukar jag sitta hemma i min källare och spela spel")
        time.sleep(4)
        print("Hoppas vi kommer få något oförberätt prov idag!")
        time.sleep(3)
    else:
        print("Hej jag heter Klara")
        time.sleep(3)
        print("Jag är 18 år gammal och älskar att lyssna på musik")
        time.sleep(3)
        print("Jag älskar att festa på fritiden")
        time.sleep(3)
        print("Hoppas det blir en najs fest ikväll efter skolan!")
        time.sleep(3)
    print("Nog om mig, berätta om dig själv!")
    time.sleep(3)
    createAvatar() #Kallar på funktionen createAvatar för att skapa en avatar
    print(f"Trevligt att träffas {nameOfAvatar} {ageOfAvatar} år från {originOfAvatar}")
    time.sleep(4)

def matteProv(): #En funktion som hanterar ett matteprov där spelaren själv ska svara på tre frågor
    print("Läraren kallar på allas uppmärksamhet!")
    time.sleep(3)
    print("Det blir helt tyst i klassrummet under några sekunder")
    time.sleep(4)
    print("Hej alla nya studententer! Det är otroligt roligt att äntligen få träffa er!")
    print()
    time.sleep(4)
    print("Och ett stort grattis till erat val av att börja läsa civilingengörsprogrammet i informationsteknologi här på Uppsala Universitet!")
    time.sleep(5)
    print("Som alla säkert redan är medvetna om är det en hel del matte som ni kommer läsa de kommande fem åren!")
    time.sleep(5)
    print("Därför kommer vi nu dela ut ett prov för att få en uppfattning över hur era matematikkunskaper ser ut")
    time.sleep(5)
    print("Det är tre frågor vi vill att ni ska svara på, det är förbjudet att fuska!")
    time.sleep(4)
    print("Det är bara att börja när ni får proven, lycka till!")
    time.sleep(3)
    fråga1 = "Vad är (1+1)*5? " # svar "10"
    fråga2 = "Vad är roten ur 81?" # svar "+-9"
    fråga3 = "Vad är cos π/6?" # svar "√3/2"
    svarFråga1=input(fråga1)
    svarFråga2 = input(fråga2)
    svarFråga3 = input(fråga3)
    fuska =False
    options = {"1":"Lämna in provet ", "2": "Fuska (skriva av grannen)"}
    choice= menu("Vad vill du göra?","Välj alternativ: ", options) #Kallar på funktionen menu får att be spelaren att välja mellan 2 alternativ (lämna in provet eller fuska)
    if choice =="2": #If sats som beskriver utfalllet om spelaren väljer att fuska
        print("Du skriver av exakt vad din granne har skrivit")
        if personToSitNextTo == "Sportfåne": #Beroende på vilket värde personToSitNextTo har sker olika saker antingen att spelaren får alla fel, alla rätt eller blir avstängd från skolan
            svarFråga1="hej"
            svarFråga2= "fotboll"
            svarFråga3 = "Mat"
            if svarFråga1=="10" and svarFråga2 == "+-9" and svarFråga3 == "√3/2":
                resultat ="3/3 rätt Fantastiskt jobbat!"
            elif (svarFråga1=="10" and svarFråga2 == "+-9") or (svarFråga1=="10" and svarFråga3 == "√3/2") or (svarFråga2 == "+-9" and svarFråga3 == "√3/2"):
                resultat = "2/3 rätt Bra Jobbat!"
            elif svarFråga1=="10" or svarFråga2 == "+-9" or svarFråga3 == "√3/2":
                resultat = "1/3 rätt Helt okej!"
            else:
                resultat= "0/3 Inte så bra:("
        elif personToSitNextTo =="Nörd":
            print("Läraren kommer fram till dig!")
            time.sleep(3)
            print("Man får inte fuska på provet! Du är härmed avstängd från skolan!")
            time.sleep(4)
            print("Gå raka vägen ut och kom aldrig tillbaka!")
            time.sleep(3)
            gameOver()
        elif personToSitNextTo == "Punkare":
            svarFråga1="10"
            svarFråga2= "+-9"
            svarFråga3 = "√3/2"
            if svarFråga1=="10" and svarFråga2 == "+-9" and svarFråga3 == "√3/2":
                resultat ="3/3 rätt Fantastiskt jobbat!"
            elif (svarFråga1=="10" and svarFråga2 == "+-9") or (svarFråga1=="10" and svarFråga3 == "√3/2") or (svarFråga2 == "+-9" and svarFråga3 == "√3/2"):
                resultat = "2/3 rätt Bra Jobbat!"
            elif svarFråga1=="10" or svarFråga2 == "+-9" or svarFråga3 == "√3/2":
                resultat = "1/3 rätt Helt okej!"
            else:
                resultat= "0/3 Inte så bra:("
                print("Läraren tar emot provet och börjar rätta provet")
                time.sleep(5)
                print("Läraren har rättat klart provet och ger tillbaka det med ditt resultat!")
                time.sleep(1)
                print(f"Du fick {resultat}")
            
             
    if choice == "1":
        if svarFråga1=="10" and svarFråga2 == "+-9" and svarFråga3 == "√3/2":
            resultat ="3/3 rätt Fantastiskt jobbat!"
        elif (svarFråga1=="10" and svarFråga2 == "+-9") or (svarFråga1=="10" and svarFråga3 == "√3/2") or (svarFråga2 == "+-9" and svarFråga3 == "√3/2"):
            resultat = "2/3 rätt Bra Jobbat!"
        elif svarFråga1=="10" or svarFråga2 == "+-9" or svarFråga3 == "√3/2":
            resultat = "1/3 rätt Helt okej!"
        else:
            resultat= "0/3 Inte så bra:("
        print("Läraren tar emot provet och börjar rätta provet")
        time.sleep(5)
        print("Läraren har rättat klart provet och ger tillbaka det med ditt resultat!")
        time.sleep(1)
        print(f"Du fick {resultat}")
def lunchScreen():
    print()
    print("Äntligen ska reccen få i sig lite mat!")
    print()
    time.sleep(3)
    print("Av det generös utbudet ska du få välja vilken mat som ska mätta dig!")
    time.sleep(3)
def choice3WhatToEatForLunch(): #Funktion som ger spelaren ett val att välja vilken lunch spelaren vill äta
    options = {"1":"Pan pizza", "2":"Nudlar", "3": "Falaffelrulle"}
    choice = menu("Vad vill du äta till lunch?","Välj alternativ: ",options)
    if choice ==3: #Om spelaren väljer att äta falafelrullen kommer spelaren att bli magsjuk och spelet slutar!
        print ("Du äter upp din falaffelrulle, men känner att den smakar lite konstigt!")
        time.sleep(3)
        print("Du känner hur du börjar dålig i magen!")
        time.sleep(3)
        print("Du har blivit magsjuk av falafelrullen!")
        time.sleep(3)
        gameOver()
    elif choice==2:
        print(f"Du äter upp dina nudlar som är bland de bästa du någonsin ätit!")
        time.sleep(4)
        print("Du är nu fylld med ny energi för att orka med resten av dagen!")
        time.sleep(4)
    else:
        print(f"Du äter snabbt upp din otroligt goda pan pizza!")
        time.sleep(4)
        print("Du är nu fylld med ny energi för att orka med resten av dagen!")
        time.sleep(4)
        
def namnLek():
    global flatTire
    print("Nu efter lunchen är det dags för er att lära känna varandra bättre!")
    time.sleep(3)
    print("Det allra viktigaste är att lära sig varandras namn!")
    time.sleep(3)
    print("Ni ska nu gissa vad personen höger om dig i ringen heter!")
    time.sleep(3)
    print("Personen på din högra sida är samma person som du satt dig bredvid i klassrummet!")
    time.sleep(3)
    gissning= input("Vad heter personen? ").lower().replace(" ", "") # Spelarens gissning lagras i "gissning" och strängen omvandlas till bara små bokstäver samt tar bort samtliga mellanslag
    if gissning != personToSitNextTo:
        print("Jag trodde vi var kompisar:(")
        time.sleep(3)
        print("Jag hatar dig!")
        if transportation == "cykel": # Om spelaren gissar fel och har en cykel gör personToSItNextTo punktering på cykeln
            flatTire == True
    else:
        print("Vad duktig du är som kom ihåg mitt namn!")
        time.sleep(3)
        print(f"Du är min bästa kompis {nameOfAvatar} :)")
        time.sleep(3)
            
def rainSick():
    
    if random.randint(0,4)==0:
        return True
    else:
        return False
    
def tillMiddag():
    options= {"1":"cykla", "2":"gå"}
    choice=menu("Hur vill du ta dig till middagen?", "Välj alternativ:", options)
    if choice== "1" and flatTire==False:
        print("Härligt! du tog dig fram utan problem!")
        print()
        time.sleep(1.5)
        print("Du kan nu njuta av din middag som avslutning på dagen!")

    elif choice=="1" and flatTire==True:
        print()
        print("Va! du har fått punka! Undra vad eller vem som gjorde detta!")
        print()
        time.sleep(1.5)
        print(f"Det verkar som du får gå istället...")
        if rainSick()==True:
            print("Oh nej det regnet gjorde dig sjuk!!")
            GameOver()
        else:
            print()
            print("Du kom fram blöt men som tur blev du inte förskyld av kylan!")
            print()
            time.sleep(2)
            print("God middag som avslutning på en toppen första dag!")
    else:
        if rainSick()==True:
            print("Oh nej det började regna!")
            time.sleep(3)
            print("Det kalla regnet gjorde dig sjuk!!")
            time.sleep(3)
            GameOver()
        else:
            print()
            print("Du kom fram blöt men som tur var blev du inte förskyld av kylan!")
            print()
            time.sleep(3)
            print("God middag som avslutning på en toppen första dag!")
        
    return None
    


       
       
              
    


    
    
            
            
    
    
    
    


    
        
        
        

        