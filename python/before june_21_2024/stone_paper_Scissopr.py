import random
class game(object):
    def bot():
        ran=random.randint(1,3)
        print(ran)
        if ran==1:
            print("bot has choosen stone")
        elif ran==2:
            print("bot has choosen paper")
        elif ran==3:
            print("bot has choosen scissor")
        return ran
        
    
    def player():
        print("Enter :")
        print("1 for STONE")
        print("2 for PAPER")
        print("3 for SCISSOR")
        return (int(input(": ")))
    
    def gameplay(play,b):
        player=play
        bot=b
        if player==bot:
            return 0
         
        # bot win
        elif player==1 and bot==2: # 1 is stone 
            return 1
        elif player==2 and bot==3: # 2 is paper
            return 1
        elif player==3 and bot==1: # 3 is scissor
            return 1
        
        elif bot==1 and player==3: # 1 is stone 
            return 2
        elif bot==2 and player==3: # 2 is paper
            return 2
        elif bot==3 and player==1: # 3 is scissor
            return 2
        
    # bot()
    # player()
    # x=gameplay(player,bot)
    # print(x)
    cha=(int(input("Enter the Chance : ")))
    win=0
    for i in range(cha):
        play=player()
        b=bot()
        g=gameplay(play,b)
        if g==0:
            print("TIE")
        elif g==1:
            print("bot win")
        elif g==2:
            print("You Win")
            win=+1
    print('your score : ',win)
    