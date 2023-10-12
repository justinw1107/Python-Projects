import random

class My_class:
  def pick_hand(self, player, computer):
    rps_outcomes = ('rock', 'paper', 'scissors')
    x, y = random.randint(1,3)
    player = rps_outcomes[x]
    computer = rps_outcomes[y]
    
    return player, computer
    
    
  # def compute_round(self, rounds*):
    

obj = My_class()
obj.instance_method()