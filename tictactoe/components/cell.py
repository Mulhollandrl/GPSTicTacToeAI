import pygame
import tictactoe.enums.STATES as state
from tictactoe.enums.COLORS import *

LINEWIDTH = 8

class Cell:
    def __init__(self, dimensions, corners) -> None:
        self.state = state.STATEEMPTY
        self.dimensions = dimensions
        self.corners = corners
        
    def update_state(self, state) -> int:
        if self.state != 0:
            return 0
        else:
            self.state = state
            return 1
        
    def render(self, surface) -> None:
        if self.state == state.STATEX:
            pygame.draw.line(surface, BLACK, 
                            (self.corners[0], self.corners[1]), 
                            (self.corners[2], self.corners[3]), 5)
            
            pygame.draw.line(surface, BLACK, 
                            (self.corners[2], self.corners[1]), 
                            (self.corners[0], self.corners[3]), 5)
        elif self.state == state.STATEO:
            pygame.draw.circle(surface, BLACK, 
                               (self.corners[0] + (self.corners[2] - self.corners[0]) // 2,
                                self.corners[1] + (self.corners[3] - self.corners[1]) // 2),
                               (self.corners[2] - self.corners[0]) // 2, 5)