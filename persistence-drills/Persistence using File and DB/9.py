import json

class Game:
    def __init__(self, player_name, score, level, items):
        self.player_name = player_name
        self.score = score
        self.level = level
        self.items = items

    def save_state(self, filename):
        game_state = {
            'player_name': self.player_name,
            'score': self.score,
            'level': self.level,
            'items': self.items
        }
        
        with open(filename, 'w') as file:
            json.dump(game_state, file, indent=4)
        print(f"Game state saved to {filename}")

    @classmethod
    def load_state(cls, filename):
        try:
            with open(filename, 'r') as file:
                game_state = json.load(file)
            return cls(
                player_name=game_state['player_name'],
                score=game_state['score'],
                level=game_state['level'],
                items=game_state['items']
            )
        except FileNotFoundError:
            print("No saved game found.")
            return None

    def display_state(self):
        print(f"Player: {self.player_name}")
        print(f"Score: {self.score}")
        print(f"Level: {self.level}")
        print(f"Items: {', '.join(self.items)}")

if __name__ == "__main__":
    game = Game(player_name="EpicGamer", score=100, level=5, items=["Sword", "Stength Potion"])

    game.save_state("game_state.json")

    restored_game = Game.load_state("game_state.json")
    if restored_game:
        restored_game.display_state()