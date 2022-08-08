from validacoes import *
import os
from time import sleep
from agenda import *


diary2 = diary

def utili():
    os.system("cls")
    print('Welcome to utilities, here I bring you more options for our platform!')
    print('Do you want to continue?')
    print('if yes, type -> Yes')
    print('If not, type -> No')
    user = str(input("What's your choice: ")).lower()
    while True:
        if user == 'no':
            print('Okay, good bye!')
        if user == 'yes':
            while user == 'yes':
                os.system("cls")
                print('Welcome to utilities menu!!!')
                print('Please choose from the options below!')
                print('''  
                | --------------------- Menu Utilities \U0001f5fa\uFE0F --------------------- |
                | ------------------ 1 - Leap Year Calendar \U0001F4C5 ---------------------- |
                | ------------------ 2 - Average Calculator --------------------------------- |
                | --------------------------------------------------------------------------- |
                
                ''')

                user = str(input("What's your choice: ")).lower()
                
                if user == '1':
                    lapyear()
                elif user == '2':
                    calculator()





def calculator():
    os.system("cls")
    print("""
    
    | ============================================================= |
    | ------------------------------------------------------------- |
    | -------- Welcome to the average calculator to BSI! ---------- |
    | -------- Below are the articles from this period!  ---------- |
    | ============================================================= |
    | -------- Introduction to Informatics [1] -------------------- |
    | -------- General Theory of Administration [2] --------------- |
    | -------- Logic [3] ------------------------------------------ |
    | -------- Fundamentals of Mathematics [4] -------------------- |
    | -------- Algorithms and Programming Logic [5] --------------- |
    | ------------------------------------------------------------- |
    | ============================================================= |
    """)
    student = input('Choose an option: ')
    
    if student == '1':
        while True:
            os.system("cls")
            print("""Welcome to Introduction to Informatics!
            This is your average calculator for your first period of INTF!
            Given by: Prof Luiz Paulo
            Le'ts calculate your average this semester...""")
            print("""
            | ------------------------------ |
            | ========== Unity: 1 ========== |
            | ========== Unity: 2 ========== |
            | ========== Unity: 3 ========== |
            | ====== Final Result: 4 ======= |
            | ======== Exit Menu: 5 ======== |
            | ------------------------------ |
            """)
            print('Loading...')
            sleep(1)
            average = 0
            student = ' '
            student = input('Which unity do you want to access: ')
        
            if student == '1':
                    os.system("cls")
                    print('You chose to chek the first unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 2 avalutations')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    average1 = (note1 + note2 ) / 2
                    print('His average was {:.2f}'.format(average1))
                    if average1 >= 5:
                        print('Congratulations you PASSED with average {:.2f}!!!'.format(average1))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average1))
                    average += average1
                    savebook(diary2)
                    input("Tap for continue: ")

            elif student == '2':
                    os.system("cls")
                    print('You chose to chek the second unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 3 avalutations')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    note3 = float(input('Type your third note: '))
                    average2 = (note1 + note2 + note3 )/ 3
                    print('His average was {:.2f}'.format(average2))
                    if average2 >= 5:
                        print('Congratulations you PASSED with average {:.2f}!!!'.format(average2))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average2))
                    average += average2
                    savebook(diary2)
                    input("Tap for continue: ")
                    
                    
            elif student == '3':
                    os.system("cls")
                    print('You chose to chek the third unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 4 avalutations')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    note3 = float(input('Type your third note: '))
                    note4 = float(input('Type your four note: '))
                    average3 = (note1 + note2 + note3 + note4)/4
                    print('His average was {:.2f}'.format(average3))
                    if average3 >= 5:
                        print('Congratulations you PASSED with average {:.2f}!!!'.format(average3))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average3))
                    average += average3
                    savebook(diary2)
                    input("Tap for continue: ")
                    
                    
            elif student == '4':
                    os.system("cls")
                    if average / 3 >= 5:
                        print('Approved by Average!!! {:.2f}'.format(average/3))
                    else:
                        print("Failed but don't drop out of the course")
                    savebook(diary2)
                    input("Tap for continue: ")
                    
            elif student == '5':
                    os.system("cls")
                    print("Thank you, have a great day!")
                    break

            else:
                print('Invalid option, try again!')
                    
                    
            
    if student == '2':
        os.system("cls")
        while True:
            print("""Welcome to General Theory of Administration!
            This is your average calculator for your first period of TGA!
            Given by: Prof. Dra Adrianne Souza
            Le'ts calculate your average this semester...""")
            print('=+'*40)
            print("""
            | ------------------------------ |
            | ========== Unity: 1 ========== |
            | ========== Unity: 2 ========== |
            | ========== Unity: 3 ========== |
            | ====== Final Result: 4 ======= |
            | ======== Exit Menu: 5 ======== |
            | ------------------------------ |
            """)
            print('+='*40)
            print('Loading...')
            sleep(1)
            average = 0
            student = ' '
            student = input('Which unity do you want to access: ')
            
            if student == '1':
                    os.system("cls")
                    print('You chose to check the first unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 3 assessments')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    note3 = float(input('type your third note: '))
                    average1 = (note1 + note2 + note3) / 3
                    print('His average was {:.2f}'.format(average1))
                    if average1 >= 5:
                        print('Congratulations you passed with average {:.2f}'.format(average1))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average1))
                    savebook(diary2)
                    average += average1
                    
                
            elif student == '2':
                    os.system("cls")
                    print('You chose to check the second unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 3 assessments')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    note3 = float(input('Type your third note: '))
                    average2 = (note1 + note2 + note3 )/ 3
                    print('His average was {:.2f}'.format(average2))
                    if average2 >= 5:
                        print('Congratulations you passed with average {:.2f}'.format(average2))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average2))
                    savebook(diary2)
                    average += average2
                    
            elif student == '3':
                    os.system("cls")
                    print('You chose to check the third unite grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 4 assessments')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    note3 = float(input('Type your third note: '))
                    note4 = float(input('Type your four note: '))
                    average3 = (note1 + note2 + note3 + note4) / 4
                    print('His average was {:.2f}'.format(average3))
                    if average3 >= 5:
                        print('Congratulations you passed with average {:.2f}'.format(average3))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average3))
                    savebook(diary2)
                    average += average3
                    
                    
            elif student == '4':
                    os.system("cls")
                    if average / 3 >= 5:
                        print('Passed with average {:.2f}'.format(average / 3))
                    else:
                        print('Disapproved')
                    savebook(diary2)
            elif student == '5':
                    os.system("cls")
                    print("Thank you have a good day!")
                    break

            else:
                print('Invalid Option!')
            
    if student == '3':
        os.system("cls")
        while True:
            print("""Welcome to Logic!
            This is your average calculator for your first period of LGC!
            Given by: Prof Dr. João Paulo
            Le'ts calculate your average this semester...""")
            print('=+'*40)
            print("""
            | ------------------------------ |
            | ========== Unity: 1 ========== |
            | ========== Unity: 2 ========== |
            | ========== Unity: 3 ========== |
            | ====== Final Result: 4 ======= |
            | ======== Exit Menu: 5 ======== |
            | ------------------------------ |
            """)
            print('+='*40)
            print('Loading...')
            sleep(1)
            
            average = 0
            student = ' '
            student = input('Which unity do you want to access: ')
            if student == '1':
                os.system("cls")
                print('You chose to check the first unit grades')
                print('To be approved you need an average of 5')
                print('In this unit there will be 3 assessments')
                note1 = float(input('Type your first note: '))
                note2 = float(input('Type your second note: '))
                note3 = float(input('Type your third note: '))
                average1 = (note1 + note2 + note3) / 3
                print('His average was {:.2f}'.format(average1))
                if average1 >= 5:
                    print('Congratulations you passed with average {:.2f}'.format(average1))
                else:
                    print('Unfortunately you failed with average {:.2f}'.format(average1))
                average += average1
                savebook(diary2)
            
            elif student == '2':
                    os.system("cls")
                    print('You chose to check the second unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 3 assessments')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    note3 = float(input('Type your third note: '))
                    average2 = (note1 + note2 + note3 )/ 3
                    print('His average was {:.2f}'.format(average2))
                    if average2 >= 5:
                        print('Congratulations you passed with average {:.2f}'.format(average2))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average2))
                    average += average2
                    savebook(diary2)
                    
                    
            elif student == '3':
                    os.system("cls")
                    print('You chose to check the second unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 4 assessments')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    note3 = float(input('Type your third note: '))
                    note4 = float(input('Type your four note: '))
                    average3 = (note1 + note2 + note3 + note4) / 4
                    print('His average was {:.2f}'.format(average3))
                    if average3 >= 5:
                        print('Congratulations you passed with average {:.2f}'.format(average3))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average3))
                    average += average3
                    savebook(diary2)
                    
            elif student == '4':
                if student / 3 >= 5:
                    print('Passed with average {:.2f}'.format(médias/3))
                else:
                    print('Disapproved')
                        
            elif student == '5':
                print("Thank you have a good day!")
                break

            else:
                print("Invalid Option!")

    if student == '4':
        os.system("cls")
        while True:
            print("""Welcome to Fundamentals of Mathematics!
            This is your average calculator for your first period of FM!
            Given by: Prof Dr. Marcio Barboza
            Le'ts calculate your average this semester...""")
            print('=+'*40)
            print("""
            | ------------------------------ |
            | ========== Unity: 1 ========== |
            | ========== Unity: 2 ========== |
            | ========== Unity: 3 ========== |
            | ====== Final Result: 4 ======= |
            | ======== Exit Menu: 5 ======== |
            | ------------------------------ |
            """)
            print('+='*40)
            print('Loading...')
            sleep(1)

            average = 0
            student = input('Which unity do you want to access: ')
        
                
            if student == '1':
                    os.system("cls")
                    print('You chose to check the frist unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 4 assessments')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    note3 = float(input('Type your third note: '))
                    note4 = float(input('Type your four note: '))
                    average1 = (note1 + note2 + note3 + note4) / 4
                    print('His average was {:.2f}'.format(average1))
                    if average1 >= 5:
                        print('Congratulations you passed with average {:.2f}'.format(average1))
                    else:
                        print('Unfortunately you failed with average{:.2f}'.format(average1))
                    average += average1
                    savebook(diary2)
                    
            elif student == '2':
                    os.system("cls")
                    print('You chose to check the second unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 2 assessments')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    average2 = (note1 + note2 ) / 2
                    print('His average was {:.2f}'.format(average2))
                    if average2 >= 5:
                        print('Congratulations you passed with average {:.2f}'.format(average2))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average2))
                    average += average2
                    savebook(diary2)
                    
            elif student == '3':
                    os.system("cls")
                    print('You chose to check the third unit grades')
                    print('To be approved you need an average of 5')
                    print('In this unit there will be 2 assessments')
                    note1 = float(input('Type your first note: '))
                    note2 = float(input('Type your second note: '))
                    average3 = (note1 + note2 )/ 2
                    print('His average was {:.2f}'.format(average3))
                    if average3 >= 5:
                        print('Congratulations you passed with average {:.2f}'.format(average3))
                    else:
                        print('Unfortunately you failed with average {:.2f}'.format(average3))
                    average += average3
                    savebook(diary2)
                    
                    
            elif student == '4':
                    os.system("cls")
                    if average / 3 >= 5:
                        print('Passed with average {:.2f}'.format(average/3))
                    else:
                        print('Disapproved')
                    
            elif student == '5':
                print("Thank you have a good day!")
                break

            else:
                print("Invalid Option!")
            
    if student == '5':
        os.system("cls")
        while True:
            print("""Welcome to Algorithms and Programming Logic!
            This is your average calculator for your first period of ALP!
            Given by: Prof Dr. Flavius Gorgônio
            Le'ts calculate your average this semester...""")
            print('=+'*40)
            print("""
            | ------------------------------ |
            | ========== Unity: 1 ========== |
            | ========== Unity: 2 ========== |
            | ========== Unity: 3 ========== |
            | ====== Final Result: 4 ======= |
            | ======== Exit Menu: 5 ======== |
            | ------------------------------ |
            """)
            print('+='*40)
            print('Loading...')
            sleep(1)
            average = 0
            student = input('Which unity do you want to access: ')
            
            if student == '1':
                os.system("cls")
                print('You chose to check the first unit grades')
                print('To be approved you need on average of 5')
                print('In this unit there will be 5 assessments')
                note1 = float(input('Digite sua primeira nota: '))
                note2 = float(input('Digite sua segunda nota: '))
                note3 = float(input('Digite sua terceira nota: '))
                note4 = float(input('Digite sua quarta nota: '))
                note5 = float(input('Digite sua quinta nota: '))
                average1 = (note1 + note2 + note3 + note4 + note5) / 5
                print('His average was {:.2f}'.format(average1))
                if average1 >= 5:
                    print('Parabéns você foi aprovado com média {:.2f}'.format(media1))
                else:
                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media1))
                médias += media1
                

            elif aluno == '2':
                    
                    print('Você escolheu verificar as notas da segunda unidade')
                    print('Para ser aprovado você precisa de média 5')
                    print('Nesta unidade serão 5 avaliações')
                    nota1 = float(input('Digite sua primeira nota: '))
                    nota2 = float(input('Digite sua segunda nota: '))
                    nota3 = float(input('Digite sua terceira nota: '))
                    media2 = (nota1 + nota2 + nota3  )/ 3
                    print('Sua média foi de {:.2f}'.format(media2))
                    if media2 >= 5:
                        print('Parabéns, você foi aprovado com média {:.2f}'.format(media2))
                    else:
                        print('Infelizmente você foi reprovado com média {:.2f}'.format(media2))
                    médias += media2
                    
                    
            elif aluno == '3':
                    
                    print('Você escolheu verificar as notas da terceira unidade')
                    print('Para ser aprovado você precisa de média 5')
                    print('Nesta unidade serão 4 avaliações')
                    nota1 = float(input('Digite sua primeira nota: '))
                    nota2 = float(input('Digite sua segunda nota: '))
                    media3 = (nota1 + nota2 )/ 2
                    print('Sua média foi de {:.2f}'.format(media3))
                    if media3 >= 5:
                        print('Parabéns você foi aprovado com média {:.2f}'.format(media3))
                    else:
                        print('Infelizmente você foi reprovado com média {:.2f}'.format(media3))
                    médias+= media3
                    
                    
            elif aluno == '4':
                if médias / 3 >= 5:
                    print('Aprovado com média {:.2f}'.format(médias/3))
                    break
                else:
                    print('reprovado')
                    break
                
            elif aluno == '5':
                print("Obrigado, tenha um bom dia!")
                break

            else:
                print("Invalid Option!")
            
                

def lapyear():
    os.system("cls")
    print('''
    | ============================================================= |
    | ------------------------------------------------------------- |
    | ---------- Welcome to the leap year calculator! ------------- |
    | ---- let's check if the year you entered is valid or not ---- |
    | ------------------------------------------------------------- |
    | ============================================================= |
    ''')
    
    day = int(input('Inform the day: '))
    month = int(input('Inform the month: '))
    year = int(input('Inform the year: '))
    leap = year % 4 == 0 and year % 100 != 0 or year % 400 ==0

    print('You informed: month {} of the day {} of the year {}'.format(month, day, year))

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 31:
            print('Invalid Date')
    elif day > 31:
        print('Invalid Date')

    if month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30:
            print('Valid Date')
    elif day > 30 and month == 4 or month == 6 or month == 9 or month == 11:
            print('Invalid Date')
            if month <= 12 and month != 0:
                print('Valid Month')
            elif month > 12:
                print('Valid Month')
    if month == 2 and day > 31:
            print('Valid Month')

    if month == 2 and day >= 29 and leap == 0:
        print('Invalid date, does not exist this year')
    elif month == 2 and day <= 29 and leap:
        print('Valid date, leap year')
    elif month == 2 and day <= 28:
        print('Valid date, leap year')

    if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
        print('Leap Year!')
    else:
        print('Non-leap year')