
import time
from validacoes import *
import pickle
import os

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

diary = listbook()


def book():
    while True:
        os.system("cls")
        print('Wonderfull, you chose to access the menu')
        print("Let's go \U0001F51B ...")
        time.sleep(1)
        print(''' 
            | ===================================================== |
            | ----------------------------------------------------- |
            | ------------- Contact Book \U0001F4D5 --------------- |
            | ----------------------------------------------------- |
            | ------------- 1 - Register \U0001F4D6 --------------- |
            | ------------- 2 - Search   \U0001F513 --------------- |
            | ------------- 3 - Edit     \U0001F513 --------------- |
            | ------------- 4 - Remove   \U0001F504 --------------- |
            | ------------- 5 - Close    \U0001F519 --------------- |
            | ----------------------------------------------------- |
            | ===================================================== |
            ''')
        option = input('Choose one of the options: ')
        if option == '1':
            os.system("cls")
            print("Let's register you in the system")
            contact = []
            while True:
                name = input('Please, type your name: ').lower()
                if validstring(name):
                    contact.append(name)
                    break
                else:
                    print('Invalid name')
            while True:
                email = input('Please, type your email: ').lower()
                if validemail(email):
                    contact.append(email)
                    break
                else:
                    print('Invaldi email')

            fone = int(input('Please, enter your contact number: '))
            contact.append(fone)
            cpf = input("Please, type your CPF: ")
            if cadastrocpf(cpf):
                diary[cpf] = contact
                print("Contact registred sucessfully")
                savebook(diary)
            print('Congratulations, your registration was succesfull!!! \U0001F929')
            print('Loading Menu...')
            time.sleep(1)
            
        
        elif option == '2':
            while True:
                os.system("cls")
                print('We will show you all registered contacts!')
                time.sleep(1)
                print('Loading Contacts..')
                cpf = input('Insert your CPF:')
                if cpf not in diary:
                    print('CPF not found')
                    book()
                else:
                    print("CPF found")
                    print(diary[cpf])
                input("Press ENTER to return to the menu")
                book()

        
        elif option == '3':
            while True:
                os.system("cls")
                print("Let's change your data")
                print("Loading...")
                time.sleep(1)
                cpf = input("Inser your CPF: ")
                if cadastrocpf(cpf):
                    if cpf not in diary:
                        print("CPF not found")
                        input("Press ENTER to return to the menu")
                    else:
                        print('CPF found')
                        print(diary[cpf])
                        while True:
                            edit = input("Which item do you want to change? ").strip().upper()
                            if edit == 'name'.upper():
                                newname = input("Type your new name: ")
                                diary[cpf][0] = newname
                                print("Name changed sucessfully!")
                                savebook(diary)
                                input("Press ENTER to return to the menu")
                                book()
                            if edit == 'email'.upper():
                                newemail = input("Type your new email: ")
                                if validemail(newemail):
                                    diary[cpf][1] = newemail
                                    print("Email changed sucessfully!")
                                    savebook(diary)
                                    input("Press ENTER to return to the menu")
                                    book()
                                else:
                                    print("Invalid Email")
                            if edit == 'fone'.upper():
                                newfone = int(input("Type your new fone:"))
                                diary[cpf][2] = newfone
                                print('Fone changed sucessfully!')
                                savebook(diary)
                                input("Press ENTER to return to the menu")
                                book()
                            else:
                                print('Invalid option!')
                else:
                    print("CPF invalid!")


            

        
        elif option == '4':
            while True:
                os.system("cls")
                print("We'll find you some contact for you!")
                cpf_search = input('Which contact do you want to find in our system?: ')
                if cpf_search not in diary:
                    print("CPF not found")
                    book()
                else:
                    print("CPF found")
                    del diary[cpf_search]
                    print("Contact removed")
                    savebook(diary)
                input("Press ENTER to return to the menu")
                break
            
            
        elif option == '5':
            print()
            print('So do you want to go out menu?')
            print('Okay!')
            break
        
        else:
            print("Invalid Option")
    print('GOODBYE, COME BACK SOON \U0001F44B')