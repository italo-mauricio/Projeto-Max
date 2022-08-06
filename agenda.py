import time
from validacoes import *
import pickle


def listbook():
    try:
        booklist = open("booklist.dat", "rb")
        diary = pickle.load(booklist)
        booklist.close
    except:
        booklist = open("booklist.dat", "wb")
        booklist.close()
    return diary

def savebook(diary):
    booklist = open("booklist.dat", "wb")
    pickle.dump(diary, booklist)
    booklist.close()

diary = {}


def book():
    
    print('Wonderfull, you chose to access the menu')
    print("Let's go \U0001F51B ...")
    time.sleep(1)
    option = input("What is your option: ")
    while option != '0':
        print('''        ===============================================
        ===============================================
        =============== Contact Book \U0001F4D5 ===============
        ===============================================
        =============== 1 - Register \U0001F4D6 ===============
        =============== 2 - Display  \U0001F9D0 ===============
        =============== 3 - Search   \U0001F513 ===============
        =============== 4 - Remove   \U0001F504 ===============
        =============== 5 - Close    \U0001F519 ===============
        ===============================================
        ===============================================
        ''')
        option = input('Choose one of the options: ')
        contact = False
        if option == '1':
            print()
            print('You chose option 1')
            print("Let's register you in the system")
            contact = []
            name = input('Please, type your name: ').lower()
            contact.append(name)
            email = input('Please, type your email: ').lower()
            contact.append(email)
            fone = int(input('Please, enter your contact number: '))
            contact.append(fone)
            diary.append(contact)
            print('Congratulations, your registration was succesfull!!! \U0001F929')
            print('Loading Menu...')
            time.sleep(1)
            print()
            
        
        elif option == '2':
            print()
            print('You chose option 2')
            print('We will show you all registered contacts!')
            time.sleep(1)
            print('Loading Contacts..')
            for i in diary:
                print('Name:\t', i[0])
                print('Email:\t', i[1])
                print('Contact Number:\t', i[2])
                print()
                print('Wonderful, here are the contacts we found for you! \U0001F609')
                print('Loadin menu...')
                time.sleep(1)
        
        elif option == '3':
            print()
            print("You chose option 3")
            print("We'll find you some contact for you!")
            name_search = input('Which contact do you want to find in our system?: ')
            demand = False
            for people in diary:
                if name_search.upper() in people[0].upper():
                    demand = True
                    print('Searching...')
                    time.sleep(1)
                    print('We found!')
                    print('Name:\t', people[0])
                    print('Email:\t', people[1])
                    print('Contact Number:\t', people[2])
                    print('Hope it was of great help to you!\U0001F606')
            if not demand:
                print("Unfortunately we could't findthe contact \U0001F914")
                print("Loading Menu...")
                time.sleep(1)
            print()
        
        
        elif option == '4':
            print()
            print('You chose option 4')
            print('So you want to remove a contact from your diary?')
            print("Okay... let's go.")
            name_remove = input('Qual contato vc quer remover: ')
            remove = False
            for name_remove in diary:
                
                remove = True
                diary.remove(name_remove)
                print('Contato removido')
            if not remove:
                print('Opção inválida')
            
            
        elif option == '5':
            print()
            print('So do you want to go out menu?')
            print('Okay!')
            break
        
        else:
            print("Invalid Option")
    print('GOODBYE, COME BACK SOON \U0001F44B')