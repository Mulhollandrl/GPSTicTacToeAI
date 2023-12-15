from tictactoe.game import Game
from gps.gps_main import GPS_Player
from gps.enums.BOARDTILES import NAME_TO_TILES

if __name__ == "__main__":
    game = Game()
    ai_player = GPS_Player()

    while True:
        game.game_loop()
        
        if not game.current_player_x:
            game.process_gps_input(NAME_TO_TILES[ai_player.get_current_step_name()])