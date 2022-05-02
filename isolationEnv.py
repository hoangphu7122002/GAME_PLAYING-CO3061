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
        old,new = self.env.aimove(self.env.board,self.current_turn)
        reward,done = self.check_win()
        self.current_turn = -1 * self.current_turn
        return reward,done

    def reset(self,player,depth,path):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = player
        self.player_mark = 1
        return copy.deepcopy(self.board)
    
    def action(self):
        pass
    
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
    
# class iMinimaxVSHuman(BaseEnvironment):
#     pass

class iHumanVSHuman(BaseEnvironment):
    def __init__(self,depth = 0,path={}):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = 1
        self.player_mark = 1
        self.path = path
        
    def env_act(self):
        pass
                
    def print_board(self):
        self.env.print_board(self.board)
        
    def reset(self,player,depth,path):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = player
        self.player_mark = 1
        return copy.deepcopy(self.board)
    
    def check_win(self):
        point,flag = self.env.check_win(self.board,self.current_turn)
        return point,flag
    
    def step(self):
        self.env.player_move(self.board,self.current_turn) 
        reward,done = self.check_win()
        self.current_turn = -1 * self.current_turn
        if done:
            return copy.deepcopy(self.board), reward, done
        return copy.deepcopy(self.board),reward,done

class iGenVSHuman(BaseEnvironment):
    pass

#==============COMING SOON=============