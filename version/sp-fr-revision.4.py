# coding: utf-8

#
# Credit to Jess Teale for original idea
# (c) Igor Smolinski 2017
# (c) Jess Teale 2017
#

from datetime import datetime #For answer recording
from time import sleep #For waiting
import random #For randomisation of question
import os #For cls/clear
import sys #I don't even know
import ctypes #Title?
from subprocess import call #changing colors

#Sets all variables to "" just in case
word = ""
key_pos = ""
var1 = ""
var2 = ""
answer = ""
la = ""
te = ""
foo = ""
correct = ""
lan = ""
ten = ""

ctypes.windll.kernel32.SetConsoleTitleW("Spanish and French Verb Ending(s) Revision")#Shell window title

def go():#Used instead of os.system('pause') to not show errors
    foo = input("Press enter to continue...")
    try:
        int(foo)
        foo = foo * foo
    except:
        pass

def oops():#Error message for when problem exists between keyboard and chair
    print("Oops! There was an error. :(")
    print("Error: exists between keyboard and chair")
    sleep(1)
    go()
    os.system('cls')
    sys.exit(0)

def main():#Defined as function to be able to loop program
    while True:
        print("╔═══════════════╗")
        print("║ Alt-codes     ║")
        print("╠══════╦════════╣")
        print("║ Alt+ ║ Symbol ║")
        print("║ 0225 ║    á   ║")
        print("║ 0233 ║    é   ║")
        print("║ 0237 ║    í   ║")
        print("╚══════╩════════╝")
        word = input("Your Infinitive: ")
        key_pos = len(word) - 2
        suggestions = ["I", "You (s.)", "He/She/It", "We", "You (Pl.)", "They"]
        var1 = random.choice(suggestions)
        var2 = ""
        if la == "a":# SPANISH
            if te == "1":# SP IMPERFECT
                if word.endswith("ar"):
                    inf = "ar"
                    if var1 == "I":
                        var2 = "aba"
                    elif var1 == "You (s.)":
                        var2 = "abas"
                    elif var1 == "He/She/It":
                        var2 = "aba"
                    elif var1 == "We":
                        var2 = "ábamos"
                    elif var1 == "You (Pl.)":
                        var2 = "abais"
                    elif var1 == "They":
                        var2 = "aban"
                elif word.endswith("er"):
                    inf = "er"
                    if var1 == "I":
                        var2 = "ía"
                    elif var1 == "You (s.)":
                        var2 = "ías"
                    elif var1 == "He/She/It":
                        var2 = "ía"
                    elif var1 == "We":
                        var2 = "íamos"
                    elif var1 == "You (Pl.)":
                        var2 = "íais"
                    elif var1 == "They":
                        var2 = "ían"
                elif word.endswith("ir"):
                    inf = "ir"
                    if var1 == "I":
                        var2 = "ía"
                    elif var1 == "You (s.)":
                        var2 = "ías"
                    elif var1 == "He/She/It":
                        var2 = "ía"
                    elif var1 == "We":
                        var2 = "íamos"
                    elif var1 == "You (Pl.)":
                        var2 = "íais"
                    elif var1 == "They":
                        var2 = "ían"
            elif te == "2":# SP PRETERITE
                if word.endswith("ar"):
                    inf = "ar"
                    if var1 == "I":
                        var2 = "é"
                    elif var1 == "You (s.)":
                        var2 = "aste"
                    elif var1 == "He/She/It":
                        var2 = "ó"
                    elif var1 == "We":
                        var2 = "amos"
                    elif var1 == "You (Pl.)":
                        var2 = "asteis"
                    elif var1 == "They":
                        var2 = "aron"
                elif word.endswith("er"):
                    inf = "er"
                    if var1 == "I":
                        var2 = "í"
                    elif var1 == "You (s.)":
                        var2 = "íste"
                    elif var1 == "He/She/It":
                        var2 = "ió"
                    elif var1 == "We":
                        var2 = "imos"
                    elif var1 == "You (Pl.)":
                        var2 = "isteis"
                    elif var1 == "They":
                        var2 = "ieron"
                elif word.endswith("ir"):
                    inf = "ir"
                    if var1 == "I":
                        var2 = "í"
                    elif var1 == "You (s.)":
                        var2 = "iste"
                    elif var1 == "He/She/It":
                        var2 = "ió"
                    elif var1 == "We":
                        var2 = "imos"
                    elif var1 == "You (Pl.)":
                        var2 = "isteis"
                    elif var1 == "They":
                        var2 = "ieron"
            elif te == "3":# SP PRESENT
                if word.endswith("ar"):
                    inf = "ar"
                    if var1 == "I":
                        var2 = "o"
                    elif var1 == "You (s.)":
                        var2 = "as"
                    elif var1 == "He/She/It":
                        var2 = "a"
                    elif var1 == "We":
                        var2 = "amos"
                    elif var1 == "You (Pl.)":
                        var2 = "áis"
                    elif var1 == "They":
                        var2 = "an"
                elif word.endswith("er"):
                    inf = "er"
                    if var1 == "I":
                        var2 = "o"
                    elif var1 == "You (s.)":
                        var2 = "es"
                    elif var1 == "He/She/It":
                        var2 = "e"
                    elif var1 == "We":
                        var2 = "emos"
                    elif var1 == "You (Pl.)":
                        var2 = "éis"
                    elif var1 == "They":
                        var2 = "en"
                elif word.endswith("ir"):
                    inf = "ir"
                    if var1 == "I":
                        var2 = "o"
                    elif var1 == "You (s.)":
                        var2 = "es"
                    elif var1 == "He/She/It":
                        var2 = "e"
                    elif var1 == "We":
                        var2 = "imos"
                    elif var1 == "You (Pl.)":
                        var2 = "ís"
                    elif var1 == "They":
                        var2 = "en"
            elif te == "4":# SP FUTURE
                if word.endswith("ar"):
                    inf = "ar"
                    if var1 == "I":
                        var2 = "aré"
                    elif var1 == "You (s.)":
                        var2 = "arás"
                    elif var1 == "He/She/It":
                        var2 = "ará"
                    elif var1 == "We":
                        var2 = "emos"
                    elif var1 == "You (Pl.)":
                        var2 = "éis"
                    elif var1 == "They":
                        var2 = "án"
                elif word.endswith("er"):
                    inf = "er"
                    if var1 == "I":
                        var2 = "eré"
                    elif var1 == "You (s.)":
                        var2 = "erás"
                    elif var1 == "He/She/It":
                        var2 = "erá"
                    elif var1 == "We":
                        var2 = "emos"
                    elif var1 == "You (Pl.)":
                        var2 = "éis"
                    elif var1 == "They":
                        var2 = "án"
                elif word.endswith("ir"):
                    inf = "ir"
                    if var1 == "I":
                        var2 = "iré"
                    elif var1 == "You (s.)":
                        var2 = "irás"
                    elif var1 == "He/She/It":
                        var2 = "irá"
                    elif var1 == "We":
                        var2 = "iremos"
                    elif var1 == "You (Pl.)":
                        var2 = "iréis"
                    elif var1 == "They":
                        var2 = "án"
            elif te == "5":#SP CONDITIONAL
                if word.endswith("ar"):
                    inf = "ar"
                    if var1 == "I":
                        var2 = "aría"
                    elif var1 == "You (s.)":
                        var2 = "arías"
                    elif var1 == "He/She/It":
                        var2 = "aría"
                    elif var1 == "We":
                        var2 = "aríamos"
                    elif var1 == "You (Pl.)":
                        var2 = "aríais"
                    elif var1 == "They":
                        var2 = "arían"
                elif word.endswith("er"):
                    inf = "er"
                    if var1 == "I":
                        var2 = "ería"
                    elif var1 == "You (s.)":
                        var2 = "erías"
                    elif var1 == "He/She/It":
                        var2 = "ería"
                    elif var1 == "We":
                        var2 = "eríamos"
                    elif var1 == "You (Pl.)":
                        var2 = "eríais"
                    elif var1 == "They":
                        var2 = "erían"
                elif word.endswith("ir"):
                    inf = "ir"
                    if var1 == "I":
                        var2 = "iría"
                    elif var1 == "You (s.)":
                        var2 = "irías"
                    elif var1 == "He/She/It":
                        var2 = "iría"
                    elif var1 == "We":
                        var2 = "iríamos"
                    elif var1 == "You (Pl.)":
                        var2 = "iríais"
                    elif var1 == "They":
                        var2 = "irían"
                else:
                    oops()
            else:
                oops()
#        elif la == "b":# FRENCH
#            if te == "1":# FR PAST
#                if word.endswith("er"):
#                    inf = "er"
#                    if var1 == "I":
#                        var2 = "é"
#                    elif var1 == "You (s.)":
#                        var2 = "é"
#                    elif var1 == "He/She/It":
#                        var2 = "é"
#                    elif var1 == "We":
#                        var2 = "é"
#                    elif var1 == "You (Pl.)":
#                        var2 = "é"
#                    elif var1 == "They":
#                        var2 = "é"
#                elif word.endswith("ir"):
#                    inf = "ir"
#                    if var1 == "I":
#                        var2 = "i"
#                    elif var1 == "You (s.)":
#                        var2 = "i"
#                    elif var1 == "He/She/It":
#                        var2 = "i"
#                    elif var1 == "We":
#                        var2 = "i"
#                    elif var1 == "You (Pl.)":
#                        var2 = "i"
#                    elif var1 == "They":
#                        var2 = "i"
#                elif word.endswith("re"):
#                    inf = "re"
#                    if var1 == "I":
#                        var2 = "u"
#                    elif var1 == "You (s.)":
#                        var2 = "u"
#                    elif var1 == "He/She/It":
#                        var2 = "u"
#                    elif var1 == "We":
#                        var2 = "u"
#                    elif var1 == "You (Pl.)":
#                        var2 = "u"
#                    elif var1 == "They":
#                        var2 = "u"
#            elif te == "2":# FR PRESENT
#                if word.endswith("er"):
#                    inf = "er"
#                    if var1 == "I":
#                        var2 = "e"
#                    elif var1 == "You (s.)":
#                        var2 = "es"
#                    elif var1 == "He/She/It":
#                        var2 = "e"
#                    elif var1 == "We":
#                        var2 = "ons"
#                    elif var1 == "You (Pl.)":
#                        var2 = "ez"
#                    elif var1 == "They":
#                        var2 = "ent"
#                elif word.endswith("ir"):
#                    inf = "ir"
#                    if var1 == "I":
#                        var2 = "is"
#                    elif var1 == "You (s.)":
#                        var2 = "is"
#                    elif var1 == "He/She/It":
#                        var2 = "it"
#                    elif var1 == "We":
#                        var2 = "issons"
#                    elif var1 == "You (Pl.)":
#                        var2 = "issez"
#                    elif var1 == "They":
#                        var2 = "issent"
#                elif word.endswith("re"):
#                    inf = "re"
#                    if var1 == "I":
#                        var2 = "s"
#                    elif var1 == "You (s.)":
#                        var2 = "s"
#                    elif var1 == "He/She/It":
#                        var2 = ""
#                    elif var1 == "We":
#                        var2 = "ons"
#                    elif var1 == "You (Pl.)":
#                        var2 = "ez"
#                    elif var1 == "They":
#                        var2 = "ent"
#            elif te == "3":# FR FUTURE
#                if word.endswith("er"):
#                    inf = "er"
#                    if var1 == "I":
#                        var2 = "ai"
#                    elif var1 == "You (s.)":
#                        var2 = "as"
#                    elif var1 == "He/She/It":
#                        var2 = "a"
#                    elif var1 == "We":
#                        var2 = "ons"
#                    elif var1 == "You (Pl.)":
#                        var2 = "ez"
#                    elif var1 == "They":
#                        var2 = "ont"
#                elif word.endswith("ir"):
#                    inf = "ir"
#                    if var1 == "I":
#                        var2 = "ai"
#                    elif var1 == "You (s.)":
#                        var2 = "as"
#                    elif var1 == "He/She/It":
#                        var2 = "a"
#                    elif var1 == "We":
#                        var2 = "ons"
#                    elif var1 == "You (Pl.)":
#                        var2 = "ez"
#                    elif var1 == "They":
#                        var2 = "ont"
#                elif word.endswith("re"):
#                    inf = "re"
#                    if var1 == "I":
#                        var2 = "ai"
#                    elif var1 == "You (s.)":
#                        var2 = "as"
#                    elif var1 == "He/She/It":
#                        var2 = "a"
#                    elif var1 == "We":
#                        var2 = "ons"
#                    elif var1 == "You (Pl.)":
#                        var2 = "ez"
#                    elif var1 == "They":
#                        var2 = "ont"
#                else:
#                    oops()
#            else:
#                oops()
        else:
            oops()

        #Removes ar, er, ir and re
        if word.endswith("ar"):
            stem = word.replace('ar', '')#Removes AR
        elif word.endswith("er"):
            stem = word.replace('er', '')#Removes ER
        elif word.endswith("ir"):
            stem = word.replace('ir', '')#Removes IR
        elif word.endswith("re"):
            stem = word.replace('re', '')#Removes RE
        else:
            oops()
        #Tells user what to change verb to
        print("Change " + word + " to <" + var1 + ">")
        answer = input(stem)
        correct = stem + var2
        def writething():
            if answer == var2:
                if la == "a":
                    call('color AE', shell=True)
                elif la == "b":
                    call('color A9', shell=True)
                print("Correct!")
                check = "Correct   :)"
            elif answer != var2:
                if la == "a":
                    call('color CE', shell=True)
                elif la == "b":
                    call('color C9', shell=True)
                print("Incorrect.")
                print("Correct answer: " + correct)
                check = "Incorrect :("
            else:
                oops()
            now = datetime.now()
            ho = now.hour
            mi = now.minute
            da = now.day
            mo = now.month
            ye = now.year
            ho = str(ho)
            mi = str(mi)
            da = str(da)
            mo = str(mo)
            ye = str(ye)
            file_handle = open ("record.txt", "a")
            file_handle.write(check)
            file_handle.write(" | ")
            file_handle.write("at ")
            file_handle.write(ho)
            file_handle.write(":")
            file_handle.write(mi)
            file_handle.write(" on ")
            file_handle.write(da)
            file_handle.write("-")
            file_handle.write(mo)
            file_handle.write("-")
            file_handle.write(ye)
            file_handle.write("\n")
            file_handle.close
            sleep(2)
            go()
            os.system('cls')
            if la == "a":
                call('color 0E', shell=True)
            elif la == "b":
                call('color 09', shell=True)
        writething()
def choose():
    os.system('cls')
    print("╔════════════════════════╗")
    print("║Verb Ending Revision ^.^║")
    print("╠════════════════════════╣")
    print("║Languages and Tenses:   ║")
    print("║a) Spanish              ║")
    print("║  1) Imperfect          ║")
    print("║  2) Preterite          ║")
    print("║  3) Present            ║")
    print("║  4) Future             ║")
    print("║  5) Conditional        ║")
    print("║b) French               ║")
    print("║  1) Past               ║")
    print("║  2) Present            ║")
    print("║  3) Future             ║")
    print("╚════════════════════════╝")
    #╣║╗╝╚╔╩╦╠═╬
    try:#Used try as there were errors previously
        la = input("Language: ")
        te = input("Tense:    ")
    except:
        oops()
    sleep(2)
    os.system('cls')
    if la == "a":
        call('color 0E', shell=True)
    elif la == "b":
        call('color 09', shell=True)
    else:
        oops()
    #Alt codes for people without those sybols on their keyboard map
    ##print("!!! Important !!!")
    ##print("Some characters have special symbols.")
    ##print("Please take note of the following Alt Codes")
    ##print("if your keyboard is not set to Spanish/French.")
    ##print("")
    ##print("Alt + 0225 | á")
    ##print("Alt + -131 | â")
    ##print("Alt + 0233 | é")
    ##print("Alt + -136 | ê")
    ##print("Alt + 0237 | í")
    ##print("Alt + -140 | î")
    ##print("Alt + -162 | ó")
    ##print("Alt + -147 | ô")
    ##print("Alt + -163 | ú")
    ##print("Alt + -150 | û")
    ##print("")
    ##sleep(2)
    ##go()
    ##os.system('cls')
    main()
    #val()
#def val():
#    print("You have chosen " + la + te)
#    print("Would you like to continue? y/n")
#    valyn = input("")
#    if valyn == "y" or valyn == "Y":
#        main()
#    elif valyn == "n" or valyn == "N":
#        choose()
#    else:
#        oops()
choose()
