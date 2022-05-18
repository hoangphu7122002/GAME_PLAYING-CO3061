import numpy as np
import math
import pygame
import sys
import copy
from GUI import *
from parameter import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
board_game = np.ones((SHAPE[1], SHAPE[0])) * (FREE)
board_game[POS['ACTIVE_P1'][0]][POS['ACTIVE_P1'][1]] = ACTIVE_P1
board_game[POS['ACTIVE_P2'][0]][POS['ACTIVE_P2'][1]] = ACTIVE_P2


### HELPER FUNCTION
def drawGrid():
    for r in range(0, SHAPE[1]):
        for c in range(0, SHAPE[0]):
            rect = pygame.Rect(c * EDGE + MARGIN, r * EDGE + MARGIN, EDGE - 2*MARGIN, EDGE - 2*MARGIN)
            if board_game[r][c] != BLOCK:                 
                pygame.draw.rect(screen, YELLOW, rect)
            elif board_game[r][c] == BLOCK:
                pygame.draw.rect(screen, BLACK, rect)
            
    for i in range(len(POS['VALID'])):
        rect = pygame.Rect(POS['VALID'][i][1] * EDGE + MARGIN, POS['VALID'][i][0] * EDGE + MARGIN, EDGE - 2*MARGIN, EDGE - 2*MARGIN)      
        pygame.draw.rect(screen, GREEN, rect)  
    pygame.draw.circle(screen, RED, (POS['ACTIVE_P1'][1] * EDGE + int(EDGE / 2), POS['ACTIVE_P1'][0] * EDGE + int(EDGE / 2)), int(EDGE / 2 - 2*MARGIN)) 
    pygame.draw.circle(screen, BLUE, (POS['ACTIVE_P2'][1] * EDGE + int(EDGE / 2), POS['ACTIVE_P2'][0] * EDGE + int(EDGE / 2)), int(EDGE / 2 - 2*MARGIN))  
    # print(POS['SELECT'])

def getKeyboard():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                # print(pygame.mouse.get_pos())
                POS['SELECT'] = [int((pygame.mouse.get_pos()[1] - OFFSET) / EDGE), int((pygame.mouse.get_pos()[0] - OFFSET) / EDGE)]
                # print(POS['SELECT'])
                if not POS['SELECT'] in POS['VALID']:
                    continue
                # rect = pygame.Rect(POS['SELECT'][1] * EDGE, POS['SELECT'][0] * EDGE, EDGE, EDGE)   
                # pygame.draw.rect(screen, YELLOW, rect)
                global TURN
                valid = False
                if TURN[0] == 0:
                    board_game[POS['ACTIVE_P1'][0]][POS['ACTIVE_P1'][1]] = FREE
                    POS['ACTIVE_P1'] = copy.deepcopy(POS['SELECT'])
                    board_game[POS['ACTIVE_P1'][0]][POS['ACTIVE_P1'][1]] = ACTIVE_P1
                    ### move selected quickly
                    POS['VALID'].clear()
                    for r in range(0, SHAPE[0]):
                        for c in range(0, SHAPE[1]):
                            if (board_game[r][c] == FREE and [r, c] != POS['ACTIVE_P1'] and [r, c] != POS['ACTIVE_P2']):
                                POS['VALID'].append([r, c])
                    #####
                    valid = True
                elif TURN[0] == 1 or TURN[0] == 3:
                    # if (board_game[POS['SELECT'][0]][POS['SELECT'][1]] == FREE):
                    board_game[POS['SELECT'][0]][POS['SELECT'][1]] = BLOCK
                    ### move selected quickly
                    if TURN[0] == 1:
                        POS['VALID'].clear()
                        for i in range(0, len(dx)):
                            if (POS['ACTIVE_P2'][0] +dx[i] in range(0, SHAPE[0]) and POS['ACTIVE_P2'][1] +dy[i] in range(0, SHAPE[1]) and board_game[POS['ACTIVE_P2'][0] +dx[i]][POS['ACTIVE_P2'][1] +dy[i]] == FREE):
                                POS['VALID'].append([POS['ACTIVE_P2'][0] +dx[i], POS['ACTIVE_P2'][1] +dy[i]])
                    elif TURN[0] == 3:
                        POS['VALID'].clear()
                        for i in range(0, len(dx)):
                            if (POS['ACTIVE_P1'][0] +dx[i] in range(0, SHAPE[0]) and POS['ACTIVE_P1'][1] +dy[i] in range(0, SHAPE[1]) and board_game[POS['ACTIVE_P1'][0] +dx[i]][POS['ACTIVE_P1'][1] +dy[i]] == FREE):
                                POS['VALID'].append([POS['ACTIVE_P1'][0] +dx[i], POS['ACTIVE_P1'][1] +dy[i]])
                    #####
                    valid = True
                elif TURN[0] == 2:
                    # if (abs(POS['SELECT'][0] - POS['ACTIVE_P2'][0]) + abs(POS['SELECT'][1] - POS['ACTIVE_P2'][1]) == 1):
                    board_game[POS['ACTIVE_P2'][0]][POS['ACTIVE_P2'][1]] = FREE
                    POS['ACTIVE_P2'] = copy.deepcopy(POS['SELECT'])
                    board_game[POS['ACTIVE_P2'][0]][POS['ACTIVE_P2'][1]] = ACTIVE_P2
                    valid = True
                    ### move selected quickly
                    POS['VALID'].clear()
                    for r in range(0, SHAPE[0]):
                        for c in range(0, SHAPE[1]):
                            if (board_game[r][c] == FREE and [r, c] != POS['ACTIVE_P1'] and [r, c] != POS['ACTIVE_P2']):
                                POS['VALID'].append([r, c])
                    #####
                if valid:
                    TURN[0] = (TURN[0] + 1) % 4
        

def result():
    global ENDGAME
    if len(POS['VALID']) == 0:
        ENDGAME[0] = True

### MAIN
def main():
    for i in range(0, len(dx)):
        if (POS['ACTIVE_P1'][0] +dx[i] in range(0, SHAPE[0]) and POS['ACTIVE_P1'][1] +dy[i] in range(0, SHAPE[1]) and board_game[POS['ACTIVE_P1'][0] +dx[i]][POS['ACTIVE_P1'][1] +dy[i]] == FREE):
            POS['VALID'].append([POS['ACTIVE_P1'][0] +dx[i], POS['ACTIVE_P1'][1] +dy[i]])
    # print(POS['VALID'])
    #####
    while True:
        result()
        a = Gui(board_game)
        a.display()
        getKeyboard()
        # pygame.display.update()
main()