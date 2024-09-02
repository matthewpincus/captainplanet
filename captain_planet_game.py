import random

class CaptainPlanetGame:
    def __init__(self):
        self.player_health = 100
        self.eco_villains = ["Hoggish Greedly", "Dr. Blight", "Verminous Skumm", "Duke Nukem", "Looten Plunder"]
        self.current_villain = None
        self.villain_health = 0

    def start_game(self):
        print("Welcome, Planeteer! Earth needs your help!")
        self.choose_villain()
        return self.game_loop()

    def choose_villain(self):
        self.current_villain = random.choice(self.eco_villains)
        self.villain_health = 100
        return f"Oh no! {self.current_villain} is causing environmental havoc! Stop them!"

    def game_loop(self):
        while self.player_health > 0 and self.villain_health > 0:
            action = input("Choose your action: (1) Earth, (2) Fire, (3) Wind, (4) Water, (5) Heart: ")
            if action not in ["1", "2", "3", "4", "5"]:
                return "Invalid action! Choose a number between 1 and 5."
            
            player_damage = random.randint(10, 20)
            villain_damage = random.randint(5, 15)
            
            self.villain_health -= player_damage
            self.player_health -= villain_damage
            
            result = f"You dealt {player_damage} damage to {self.current_villain}!\n"
            result += f"{self.current_villain} dealt {villain_damage} damage to you!\n"
            result += f"Your health: {self.player_health}, Villain health: {self.villain_health}\n"
            
            if self.villain_health <= 0:
                return result + f"Congratulations! You defeated {self.current_villain}! The planet is safe... for now."
            elif self.player_health <= 0:
                return result + "Oh no! You've been defeated. Better luck next time, Planeteer!"
            
            return result

game = CaptainPlanetGame()
