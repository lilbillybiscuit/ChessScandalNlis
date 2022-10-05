import sys 
import chess.pgn 
import io 

# This function splits the file into multiple games that in a certain directory 

def split_file(input, output_directory):
    pgn_file = open(input, 'r').read()   #Reading the file
    for game in pgn_file.split('[Event')[1:]:
        game = "[Event" + game  # As we have split by the "[Event" keyword, we have to bring it back as python makes it disappear 
        game_cpy = io.StringIO(game)  
        game_cpy = chess.pgn.read_game(game_cpy)
        black = game_cpy.headers['Black']
        white = game_cpy.headers['White']
        date = game_cpy.headers['Date'].replace(".", "_")
        result = game_cpy.headers['Result'].replace("/", "")
        event = game_cpy.headers['Event']
        filename = ((str(black) + "_vs_" + str(white) + "_" + str(event) + "_" + str(date) + "_" + str(result)+ ".pgn").replace(" ", "_")).replace(",","_").replace("-", "_")
        file = open(output_directory + "/" +filename, "w")
        file.write(game)
        file.close()


# Example 
split_file(sys.argv[1], sys.argv[2])