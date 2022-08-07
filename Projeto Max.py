import os
import time
from random import randint
from time import sleep
from agenda import *
import games
import utilidades




diary = []
while True:
    os.system("cls")
    option = ''
    print('WELCOME TO UFRN \U0001f600 !!!')
    print('''My name is Helena \U0001F600 , i'm the campus virtual assistant, 
i'm here to help you.
    ''')
    print('But first, i need to ask you a question...')
    time.sleep(1)
    print('You want to access the options menu?')
    print('if yes, type -> Yes')
    print('if not, type -> No')
    print('if bônus, type -> Game')
    print('if Utilites, type -> Utilites')

    user = str(input("What's your choice: ")).lower()
    if user == 'yes':
        book()

    elif user == 'no':
        print("Damn, I'll miss you, but thanks for dropping by")
        print("See you \N{slightly smiling face}")
    elif user == 'game':
        games()

    elif user == "utilites":
        utilidades.utili()
    else:
        print("Invalid option")

    

                            
                                
                            
                            




        





