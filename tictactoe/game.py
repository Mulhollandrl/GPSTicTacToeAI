import sys
import pygame
import tictactoe.enums.STATES as state
from pygame.locals import *
from tictactoe.enums.COLORS import *
from tictactoe.components.board import Board

BOARDSIZE = 3
FPS = 60
SCREENWIDTH = 600

class Game():
    def __init__(self) -> None:
        self.SCREENWIDTH = SCREENWIDTH
        self.board = Board(BOARDSIZE, SCREENWIDTH)
        self.cells_to_update = []
        self.current_player_x = True
        self.game_over = False
        
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        
        self.DISPLAYSURF = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENWIDTH))
        self.FPS = pygame.time.Clock()
        
        self.FPS.tick(FPS)
        
        
    def process_input(self) -> int:
        corners = self.board.get_corners()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    raise ConnectionResetError
            elif event.type == pygame.MOUSEBUTTONDOWN and self.game_over == False:
                pos = pygame.mouse.get_pos()
                
                for i, corner in enumerate(corners):
                    if corner[2] > pos[0] > corner[0] and corner[3] > pos[1] > corner[1]:
                        if self.current_player_x:   
                            self.cells_to_update.append((i, state.STATEX))
                        else:
                            self.cells_to_update.append((i, state.STATEO))
                
    def update(self) -> int:
        success = self.board.update(self.cells_to_update)
        
        if success == 1 and len(self.cells_to_update) != 0:
            self.current_player_x = not self.current_player_x
            print()
        elif success == 2:
            self.game_over = True
            
        self.cells_to_update = []
    
    def render(self) -> int:
        self.DISPLAYSURF.fill(WHITE)
        self.board.render(self.DISPLAYSURF)
        pygame.display.update()

    def process_gps_input(self, cell):
        if not self.current_player_x:
            # Cell should be passed in by the one that corresponds to the name in BOARDTILES.py
            self.cells_to_update.append((cell))
            return True

        return False
    
    def game_loop(self):
        self.process_input()
        self.update()
        self.render()

while __name__ == "__main__":
    game = Game()
    
    while True:
        try:
            game.game_loop()
        except ConnectionResetError:
            game = Game()