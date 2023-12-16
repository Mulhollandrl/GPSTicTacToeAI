from tictactoe.game import Game
from gps.gps_main import GPS_Player
from gps.enums.BOARDTILES import NAME_TO_TILES
from tictactoe.enums import STATES as state

def check_for_invalid_steps(game):
    cell_steps = [key for key, value in NAME_TO_TILES.items()]
    invalid_steps = []

    for index, cell in enumerate(game.board.cells):
        if cell.state != state.STATEEMPTY:
            invalid_steps.append(cell_steps[index])

    return invalid_steps

if __name__ == "__main__":
    game = Game()
    ai_player = GPS_Player()

    while True:
        game.game_loop()
        
        if not game.current_player_x:
            ai_player.invalid_steps = check_for_invalid_steps(game)
            ai_player.check_step_paths_valid()
            ai_player.choose_step_path()
            processed = game.process_gps_input(NAME_TO_TILES[ai_player.get_current_step_name()])

            if processed:
                ai_player.increment_step()