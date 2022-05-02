from interface_game.environment import *
from Minimax_Interface_Isolation import *
import copy
from Minimax_Isolation import *

class iMinimaxVSMinimax(BaseEnvironment):
    def __init__(self,depth,path={}):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = 1
        self.player_mark = 1
        self.path = path

    def env_act(self):
        
        pass

    def env_step(self, action):
        pass
        
    def env_cleanup(self):
        pass

    def env_message(self, message):
        pass
        
    def reset(self,player,depth,path):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = player
        self.player_mark = 1
        return copy.deepcopy(self.board)
    
    def check_win(self):
        point,flag = self.env.check_win(self.board,self.current_turn)
        return point,flag
    
    def step(self,action):
        old,new = action
        self.env.move_piece(self.env.board,self.current_turn,old,new)
        self.board = self.env.board
        reward,done = self.check_win()
        self.current_turn = -1 * self.current_turn
        if done:
            return copy.deepcopy(self.board), reward, done
        reward,done = self.env_act()
        return copy.deepcopy(self.board),reward,done
    
    def isValid(self,action):
        pass
    
class iMinimaxVSHuman(BaseEnvironment):
    pass

class iHumanVSHuman(BaseEnvironment):
    pass

class iGenVSHuman(BaseEnvironment):
    pass

#==============COMING SOON=============