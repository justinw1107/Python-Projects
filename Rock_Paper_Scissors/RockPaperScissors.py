import random

class My_class:
  def __init__(self):
    self.results = []
    self.total = []
    self.wins = 0
    self.ties = 0
    self.losses = 0
    self.outcomes = []
    self.outcomehelper = []
  
  
  def pick_hands(self):
    rps_outcomes = ('rock', 'paper', 'scissors')
    self.player = random.choice(rps_outcomes)
    self.computer = random.choice(rps_outcomes)
    
    
  def compute_round(self, rounds):
    outcomes_dictionary = {
      ('rock', 'rock'): 'tie',
      ('rock', 'paper'): 'lose',
      ('rock', 'scissors'): 'win',
      ('paper', 'rock'): 'win',
      ('paper', 'paper'): 'tie',
      ('paper', 'scissors'): 'lose',
      ('scissors', 'rock'): 'lose',
      ('scissors', 'paper'): 'win',
      ('scissors', 'scissors'): 'tie'
    }
    
    
    
    for x in range(rounds):
      self.pick_hands()
      result = outcomes_dictionary[(self.player, self.computer)]
      self.results.append(result)
    
    
  def add_result(self):
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

    for result in self.results:
      print(f"Result: {result}")
      

    
  def write_result(self):
    self.add_result()
    f = open("Rock_Paper_Scissors/results.txt", "w")
    for x in self.results:
      f.write(str(x) + '\n')
    
    
      
    
            
    

obj = My_class()
obj.write_result()
