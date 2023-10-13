import random

class RPS:
  def __init__(self):
    self.results = []
    self.wins = 0
    self.ties = 0
    self.losses = 0

  
  def pick_hands(self):
    rps_outcomes = ('Rock', 'Paper', 'Scissors')
    self.player = random.choice(rps_outcomes)
    self.computer = random.choice(rps_outcomes)
    
    
  def compute_round(self, rounds):
    outcomes_dictionary = {
      ('Rock', 'Rock'): 'Tie',
      ('Rock', 'Paper'): 'Lose',
      ('Rock', 'Scissors'): 'Win',
      ('Paper', 'Rock'): 'Win',
      ('Paper', 'Paper'): 'Tie',
      ('Paper', 'Scissors'): 'Lose',
      ('Scissors', 'Rock'): 'Lose',
      ('Scissors', 'Paper'): 'Win',
      ('Scissors', 'Scissors'): 'Tie'
    }
    
    for _ in range(rounds):
      self.pick_hands()
      result = outcomes_dictionary[(self.player, self.computer)]  
      
      if result == 'Win':
        self.wins += 1
      elif result == 'Tie':
        self.ties += 1
      else:
        self.losses += 1
        
      self.results.append((self.player, self.computer, result))
    
    
  def execute(self):
    while True:
      try:
        user_input = input('How many rounds would you like to play?\n')
        rounds = int(user_input)
        if rounds < 1:
          print('Please enter a number greater than 0')
          continue
        else:
          break
      except ValueError:
        print('Please enter a valid number')
    
    self.compute_round(rounds)
    
    print(f"Wins: {self.wins}\nTies: {self.ties}\nLosses: {self.losses}")
      

  def write_result(self):
    self.execute()

    f = open("Rock_Paper_Scissors/results.txt", "w")
    for player, computer, result in self.results:
      f.write(f"{player} VS {computer} : {result}\n")
    
    
      
game = RPS()
game.execute()
# game.write_result()
