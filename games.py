from validacoes import *
from agenda import *
from random import randint
import os

diary1 = diary

def gaming():
    os.system("cls")
    option = ''
    print('You chose the games option!')
    print('Welcome to the player options menu')
    print('Do you want to continue?')
    print('if yes, type -> Yes')
    print('If not, type -> No')
    
    
    user = str(input("What's your choice: ")).lower()
    if user == 'no':
        print('Good bye')
    if user == 'yes':
        while user == 'yes':
            print('Welcome to the games menu, take your pick! ')
            print('''
            | ===================================================== |
            | ----------------------------------------------------- |
            | ==================== GAMES! ========================= |
            | ---------- 1 - Gessing Game \U0001F3B2 -------------- |
            | ---------- 2 - Tic-Tak-Toe Game \U0001F475 ---------- |
            | ---------- 3 - Jokenpô \u2702\uFE0F ----------------- |
            | ---------- 4 - Saída \U0001F6B6 --------------------- |
            | ----------------------------------------------------- |
            | ===================================================== |
            ''')

            player = str(input("What's your choice: ")).lower()
            if player == '1':
                acertou = False
                while option != '0' and not acertou:
                    
                    print('Welcome to the Guessing Game')
                    print("=="*20)
                    time.sleep(1)
                    print('The game has two phases')
                    print("let's go to the first phase...")
                    time.sleep(1)
                    print('''GAME RULES:
                    ['Rule 1° = Chose one number]
                    ['Rule 2° = Be very lucky]
                    ['Rule 3° = follow the first two \U0001F605]
                    ''')
                    CPU = randint(1,9)
                    player_game = int(input('Try to hit a value: '))
                    i = 1
                    while player_game != CPU and i < 3:
                        print('You missed!')
                        if player_game > CPU:
                            print('You went too far, go back a little...')
                        else:
                            print('You need to climb this mountain more, keep going!')
                        player_game = int(input('Try to hit a value: '))
                        
                        i += 1
                    
                    if player_game == CPU:
                            print('You got it right after %d trying'%i)

                    elif player_game != CPU:
                        print('You failed even with 3 attempts!!')

                    if i == 1 and player_game == CPU:
                        print("Beginner's luck \U0001F602")
                    elif i == 2 and player_game == CPU:
                        print('You were pretty insightful but it was still luck!\U0001F92D')
                    elif i == 3 and player_game == CPU:
                        print('You were very perceptive, an excellent strategist, Sun Tzu would be jealous of you!\U0001F44F')
                    else:
                            print("It wasn't this time, but don't give up! \U0001F4AA")  
                                
                    print('CPU value = {}'.format(CPU))
                    time.sleep(2)
                    print('*=='*30)
                    print('==*'*30)
                    print("You made it to the second level, whether or not you hit the first one, no problem!!")
                    print('Keep going with the game!!!')
                    print('The challenge now is to hit a number between 1 and 100!')
                    print('GOOD LOOK DUDE')
                    print("Let's start the second challenge, now much bigger than the first!")
                    print('Wait a minute!')
                    print('LOADING \U0001F3B2...')
                    time.sleep(5) #Aqui foi um plus, lembrei que existia esse comando de sleep e decidir usar
                    #para parecer que estamos num jogo de verdade com tela de carregamento.
                    print("all ready, let's start!")
                    #Professor, quis fazer o desafio na sequênca, como se fosse um próximo nível
                    import random
                    cpu = random.randint(1, 100)
                    min = 1 #minimo de números na faixa de representação
                    max = 100 #máxmo na faixa de representação
                    disqua = False #varável para desclassificação
                    player_game2 = int(input('Try to hit a value:: '))
                    if player_game2 < min or player_game2 > max:
                        disqua = True
                    plays = 1
                    while player_game2 != cpu and plays < 10 and not disqua:
                        print("you didn't get friend...")
                        if player_game2 < min or player_game2 > max:
                            disqua = True
                        else:
                            if player_game2 > cpu:
                                print("Boy... I'd say it's lower \U0001F602")
                                max = player_game2 - 1
                            else:
                                print('The answer is a hill... go higher!')
                                min = player_game2 + 1 
                            print('You only have more %d plays champion'%(10-plays))
                            player_game2 = int(input('Digite seu palpite: '))
                            plays += 1
                    if player_game2 == cpu:
                        
                        print('You got it... after {} plays'.format(plays))
                        if plays == 1:
                            print('You are very lucky, congratulations!!! \U0001F970')
                        elif plays <= 4:
                            print('Okay, you got it after {} tries but stil, but still it was very lucky! \U0001F605'.format(plays))
                        elif plays <= 7:
                            print('You are a great strategist, but you need to improve a lot! \U0001F60A')
                            
                        else:
                            print('You got it, but i recommend more training! \U0001F601')
                        acertou = True

                    elif disqua == True:
                        acertou = True
                        print('...Unfortunately you broke the limits of representation, you are disqualified!')
                        print('REASON: You selected a number below or above the tip')
                        print('''Because there are two ways to declassify:
            1st - choose a number less than 1 and greater than 100
            2nd - your next guess after the first one disobeys the hint, for example:
            your guess was 20, the answer is 18, the hint will suggest you a number less than 20
            if you choose 21, for example, you will be disqualified, as the range will be reduced to
            1 and 19.''')#Quis esclarecer aqui como funciona o sistema de desclassificação
                        print('Minimum value was: ', min)
                        print('Maximum value was: ', max)
                        print('The computer chose: ', CPU)
                    else:
                        acertou = True
                        print("Oops, unfortunately you didn't get it right and exceeded the number of moves")
                        print('The number was: {}'.format(CPU))
                    print('END GAME!')


                

                
            
            elif player == '2':
                while option != '0':
                    print('''Welcome to Tic-tac-to
                    one of the oldest games and for sure one of the first you played in your childhood.
                    ''')
                    print('lets go...')
                    time.sleep(1)
                    old = [

                                ['_', '_', '_'],
                                ['_', '_', '_'],
                                ['_', '_', '_']
                            
                            ]

                    #condicionais de vitória e de jogadas   
                    win = False
                    play = 0
                    draw = False
                    #laço de repetição
                    while play < 10 and not(win):
                        print("Board")
                        for i in range(3):
                            for j in range(3):
                                print(old[i][j], end=' ')
                            print()  
                        #espaçamento
                        
                        print("\nPlayer X it's your turn!")
                        i = int(input('Inform the line: '))
                        j = int(input('Inform the column: '))
                        old[i-1][j-1] = 'X'
                        print("Board")
                        for i in range(3):
                            for j in range(3):
                                print(old[i][j], end=' ')
                            print()
                        #condicionais de teste 
                        if (old[0][0] == old[0][1]) and (old[0][1] == old[0][2]) and (old[0][2] != '_'):
                            win= True
                        elif (old[1][0] == old[1][1]) and (old[1][1] == old[1][2]) and (old[1][2] != '_'):
                            win = True
                        elif (old[2][0] == old[2][1]) and (old[2][1] == old[2][2]) and (old[2][2] != '_'):
                            win = True
                        elif (old[0][0] == old[1][0]) and (old[1][0] == old[2][0]) and (old[2][0] != '_'):
                            win = True
                        elif (old[0][1] == old[1][1]) and (old[1][1] == old[2][1]) and (old[2][1] != '_'):
                            win = True
                        elif (old[0][2] == old[1][2]) and (old[1][2] == old[2][2]) and (old[2][2] != '_'):
                            win = True
                        elif (old[0][0] == old[1][1]) and (old[1][1] == old[2][2]) and (old[2][2] != '_'):
                            win = True
                        elif (old[0][2] == old[1][1]) and (old[1][1] == old[2][0]) and (old[2][0] != '_'):
                            win = True

                        if win == True:
                            print("Calculating result...")
                            time.sleep(1)
                            print('Player X WINS!!!')
                        
                        else:
                            print("\nPlayer Y its's your turn!")
                            i = int(input('Inform the line: '))
                            j = int(input('Inform the column: '))
                            old[i-1][j-1] = 'Y'
                            if (old[0][0] == old[0][1]) and (old[0][1] == old[0][2]) and (old[0][2] != '_'):
                                win= True
                            elif (old[1][0] == old[1][1]) and (old[1][1] == old[1][2]) and (old[1][2] != '_'):
                                win = True
                            elif (old[2][0] == old[2][1]) and (old[2][1] == old[2][2]) and (old[2][2] != '_'):
                                win = True
                            elif (old[0][0] == old[1][0]) and (old[1][0] == old[2][0]) and (old[2][0] != '_'):
                                win = True
                            elif (old[0][1] == old[1][1]) and (old[1][1] == old[2][1]) and (old[2][1] != '_'):
                                win = True
                            elif (old[0][2] == old[1][2]) and (old[1][2] == old[2][2]) and (old[2][2] != '_'):
                                win = True
                            elif (old[0][0] == old[1][1]) and (old[1][1] == old[2][2]) and (old[2][2] != '_'):
                                win = True
                            elif (old[0][2] == old[1][1]) and (old[1][1] == old[2][0]) and (old[2][0] != '_'):
                                win = True
                                
                                #encerramento do laço

                            if win == True:
                                
                                print('Calculating result...')
                                time.sleep(1)
                                print('Player Y WINS!!!')
                                play += 1
                            while play >= 9:
                                draw = True
                                print('Deu velha')
                                play +=1
                            
                    print('End of the phase!')
                    print('==*'*30)
                    print('==*'*30)
            elif player == '3':
                from random import choice
                print('Welcome to JOKENPÔ')
                time.sleep(1)
                print('===*'*20)
                print('''The game consists of you choosing rock, paper or scissors, and you will try to beat the CPU,
                good look...''')
                print("Loading...")
                time.sleep(1)

                items = ['Stone', 'Paper', 'Scissors']

                CPU = items.index(choice(items))
                print('''Your Options:
                [ 0 ] STONE
                [ 1 ] PAPER
                [ 2 ] SCISSORS''')
                player = int(input("What's your move: "))
                
                count = 0
                
                while True:
                    if player > 2:
                        print('Número inválido')
                        player = int(input('Qual é a sua jogada: '))
                        count += 1
                    else:
                        print('CPU playing: {}'.format(items[CPU]))
                        print('Player playing: {}'.format(items[player]))
                        if CPU == 0:
                            if player == 0:
                                time.sleep(1)
                                print('Draw')
                            elif player == 1:
                                time.sleep(1)
                                print('Player Wins!')
                            elif player == 2:
                                time.sleep(1)
                                print('CPU Wins!')
                        elif CPU == 1:
                            if player == 0:
                                time.sleep(1)
                                print('CPU Wins!')
                            elif player == 1:
                                time.sleep(1)
                                print('Draw')
                            elif player == 2:
                                time.sleep(1)
                                print('Player Wins!')
                        elif CPU == 2:
                            if player == 0:
                                time.sleep(1)
                                print('Player Wins!')
                            elif player == 1:
                                time.sleep(1)
                                print('CPU Wins!')
                            elif player == 1:
                                time.sleep(1)
                                print('Draw')
                        player = int(input('Qual é a sua jogada: '))
                        count +=1
                    
            else:
                print('Bye!')
                
                
                



