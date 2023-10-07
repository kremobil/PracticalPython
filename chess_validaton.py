def is_valid_chess_board(board:dict):
    bkings = 0
    wkings = 0 
    for figure in board.values():
        if figure == 'bking':
            bkings += 1
        elif figure == 'wking':
            wkings += 1
    if bkings != 1 or wkings != 1:
        return False
    
    wfigures = 0
    bfigures = 0

    for figure in board.values():
        if figure[0] == 'w':
            wfigures += 1
        elif figure[0] == 'b':
            bfigures += 1
        else: 
            print(figure)
            return False
        
        if figure[1:] not in ["pawn", "knight", "bishop", "rook", "queen", "king"]:
            print(figure)
            return False

    if wfigures > 16 or bfigures > 16:
        return False
    
    for position in board.keys():
        if int(position[0]) < 0 or int(position[0]) > 8 or position[1] not in [chr(ord('a') + i) for i in range(8)]:
            print(position)
            return False

    return True

board = {"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}

print(is_valid_chess_board(board))