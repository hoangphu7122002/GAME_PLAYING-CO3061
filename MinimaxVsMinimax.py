from doctest import DONT_ACCEPT_BLANKLINE
from isolationEnv import *
from helper_function import *
from time import sleep

if __name__ == "__main__":
    env = iMinimaxVSMinimax(1000)
    max_step = 36
        
    for ep in range(1):
        depth1 = int(input('depth for maximizer: '))
        depth2 = int(input('depth for minimizer: '))
        player = 1
        done = False
        env.reset(depth1,depth2)
        
        print("START ISOLATION")
        
        for i in range(max_step):
            state,reward,done = env.step()
            if done:
                break
            print_board(env.board)
            sleep(2)
        if reward > 0:
            print("player1 WON!!!: ",reward)
        elif reward < 0:
            print("player2 WON!!!: ",reward)
        else:
            print("GAME TIE!!!")
        
        print("log out")