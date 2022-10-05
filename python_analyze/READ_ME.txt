EDIT: I will change the code so that instead of parsing one file with multiple games, it parses multiples files with one game each. This will be easier to scale, as suggested by Bill Qian. I should have the code ready by tomorrow, Oct 2.

Hi Everyone, Gabriel here!

This directory contains four files:
1. Hans_Moke_Niemann.pgn - pgn file containing all Niemann's FIDE games;
2. test_pgn.pgn - a smaller version of that file to test the scripts on;
3. pgn_parser_jupyter.ipynb - Jupyter notebook that parses pgn files and does multiple things with them (more details later);
4. app.py - Python script that does the same thing as the notebook.

REQUIREMENTS:
1. You must have a chess engine installed in your computer. I am using Stockfish 15. You can find it at https://stockfishchess.org/download/. Take note of where it is in your computer, as you will need this information later.
2. You must install a few Python packages. Running 'pip install chess pandas numpy' should do the trick.

HOW TO USE:
Start by setting up a few global variables. 
1. engine - path to your engine. In my case, it's "/usr/local/bin/stockfish";
2. pgn_test - path to pgn file;
3. num_moves - the number of variations you want the engine to output;
4. depth_limit - how deep the engine should go;
5. time_limit - for how long the engine should analyze each position. It's set to 0.01 by default to make testing quicker, but that's not enough time to get anything good out of it.
NOTE: Whatever limit is reached first will be the binding limit. That is, if depth_limit is reached first, then the engine will stop calculating regardless of how much time has passed.

I have already set up examples in both the Jupyter notebook and the Python script. So you should get a basic example by simply running either one of them. Nonetheless, if you want to experiment with them, I briefly documented all functions.

Please let me know if you have any questions.

Possible improvements:
 - If you'd like to analyze the games with multiple engines, I believe the easiest way to do this would be to download all these engines and create a variable for each one. Then run the script multiple times, one for each engine.
- I wrote this aiming for simplicity and ease of use. However, the script can be somewhat inefficient at times. If you have any suggestions, please let me know. I might create a github repo later to make this easier.


