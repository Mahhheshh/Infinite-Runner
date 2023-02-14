from src import create_game, fps

if __name__ == "__main__":
    game = create_game()
    while True:
        game.gameloop()
        fps.tick(30)