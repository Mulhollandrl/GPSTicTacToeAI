import pygame
import enums.STATES as state
from components.cell import Cell
from enums.COLORS import *

class Board:
    def __init__(self, BOARDSIZE, SCREENSIZE) -> None:
        self.BOARDSIZE = BOARDSIZE
        self.SCREENSIZE = SCREENSIZE
        self.OFFSET = SCREENSIZE//BOARDSIZE
        self.game_over = False
        self.winner = None
        self.cells = []
        
        for i in range(BOARDSIZE*BOARDSIZE):
            x_index = i % self.BOARDSIZE
            y_index = i // self.BOARDSIZE
            self.cells.append(Cell(SCREENSIZE//BOARDSIZE, 
                                   (x_index * self.OFFSET, y_index * self.OFFSET, 
                                    (x_index + 1) * self.OFFSET, (y_index + 1) * self.OFFSET)))
            
    def get_corners(self) -> list[tuple[int, int, int, int]]:
        all_corners = []
        
        for cell in self.cells:
            all_corners.append(cell.corners)
            
        return all_corners
        
    def update(self, cells_to_update) -> int:
        rows = [self.cells[i:i+self.BOARDSIZE] for i in range(0, len(self.cells), self.BOARDSIZE)]
        cols = [[row[i] for row in rows] for i in range(self.BOARDSIZE)]
        diag_left_right = [self.cells[i*self.BOARDSIZE + i] for i in range(self.BOARDSIZE)]
        diag_right_left = [self.cells[i*self.BOARDSIZE + (self.BOARDSIZE - i - 1)] for i in range(self.BOARDSIZE)]
        
        for row in rows:
            current_looking_state = state.STATEEMPTY
            skip_row = False
            
            for index, cell in enumerate(row):
                if cell.state != current_looking_state:
                    if current_looking_state == state.STATEEMPTY and index == 0:
                        current_looking_state = cell.state
                    else:
                        skip_row = True
                        break
                    
            if skip_row:
                continue
            elif current_looking_state != state.STATEEMPTY:
                self.winner = current_looking_state
                self.game_over = True
                return 2
            
        for col in cols:
            current_looking_state = state.STATEEMPTY
            skip_col = False
            
            for index, cell in enumerate(col):
                if cell.state != current_looking_state:
                    if current_looking_state == state.STATEEMPTY and index == 0:
                        current_looking_state = cell.state
                    else:
                        skip_col = True
                        break
                    
            if skip_col:
                continue
            elif current_looking_state != state.STATEEMPTY:
                self.winner = current_looking_state
                self.game_over = True
                return 2
            
        current_looking_state = state.STATEEMPTY
        
        for index, cell in enumerate(diag_left_right):
            if cell.state != current_looking_state:
                if current_looking_state == state.STATEEMPTY and index == 0:
                    current_looking_state = cell.state
                else:
                    break
            else:
                if index == len(diag_left_right) - 1 and current_looking_state != state.STATEEMPTY:
                    self.winner = current_looking_state
                    self.game_over = True
                    return 2
                
        current_looking_state = state.STATEEMPTY
                
        for index, cell in enumerate(diag_right_left):
            if cell.state != current_looking_state:
                if current_looking_state == state.STATEEMPTY and index == 0:
                    current_looking_state = cell.state
                else:
                    break
            else:
                if index == len(diag_left_right) - 1 and current_looking_state != state.STATEEMPTY:
                    self.winner = current_looking_state
                    self.game_over = True
                    return 2
        
        for cell_index, cell_state in cells_to_update:
            success = self.cells[cell_index].update_state(cell_state)
            
            if success == 0:
                return 0
            
        return 1    
    
    def render(self, surface) -> None:
        corners = self.get_corners()
        
        for i, corner in enumerate(corners):
            if not(i % self.BOARDSIZE == 0 or i >= self.BOARDSIZE):
                pygame.draw.line(surface, BLACK, 
                            (corner[0], 0), 
                            (corner[0], self.SCREENSIZE), 5)
                
            if (i + 1) % self.BOARDSIZE == 0 and not i == len(corners) - 1:
                pygame.draw.line(surface, BLACK, 
                            (0, corner[3]), 
                            (self.SCREENSIZE, corner[3]), 5)
        
        for cell in self.cells:
            cell.render(surface)
            
        if self.game_over:
            font = pygame.font.Font(None, 166)
            if self.winner == 1:
                self.winner = "X"
            else:
                self.winner = "O"
                
            text = font.render(f"{self.winner} Wins!", True, RED)
            text_width, text_height = text.get_size()
            
            surface.blit(text, ((self.SCREENSIZE - text_width) // 2, (self.SCREENSIZE - text_height) // 2))