import json

class Game:
    def __init__(self, player_name, score, level=None, items=None, version=1):
        self.player_name = player_name
        self.score = score
        self.level = level if level is not None else 1
        self.items = items if items is not None else []
        self.version = version

    def save_state(self, filename):
        game_state = {
            'version': self.version,
            'player_name': self.player_name,
            'score': self.score,
            'level': self.level,
            'items': self.items
        }
        
        with open(filename, 'w') as file:
            json.dump(game_state, file, indent=4)
        print(f"Game state saved to {filename} (version {self.version})")

    @classmethod
    def load_state(cls, filename):
        try:
            with open(filename, 'r') as file:
                game_state = json.load(file)
            
            version = game_state.get('version', 1)

            if version == 1:
                print("Loading game state from version 1...")
                game_state['level'] = 1
                game_state['items'] = []

            return cls(
                player_name=game_state['player_name'],
                score=game_state['score'],
                level=game_state['level'],
                items=game_state['items'],
                version=version
            )
        except FileNotFoundError:
            print("No saved game found.")
            return None

    def display_state(self):
        print(f"Player: {self.player_name}")
        print(f"Score: {self.score}")
        print(f"Level: {self.level}")
        print(f"Items: {', '.join(self.items)}")
        print(f"Version: {self.version}")

if __name__ == "__main__":
    game_v1 = Game(player_name="TestPlayer", score=20)
    game_v1.save_state("game_v1.json")
    
    game_v2 = Game(player_name="TestPlayer", score=100, level=5, items=["Sword", "Strength Potion"], version=2)
    game_v2.save_state("game_v2.json")

    restored_game_v1 = Game.load_state("game_v1.json")
    if restored_game_v1:
        restored_game_v1.display_state()

    restored_game_v2 = Game.load_state("game_v2.json")
    if restored_game_v2:
        restored_game_v2.display_state()