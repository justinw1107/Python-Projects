import random

class My_class:
  def __init__(self):
    self.player = ''
    self.computer = ''
    self.result = ''
    self.total = []
    self.wins = 0
    self.ties = 0
    self.losses = 0
  
  
  def pick_hands(self):
    rps_outcomes = ('rock', 'paper', 'scissors')
    x = random.randint(0,2)
    y = random.randint(0,2)
    self.player = rps_outcomes[x]
    self.computer = rps_outcomes[y]
    
    
  def compute_round(self, rounds):
    for x in range(rounds):
      self.pick_hands()
      
      if self.player == 'rock':
        if self.computer == 'rock':
          self.result = 'tie'
          self.ties += 1
        elif self.computer == 'paper':
          self.result = 'lose'
          self.losses += 1
        else:
          self.result = 'win'
          self.wins += 1
          
      elif self.player == 'paper':
        if self.computer == 'rock':
          self.result = 'win'
          self.wins += 1
        elif self.computer == 'paper':
          self.result = 'tie'
          self.ties += 1
        else:
          self.result = 'lose'
          self.losses += 1
          
      else:
        if self.computer == 'rock':
          self.result = 'lose'
          self.losses += 1
        elif self.computer == 'paper':
          self.result = 'win'
          self.wins += 1
        else:
          self.result = 'tie'
          self.ties += 1
          
      self.total.append(self.result)
    
    
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
    for x in self.total:
      print(x)
      
    print('Wins: ' + str(self.wins))
    print('Ties: ' + str(self.ties))
    print('Losses: ' + str(self.losses))
      
    
            
    

obj = My_class()
obj.add_result()
