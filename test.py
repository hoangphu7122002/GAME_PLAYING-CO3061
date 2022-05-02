import numpy as np

board = np.zeros((6,6))
board[2,0] = 1
board[0,2] = -1

board[5,2] = 2

# board_lst = [i for lst in board for i in lst] 
# print(board_lst)

# def print_board(board):
#     board_lst = [i for lst in board for i in lst] 
#     head_col = "-------------------\n"
#     row = [""] * len(board)
#     for i in range(len(row)):
#         row[i] += '|'
#         for ele in board_lst[i * 6 : (i + 1) * 6]:
#             if ele == 0:
#                 row[i] += '  |'
#             elif ele == 1:
#                 row[i] += 'P1|'
#             elif ele == -1:
#                 row[i] += 'P2|'
#             else:
#                 row[i] += '==|'
#         row[i] += '\n'
#     head = ""
#     head += head_col
#     for row_ele in row:
#         head += row_ele
#     head += head_col
#     print(head)
#     pass


def print_board(board):
        head_col = "      "
        for ele in range(0,len(board)):
            head_col += str(ele)
            head_col += '  '
        line = "    "
        line += "-" * 19
        line += '\n'
        head_col += '\n'
        head_col += line
        row = [""] * len(board)
        index = 0
        for i in range(len(board)):
            row[i] += str(i)
            row[i] += '   |'
            for ele in board[index]:
                if ele == 1:
                    row[i] += 'P1|'
                elif ele == -1:
                    row[i] += 'P2|'
                elif ele == 0:
                    row[i] += '  |'
                else:
                    row[i] += 'XX|'
            row[i] += '\n'
            index += 1
        for ele in row:
            head_col += ele
        line = "    "
        line += "-" * 19
        line += '\n'
        head_col += line
        print(head_col)

print_board(board)
