'''Sources: https://python-chess.readthedocs.io/en/v1.7.0/engine.html, https://blog.propelauth.com/chess-analysis-in-python/, 
and https://github.com/official-stockfish/Stockfish.'''

import chess
import chess.pgn
import chess.engine
import pandas as pd
import sys

# Path to engine
engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

# Path to pgn file
pgn_test = 'pgns/Santarius__Erik_vs_Niemann__Hans_Moke_24th_Chicago_Open_2015_2015_05_25_12_12.pgn'

# Number of variations the engine should output
num_moves = 2

# Engine depth limit
depth_limit = 20

# Engine analysis time limit
time_limit = 0.01

# NOTE: Whatever limit is reached first will be the binding limit.

def analyze_position(board, num_moves_to_return=1, depth_limit=None, time_limit=None):
    '''Analyzes the board through a FEN string and returns a dictionary with three
    values:
        mate_score - number of moves to mate. Positive for white, negative for black.
        centipawn_score - centipawn score (1 cp = 1/100th of a pawn). Positive for white, negative for black.
        pv - sequence of moves suggested by the engine.
    
    These values rely on the following parameters:
        board - struct from `chess` package representing the current board's configuration.
        num_moves_to_return - he number of move sequences the engine should suggest.
        depth_limit - the depth each sequence goes to.
        time_limit - the engine stops analyzing moves when it hits this time limit,
    '''
    
    # Limits our search.
    search_limit = chess.engine.Limit(depth=depth_limit, time=time_limit)
    
    # Represents the information we want from our analysis.
    infos = engine.analyse(board, search_limit, multipv=num_moves_to_return)
    
    # Returns a dictionary containing all these values.
    return [format_info(info) for info in infos]
   
def format_info(info):
    '''Called by analyze_position to initiliase a dict
    containing the engine's analysis.
    '''
    
    # Always look from White's perspective.
    score = info["score"].white()
    
    # Initialises a dictionary with mate_score, centipawn_score and pv.
    mate_score = score.mate()
    centipawn_score = score.score()
    return {
        "mate_score": mate_score,
        "centipawn_score": centipawn_score,
        "pv": format_moves(info["pv"]),
    }

def format_moves(pv):
    '''Converts the move class to a standard string.
    '''
    
    return [move.uci() for move in pv]

def analyze_game(pgn, depth_limit=depth_limit, time_limit=time_limit):
    '''Analyzes individual game using `analyze_position`and returns 
    a list containing this analysis.
    
    These values rely on the following parameters:
        pgn - pgn containing ONLY ONE game in pgn format
        depth_limit - the depth each sequence goes to.
        time_limit - the engine stops analyzing moves when it hits this time limit,
    '''
    
    with open(pgn) as pgn:
        try:
            game = chess.pgn.read_game(pgn)
        except:
            print("Could not read game.")
        eng_output = []
        board = game.board()
        
        for move in game.mainline_moves():
            info = analyze_position(board=board, num_moves_to_return=num_moves, depth_limit=depth_limit, time_limit=time_limit)
            eng_output.append(info)
            board.push(move)

    return eng_output

def create_eval_df(eng_output):
    '''Creates a pandas dataframe from information the engine outputs
    for each move in a game.
    '''
    eval_lst = []
    counter = 1
    df_eval = pd.DataFrame()
    
    for i in range(0, len(eng_output)):
        eval_lst.append(
            pd.DataFrame(
                eng_output[i], 
                index = [f'{i+1}_line_{counter}_move' for i in range(0, num_moves)]
                )
            )
        counter += 1
    df_eval = pd.concat(eval_lst)
    return df_eval

def lst_eval_df(pgn):
    '''Returns a dataframs containing the analyzed game.
    '''
    game = analyze_game(pgn=pgn, depth_limit=depth_limit, time_limit=time_limit)
    return create_eval_df(eng_output=game)

if __name__ == "__main__":
    ### Example usage
    print(lst_eval_df(pgn_test))
    # print(lst_eval_df(sys.argv[1])) also works perfectly fine.
