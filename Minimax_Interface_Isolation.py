from interface_game.Minmax_class import *

class MinimaxII(MinimaxInterface):
    def __init__(self,depth,path = {}):
        self.env = MinimaxIsolation(depth,None)
        self.path = path
        self.depth = depth
        self.board = self.end.board
        
    def get_act_space(self,board,player):
        player_pos = self.env.action_pos[player]
        new_space = self.env.get_all_empty_cell(board,player_pos[0],player_pos[1])
        
        action_space = [(player_pos,cell) for cell in new_space]
        return action_space
        
    def sample_act(self,board,player):
        action_space = self.get_act_space(board,player)
        cell = np.random.choice(action_space)
        
        old,new = cell
        self.env.move_piece(board,player,old,new)
        self.board = board
        return old,new
    
    def minimax_act(self,board,player):
        if self.depth == 0:
            return self.sample_act(board,player)
        old,new = self.env.aimove(board,player)        
        return old,new
    
    def getBoard(self):
        pass