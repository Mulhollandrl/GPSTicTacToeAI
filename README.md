# Tic Tac Toe with AI opponent
### Using GPS as based on the model described by A. Newell and H. A. Simon in "GPS, A Program that Simulates Human Thought"

## Dependencies

This program runs on Python 3.12. This is the only tested version. It uses PyGame 2.5.2.

## Installation

First, navigate to the github repo (congrats! you are already there!). Now go to the "*<> Code*" button and click it, then click on "*Download ZIP*".

Navigate to the zip that you just downloaded, and unzip the folder. Now open up that folder, as well as a terminal in that folder. Run
```
pip install -r requirements.txt
```

This will download all of the dependencies for you (except Python 3.12).

Now run "*game.py*" in the "*tictactoe*" folder to play Tic Tac Toe.

## Video

There is a video going over the Game as well as the code [here](https://youtu.be/Vp3YCs2kCrg).

The first 4.5 minutes are spent on the overview of the game, and the rest is spent on the code.

## Notes on Implementation

Unfortunately, I ran into a few problems trying to get GPS to work with Tic Tac Toe, so it is not a pure GPS implementation, even if it does get pretty close!

Additionally, I have only implemented one algorithm for the AI, that being a greedy algorithm. All it will do at the moment is try to find the shortest path to IT winning, and will NEVER purposefully obstruct you. 

## Future Development

There are three main things that would be quite apparently interesting to pursue for future development:

1. **Implement obstruction**: Right now, the AI does not purposefully obstruct the player. It may be fun to make it so that it wants to do this.

2. **Implement other path choosing algorithms**: Right now, the AI is only ever greedy. A more purposeful plan for choosing a step path may help it succeed more often.

3. **Implement AI being first player**: Currently, the AI is always the 2nd player, which (in the game of Tic Tac Toe) inherently puts it at a disadvantage! It would be nice to have it go first at least sometimes!

Additionally, there are some other avenues to pursue:

1. **Varied sizes of boards**: 3x3 boards are the only boards you can play with the AI right now. Implementing more rules and logic to facilitate a 5x5 or such would be nice!

2. **Menuing and better game**: Currently the game is pretty barebones. It may be nice to make it better looking, and even possibly add menus to get different playstyles!

3. **Use an executable to run the game**: Currently you have to run the game in an IDE or such, and it is not super user friendly. This makes it hard to send to non coder friends (or people not using Python 3.12).

# THANK YOU FOR CHECKING THIS OUT!
## - Richard Mulholland