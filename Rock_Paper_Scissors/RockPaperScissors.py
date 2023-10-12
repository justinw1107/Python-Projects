import random

class My_class:
  def __init__(self):
    self.player = ''
    self.computer = ''
    self.result = ''
    self.total = []
  
  def pick_hands(self):
    rps_outcomes = ('rock', 'paper', 'scissors')
    x = random.randint(0,2)
    y = random.randint(0,2)
    self.player = rps_outcomes[x]
    self.computer = rps_outcomes[y]
    print(self.player, self.computer)
    
    
  def compute_round(self, rounds):
    for x in range(rounds):
      self.pick_hands()
      
      if self.player == 'rock':
        if self.computer == 'rock':
          self.result = 'tie'
        elif self.computer == 'paper':
          self.result = 'lose'
        else:
          self.result = 'win'
      elif self.player == 'paper':
        if self.computer == 'rock':
          self.result = 'win'
        elif self.computer == 'paper':
          self.result = 'tie'
        else:
          self.result = 'lose'
      else:
        if self.computer == 'rock':
          self.result = 'lose'
        elif self.computer == 'paper':
          self.result = 'win'
        else:
          self.result = 'tie'
          
      self.total.append(self.result)
    
    
  def add_result(self):
    self.compute_round(10)
    for x in range(self.total):
      print(self.total[x])
      
    
            
    

obj = My_class()
obj.add_result()
